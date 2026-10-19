# Invoice Ledger

System of record for all BNB Pro invoicing. Numbering is **per-client** (sequences
may overlap across clients). Keep this updated on every issue and every payment.

Status legend: **Issued** (sent, awaiting payment) · **Paid** · **Draft** (not yet issued).
Terms are "due on receipt" unless noted, so anything Issued and unpaid is Outstanding.

## StayC Group — USD, Zero Rated (0%)
| Invoice | Period | Issue date | Subtotal | VAT | Total | Status | Paid date |
|---|---|---|---|---|---|---|---|
| OS242 | 7 Jul–7 Aug 2026 | 07/07/2026 | 3,000.00 | 0.00 | USD 3,000.00 | Issued (legacy) | — |
| OS243 | 7 Aug–7 Sep 2026 | 07/08/2026 | 5,568.00 | 0.00 | USD 5,568.00 | Issued | — |
| OS244 | 7 Sep–7 Oct 2026 | 07/09/2026 | 5,568.00 | 0.00 | USD 5,568.00 | Issued | — |

## SKY Vacation Home Rental L.L.C — AED, Standard Rated 5% (DXB)
| Invoice | Period | Issue date | Subtotal | VAT | Total | Status | Paid date |
|---|---|---|---|---|---|---|---|
| OS249 | 18 Aug–17 Sep 2026 | — | 9,360.00 | 468.00 | AED 9,828.00 | Issued (original) | — |
| OS249* | 18 Aug–17 Sep 2026 | — | 7,929.00 | 396.45 | AED 8,325.45 | Draft edit (33@180 −15%, 32@90) | — |

> ⚠️ Two versions of OS249 exist — confirm which was actually sent to the client.
> Also: master sheet lists SKY per-unit at AED 300, but OS249 used 180/90 — reconcile.

## Noya Living Vacation Homes -LLC — AED, Standard Rated 5% (DXB)
Per-client sequence. Min AED 3,000/month before VAT (waived month 1). Cycle now 7th→7th.
| Invoice | Period | Issue date | Subtotal | VAT | Total | Status | Paid date |
|---|---|---|---|---|---|---|---|
| OS240 | 15 Aug–15 Sep 2026 | — | 2,100.00 | 105.00 | AED 2,205.00 | Issued (min waived) | — |
| OS241 | 15 Sep–7 Oct 2026 (22d) | 09/30/2026 | 2,200.00 | 110.00 | AED 2,310.00 | Issued (prorated min) | — |
| OS242 | 7 Oct–7 Nov 2026 | — | 3,000.00 | 150.00 | AED 3,150.00 | Draft (not issued) | — |

## One Stone (Claims Management) — USD, 30% success fee, ad hoc
| Invoice | Period | Issue date | Subtotal | Tax | Total | Status | Paid date |
|---|---|---|---|---|---|---|---|
| ONE001 | AirCover claims to date (11 claims) | 10/18/2026 | 1,836.15 | 0.00 | USD 1,836.15 | Issued | — |

> ONE001 = balance after 30%/20% correction. Total recovered $9,810.50 across 11 won
> Airbnb damage claims; agreed commission 30% = $2,943.15; $1,107.00 already paid on the
> first (20%-billed) invoice; ONE001 collects the remaining $1,836.15 as two lines
> (10% correction on the $5,535 batch = $553.50; 30% on $4,275.50 newly recovered = $1,282.65).
> PDF: invoicing/invoices/ONE001.pdf

## October 2026 — in-house invoices (VirtuPro LLC)
Status legend: Draft → Issued (generated) → Sent (to client) → Paid.
| Invoice | Client | Basis | Total | Status | Paid date |
|---|---|---|---|---|---|
| KHH001 | Kensington | Flat (up to 80 units) | AED 6,000.00 | **Sent** (2026-10-19) | — |
| RV001 | Royal Vista | 35 × 200 (tier) | AED 7,000.00 | **Sent** (2026-10-19) | — |
| BBH001 | Blue Breeze | 7 × 250 + 1,250 top-up | AED 3,000.00 | Issued | — |
| IST001 | Elite Nest (The IST Company) | 10 × 300 | AED 3,000.00 | **Sent** (2026-10-19) | — |
| UTX001 | Utopix | 9 × 300 + 300 top-up | AED 3,000.00 | Issued | — |
| NOYA001 | Noya Living | 9 × 300 + 300 top-up | AED 3,000.00 | Issued | — |
| MKB001 | MKB Living | 14 × 300 | AED 4,200.00 | Issued | — |
| ONE001 | One Stone (claims) | 30% success fee balance | USD 1,836.15 | Issued | — |

> NOYA001 + KHH001 reissued under new US entity VirtuPro LLC. Others still on old
> entity header pending reissue. Noya extra listing work pending (details tonight).

## Cash-flow snapshot (outstanding = Issued & unpaid)
Payment status not yet provided for any invoice — all Issued invoices are currently
treated as Outstanding. Update "Paid date" as payments arrive to keep this accurate.

| Currency | Outstanding (Issued, unpaid) |
|---|---|
| USD | 3,000 + 5,568 + 5,568 = **USD 14,136.00** |
| AED (SKY) | OS249 — confirm which version (9,828.00 or 8,325.45) |
| AED (Noya) | 2,205.00 + 2,310.00 = **AED 4,515.00** |
