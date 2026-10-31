#!/usr/bin/env python3
"""Daily claims delta runner. Usage: python daily_delta.py VP.xlsx INTER.xlsx [YYYY-MM-DD] [snap]
Reads ops/claims_snapshot.json as baseline, prints deltas, writes new snapshot.

Wins are identified by SET DIFF on per-row fingerprints, not by count + bottom-append.
A row that flips to green mid-sheet (an existing filed claim that gets won) is detected
correctly, and its amount is read off that row — never a stale bottom row.
Snapshot stores per-client won fingerprints under vp[client]['fp'] so each day diffs exactly.
Falls back to count-only on first run / legacy snapshots (no 'fp'); starts storing fp then.
"""
import json, sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from claims_engine import analyze, row_color
GUESTY = {'EliteNest', 'Royal Vista'}

def amt(s):
    s = (s or '').replace(',', '').strip()
    m = re.search(r'-?\d+\.?\d*', s)
    return float(m.group()) if m else None

def fingerprint(vals):
    """Stable per-row key: all non-empty cell texts in column order."""
    return '|'.join(x[0].strip() for c, x in sorted(vals.items()) if x[0].strip())

def won_rows(tab, rows):
    """List of (rownum, vals) counted as won for this tab."""
    c = tab.replace(' - Claim Tracker', '').strip()
    if c in GUESTY:
        return [(rn, v) for rn, v in rows[1:] if any(x[0].strip() for x in v.values())]
    return [(rn, v) for rn, v in rows[1:] if row_color(v) == 'green']

def received_amt(vals, hdr):
    pr = [(x[0].strip().lower(), k) for k, x in hdr.items()]
    rec = next((k for tt, k in pr if 'reciev' in tt or 'receiv' in tt), None)
    clm = next((k for tt, k in pr if 'amount' in tt), None)
    v = amt(vals.get(rec, ('', ''))[0]) if rec else None
    if v is None and clm:
        v = amt(vals.get(clm, ('', ''))[0])
    return v or 0

def run(vpx, inx, date, snap_path):
    base = json.load(open(snap_path))
    bvp = base['vp']
    bi = base['inter']
    vp = analyze(vpx)
    newvp = {}
    changed = []
    for tab, rows in vp.items():
        if not rows:
            continue
        c = tab.replace(' - Claim Tracker', '').strip()
        wr = won_rows(tab, rows)
        hdr = rows[0][1]
        curfps = {fingerprint(v): v for _, v in wr}
        newvp[c] = {'won': len(wr), 'fp': sorted(curfps.keys())}
        bentry = bvp.get(c)
        if bentry is None:
            changed.append(f"{c}: NEW tab {len(wr)} won")
            continue
        bfp = set(bentry.get('fp') or [])
        if bentry.get('fp') is None:
            # legacy snapshot: no fingerprints to diff; report count change only
            if len(wr) != bentry['won']:
                changed.append(f"{c}: +{len(wr)-bentry['won']} won (amount n/a: baseline had no row detail)")
        else:
            added = [fp for fp in curfps if fp not in bfp]
            if added:
                tot = sum(received_amt(curfps[fp], hdr) for fp in added)
                names = ', '.join((curfps[fp].get('E', ('', ''))[0] or curfps[fp].get('C', ('', ''))[0] or '?')[:20] for fp in added)
                changed.append(f"{c}: +{len(added)} won, {tot:,.0f} AED ({names})")
    # Inter
    inter = analyze(inx)
    rows = inter.get('Claims') or list(inter.values())[0]
    st = {'green': 0, 'yellow': 0, 'red': 0, 'none': 0}
    tot = 0
    gfps = {}
    for rn, v in rows[1:]:
        col = row_color(v) or 'none'
        st[col] = st.get(col, 0) + 1
        if col == 'green':
            tot += amt(v.get('K', ('', ''))[0]) or 0
            gfps[fingerprint(v)] = v
    bifp = set(bi.get('fp') or [])
    dwon = st['green'] - bi['won']
    print("VP vs %s: %s" % (base['date'], changed if changed else "NONE"))
    print("Inter: Won {}({:+d}) Ongoing {}({:+d}) Lost {}({:+d}) Pending {}({:+d}) recv{:+,.0f}".format(
        st['green'], dwon, st['yellow'], st['yellow']-bi['ongoing'], st['red'], st['red']-bi['lost'],
        st['none'], st['none']-bi['pending'], tot-bi['won_received_thb']))
    if bi.get('fp') is not None:
        for fp in [f for f in gfps if f not in bifp]:
            v = gfps[fp]
            print("  new won:", (v.get('C', ('', ''))[0] or '')[:22], amt(v.get('K', ('', ''))[0]), "THB")
    elif dwon > 0:
        for rn, v in [r for r in rows[1:] if row_color(r[1]) == 'green'][-dwon:]:
            print("  new won:", (v.get('C', ('', ''))[0] or '')[:22], amt(v.get('K', ('', ''))[0]), "THB")
    snap = {'date': date, 'vp': newvp,
            'inter': {'won': st['green'], 'ongoing': st['yellow'], 'lost': st['red'],
                      'pending': st['none'], 'won_received_thb': int(tot),
                      'fp': sorted(gfps.keys())}}
    json.dump(snap, open(snap_path, 'w'), indent=1)

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else 'ops/claims_snapshot.json')
