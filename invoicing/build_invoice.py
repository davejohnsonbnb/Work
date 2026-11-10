"""VirtuPro invoice PDF builder (house teal template).

Usage: python3.13 build_invoice.py spec.json [outdir]
spec.json is a list of invoice dicts:
  no, client, addr (list), date, ccy, period (default period text for lines),
  lines: [{title, sub?, qty?, rate?, amount, tax?}],
  eur_rate?, rate_date?  -> adds an EUR reference total (USD invoices),
  tax_col? (bool), footnote?
"""
import json
import os
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle)

TEAL = colors.Color(14 / 255, 144 / 255, 154 / 255)
GREY = colors.Color(0.42, 0.42, 0.42)
LINE = colors.Color(0.80, 0.80, 0.80)
ISSUER = ["5900 Balcones Drive, Suite 165", "Austin, TX 78731", "United States",
          "+1 332 252 2342", "ahmed@virtupro.io", "www.virtupro.io"]
_ss = getSampleStyleSheet()


def P(size=9, font="Helvetica", color=colors.black, align=TA_LEFT):
    return ParagraphStyle("x", parent=_ss["Normal"], fontName=font, fontSize=size,
                          textColor=color, alignment=align, leading=size * 1.3)


def money(x):
    return f"{x:,.2f}"


def build(inv, outdir="."):
    out = os.path.join(outdir, inv["no"] + ".pdf")
    doc = BaseDocTemplate(out, pagesize=letter, leftMargin=50, rightMargin=50,
                          topMargin=46, bottomMargin=46)
    doc.addPageTemplates([PageTemplate(id="m", frames=[
        Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")])])
    s = []

    comp = [Paragraph("VirtuPro LLC", P(13, "Helvetica-Bold")), Spacer(1, 4)]
    comp += [Paragraph(ln, P(9, "Helvetica", GREY)) for ln in ISSUER]
    h = Table([[comp, [Paragraph("Invoice", P(23, "Helvetica-Bold", TEAL, TA_RIGHT))]]],
              colWidths=[3.4 * inch, 3.7 * inch])
    h.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    s += [h, Spacer(1, 22)]

    bt = [Paragraph("BILL TO", P(8, "Helvetica-Bold", GREY)), Spacer(1, 4),
          Paragraph(inv["client"], P(10, "Helvetica-Bold"))]
    bt += [Paragraph(ln, P(9, "Helvetica", GREY)) for ln in inv.get("addr", [])]
    meta = [["INVOICE NO.", inv["no"]], ["DATE", inv["date"]], ["DUE DATE", inv["date"]],
            ["TERMS", inv.get("terms", "Due on receipt")], ["CURRENCY", inv["ccy"]]]
    mt = Table([[Paragraph(k, P(8, "Helvetica-Bold", GREY, TA_RIGHT)),
                 Paragraph(v, P(9, "Helvetica-Bold", colors.black, TA_RIGHT))] for k, v in meta],
               colWidths=[1.2 * inch, 1.9 * inch])
    mt.setStyle(TableStyle([("TOPPADDING", (0, 0), (-1, -1), 1),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                            ("LEFTPADDING", (0, 0), (-1, -1), 2),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    tt = Table([[bt, mt]], colWidths=[3.6 * inch, 3.5 * inch])
    tt.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 0),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    s += [tt, Spacer(1, 24)]

    tax_col = inv.get("tax_col", False)
    hdr = ["DESCRIPTION"] + (["TAX"] if tax_col else []) + ["QTY", "RATE", "AMOUNT"]
    rows = [[Paragraph(c, P(8.5, "Helvetica-Bold", colors.white,
                            TA_LEFT if i == 0 else TA_RIGHT)) for i, c in enumerate(hdr)]]
    total = 0.0
    for ln in inv["lines"]:
        sub = ln.get("sub", "Invoice for the period " + inv["period"] if "period" in inv else "")
        desc = f"<b>{ln['title']}</b>" + (f"<br/>{sub}" if sub else "")
        row = [Paragraph(desc, P(9))]
        if tax_col:
            row.append(Paragraph(ln.get("tax", ""), P(9, align=TA_RIGHT)))
        row += [Paragraph(str(ln.get("qty", "")), P(9, align=TA_RIGHT)),
                Paragraph(money(ln["rate"]) if "rate" in ln else "", P(9, align=TA_RIGHT)),
                Paragraph(money(ln["amount"]), P(9, align=TA_RIGHT))]
        rows.append(row)
        total += ln["amount"]
    widths = ([3.75, 0.55, 0.5, 1.0, 1.1] if tax_col else [4.3, 0.7, 1.0, 1.1])
    it = Table(rows, colWidths=[w * inch for w in widths])
    it.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), TEAL),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("TOPPADDING", (0, 0), (-1, 0), 7), ("BOTTOMPADDING", (0, 0), (-1, 0), 7),
                            ("TOPPADDING", (0, 1), (-1, -1), 9), ("BOTTOMPADDING", (0, 1), (-1, -1), 9),
                            ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                            ("LINEBELOW", (0, 1), (-1, -1), 0.5, LINE)]))
    s += [it, Spacer(1, 8)]

    trows = [[Paragraph("SUBTOTAL", P(9, "Helvetica", GREY, TA_RIGHT)),
              Paragraph(money(total), P(9, align=TA_RIGHT))],
             [Paragraph("TOTAL DUE", P(11, "Helvetica-Bold", colors.black, TA_RIGHT)),
              Paragraph(f"{inv['ccy']} {money(total)}", P(13, "Helvetica-Bold", TEAL, TA_RIGHT))]]
    if inv.get("eur_rate"):
        eur = round(total * inv["eur_rate"], 2)
        trows += [[Paragraph("", P(9)), Paragraph("EUR " + money(eur),
                                                  P(10, "Helvetica-Bold", colors.black, TA_RIGHT))],
                  [Paragraph("", P(9)), Paragraph(
                      f"1 USD = {inv['eur_rate']:.6f} EUR ({inv.get('rate_date', '')})",
                      P(8, "Helvetica", GREY, TA_RIGHT))]]
    tot = Table(trows, colWidths=[5.0 * inch, 2.1 * inch])
    tot.setStyle(TableStyle([("RIGHTPADDING", (0, 0), (-1, -1), 8),
                             ("TOPPADDING", (0, 1), (-1, 1), 8),
                             ("LINEABOVE", (0, 1), (-1, 1), 1, LINE)]))
    s += [tot, Spacer(1, 20),
          Paragraph(inv.get("footnote",
                            "VAT: under review — not applied on this invoice pending confirmation."),
                    P(8.5, "Helvetica", GREY))]
    doc.build(s)
    return out, total


if __name__ == "__main__":
    specs = json.load(open(sys.argv[1]))
    outdir = sys.argv[2] if len(sys.argv) > 2 else "."
    for inv in specs:
        f, t = build(inv, outdir)
        print(f"{inv['no']:8s} {inv['client'][:36]:36s} {inv['ccy']} {t:,.2f}")
