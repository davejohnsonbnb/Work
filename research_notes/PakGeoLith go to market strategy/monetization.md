# PakGeoLith Monetization: Marketplace Business Models, Geodata Pricing Benchmarks and a Recommended Revenue Model

**Currency conventions.** I used USD 1 = PKR 278. Early-October 2026 trackers quoted 276.76 on 11 Oct 2026 and 277.9/278.3 buy/sell on 6 Oct 2026 ([30rates](https://30rates.com/usd-to-pkr-today-forecast-dollar-to-pakistani-rupee); [longforecast](https://longforecast.com/usd-to-pkr-forecast)). The 2026 range was about 276.7–281.7 ([Pound Sterling Live](https://www.poundsterlinglive.com/history/USD-PKR-2026)). I found no live November 2026 SBP rate.
- INR conversions use about INR 88 = USD 1, which comes from my own knowledge, not a source found this session. Treat INR→USD figures as approximate.
- GBP conversions use about GBP 1 = USD 1.30, also my own assumption.

PakGeoLith's current prices at PKR 278/USD:

| Item | PKR | USD |
|---|---|---|
| Subscription, standard | 5,000/yr | ~18/yr |
| Subscription, top tier | 10,000/yr | ~36/yr |
| Satellite survey report | 150k–1M | ~540–3,600 |
| Compliance report | 30k | ~108 |
| Auction listing fee | 5,000/lot | ~18/lot |

## Q1. How do B2B commodity, mineral and gemstone marketplaces make money?

### Takeaway
Discovery and lead-generation platforms (IndiaMART, Alibaba) earn mainly from supplier subscriptions, roughly USD 570–6,500 per year. They take no commission. Full-stack commodity players (Metalbook, OfBusiness) buy and resell, so their reported revenue is close to GMV and their real margin is only a few percent. Government and producer e-auctions charge small percentage fees (about 0.2–1%) or simply sell their own production (Gemfields). Commodity marketplaces in general run net take rates below 1% to a few percent. Higher takes are only defensible when the platform handles logistics, trust, finance and quality.

### Cited Findings

**Take-rate theory**
- In one investor's chart of commodity-type B2B marketplaces, most had net take rates below 1%, offset by very large reach — [Tidemark VSKP](https://www.tidemarkcap.com/vskp-chapter/marketplace-take-rates)
- Take rates depend on how managed the marketplace is and what the industry will tolerate paying a middleman. The same source cites implied take rates of about 5% and 3% for two public comparables, and a much higher rate for the heavily managed Xometry — [Tidemark VSKP](https://www.tidemarkcap.com/vskp-chapter/marketplace-take-rates)
- A sector overview puts B2B marketplace take rates at "typically 3–15% depending on category complexity and value-add services" — [Multiples.vc](https://docs.multiples.vc/coverage/b2b-marketplaces)
- I could not verify a primary a16z figure for commodity take rates. Secondary summaries say a16z argues managed marketplaces that handle logistics, trust and guarantees can justify higher takes. Several scraped pages claiming "1–3% for commodities" were low quality and are not relied on.

**IndiaMART (subscription and lead model, no commission)**
- FY26 (to 31 Mar 2026) consolidated revenue was ₹1,569 crore, up 11% YoY — [FilingReader](https://filingreader.com/news-wire/mumbai/2026-05-04/indiamart-revenue-hits-inr-1569-crore-with-total-rs-60-dividend)
- Q1 FY26: about 2.2 lakh (220,000) paying suppliers, with annualised revenue per paying supplier of about ₹64K (~USD 730), up 6% YoY — [Inc42](https://inc42.com/buzz/indiamart-q1-profit-soars-35-yoy-to-inr-154-cr); [Business Standard](https://www.business-standard.com/companies/news/indiamart-q1-results-net-profit-rises-35-to-153-54-cr-income-up-20-125071800876_1.html)
- A weaker source reports 9M FY26 ARPU of about ₹67K — [AlphaStreet](https://alphastreet.com/india/india-mart-q2-fy26-earnings-results) (page quality questionable)
- TrustSEAL verification plus catalogue combo: ₹50,000 for 1 year, ₹80,000 for 2 years, ₹100,000 for 3 years, excluding tax (~USD 570/yr) — [IndiaMART help](https://help.indiamart.com/?p=4684); [IndiaMART corporate](https://corporate.indiamart.com/mdc-ts-combo/)
- One proforma invoice of unclear date gives a different 3-year TrustSEAL price of ₹80,000 — [Scribd](https://www.scribd.com/document/815177907/PI)

**Alibaba.com (supplier membership)**
- Gold Supplier membership estimates vary by source: about USD 4,700/yr (UK) and USD 3,500–6,500/yr depending on supplier location. Alibaba's NZ promotion cites a USD 3,999 example — [JingSourcing](https://jingsourcing.com/b-alibaba-gold-supplier/); [WorldFirst NZ](https://www.worldfirst.com/nz/?p=23938)
- Verified Supplier tier: about USD 12,500/yr — [CosmoSourcing](https://www.cosmosourcing.com/blog/what-are-alibaba-verified-suppliers)
- Alibaba raised membership fees from 1 Jan 2024 — [Alibaba seller blog](https://seller.alibaba.com/businessblogs/price-adjustment-notice-of-gold-supplier-membership-px0029a5p)
- In PKR terms, a Gold Supplier pays roughly PKR 1.0–1.8M/yr. That is 200–360 times PakGeoLith's PKR 5,000 tier.

**Metalbook (full-stack metals: procurement, logistics, financing)**
- FY25 revenue from operations was ₹1,327 crore, up from ₹796 crore in FY24. Ferrous commodities were 71% of revenue — [Entrackr](https://entrackr.com/fintrackr/metalbooks-gross-revenue-crosses-rs-1300-cr-in-fy25-10618334)
- Metal procurement cost was 95.6% of total costs, and the expense-to-revenue ratio was 1.03x, meaning a loss on a GMV-like top line — [Entrackr](https://entrackr.com/fintrackr/metalbooks-gross-revenue-crosses-rs-1300-cr-in-fy25-10618334)
- Entrackr treats Metalbook's top line as gross revenue, essentially GMV — [Entrackr FY24](https://entrackr.com/fintrackr/metalbook-nears-rs-800-cr-gross-revenue-in-fy24-8688576)

**Government and state e-auctions**
- MSTC (India) earns a service charge on transaction value for e-auctions — [MSTC](https://mstcecommerce.com/eAuction_desc.jsp)
- In the 2014 Goa iron-ore e-auctions, the winning bidder paid a 0.2% service charge plus service tax to MSTC — [Goa DMG](https://dmg.goa.gov.in/PDFs/E-Auction/Clarification%20Regarding%20Base%20Price%20And%20Details%20Concerning%20The%20E-Auction%20On%2017-Feb-2014.pdf) (old, state-specific)
- Coal spot e-auctions require an EMD of about ₹500/tonne — [MSTC CCL notice](https://www.mstcindia.co.in/MSTC_Static_Pages/Coal/CCL_notice.pdf)
- Tanzania mineral trading centres originally charged a 6% royalty plus a 1% inspection and clearance fee on gold, gems and tin — [The Citizen](https://www.thecitizen.co.tz/tanzania/news/national/trading-centres-boost-tanzania-s-mining-sector-2693818)
- An October 2024 amendment cut the gold royalty to 4% and the inspection fee to 0% — [FB Attorneys](https://fbattorneys.co.tz/bot-issues-notice-on-gold-purchase-program-in-tanzania/). I could not confirm the current rates.

**Gemfields (producer-run tender auctions)**
- Gemfields sells its own production at auction, so there is no commission. 2025 auction revenue was USD 128.5M, down about 34% from USD 196M — [Engineering News](https://www.engineeringnews.co.za/print-version/gemfields-full-year-auction-revenues-reach-1285m-2026-01-30); [finanzen.at/Mining.com](https://www.finanzen.at/nachrichten/aktien/gemfields-auction-revenue-falls-34percent-15450679)
- The December 2025 commercial-quality emerald auction made USD 25.4M, selling 45 of 46 lots at about USD 7.46/ct — [Mining Weekly](https://www.miningweekly.com/article/gemfields-reports-254m-result-at-year-end-commercial-emerald-auction-2025-12-05)
- The June 2025 ruby auction made USD 31.7M — [HL](https://www.hl.co.uk/shares/stock-market-news/aim-and-small-cap-news/aim-bulletin/gemfields-generates-$31.7m-revenue-from-latest-auction)
- Average lot value in December 2025 was about USD 550K, or PKR ~153M. A flat PKR 5,000 (USD 18) listing fee on lots of that size is negligible compared with a percentage fee.

**Inspection and assay (SGS, Bureau Veritas)**
- India's IBM publishes a government schedule of charges for mineral testing and analysis — [IBM schedule 2025](https://ibm.gov.in/writereaddata/files/17528215946879ef5ac0bb0Rev_Schedule_of_Charges_TMP_180725.pdf). I did not extract specific line items.
- I found no SGS or Bureau Veritas price list.

### Inferences
- PakGeoLith's planned marketplace sits between IndiaMART-style discovery and MSTC-style auctions. The realistic stack is:
  1. A verified-seller annual subscription, in the IndiaMART TrustSEAL band of ~USD 500/yr (PKR ~140k), discounted for Pakistan's market.
  2. A success fee of about 0.5–2% on escrowed or auction transactions, set above MSTC's 0.2% only where PakGeoLith adds assay, escrow or logistics.
  3. Pass-through margins on inspection and assay, logistics and trade finance.
- The current PKR 5,000 flat per-lot auction fee should become a minimum fee plus a percentage of hammer price. For example: PKR 5,000 minimum, or 1% of sale value, whichever is greater.
- Do not copy Metalbook's buy-and-resell model early. It inflates revenue but carries inventory and credit risk, at an expense ratio above 1x.

### Gaps
- I found no public take rate for Metalbook, OfBusiness, Material Depot, Metal.com, ScrapMonster or BlueSky, and no data on Gemfair, Bharat gemstone portals or the Zambia trading centres.
- I found no current MSTC service-charge schedule (only a 2014 figure) and no MMTC data.
- I found no SGS or Bureau Veritas assay price list. These normally come only as quotes.
- I found no a16z primary source on commodity take rates.

## Q2. Why do mineral marketplaces fail, and how do winners solve it?

### Takeaway
Most of the evidence is general, not mineral-specific, but it is consistent. Buyers and sellers bypass the platform once trust exists ("disintermediation"), and quality and grade disputes kill repeat trade. Winners stay in the transaction by bundling services that are hard to replicate off-platform: escrow tied to independent assay, inspection, logistics, financing and standardised grading.

### Cited Findings
- **Trust can backfire.** A randomized field experiment on an online freelance marketplace (Gu & Zhu, *Management Science*) found that higher trust improved matching with high-quality sellers. Past a threshold, it also increased off-platform transactions that offset the revenue gains — [SUFE summary](https://academicnewsletter.sufe.edu.cn/info/390411)
- **Escrow alone is weaker than expected.** Research on B2B e-marketplaces finds institutional trust mechanisms (escrow, insurance, third-party seals) less effective than other trust-building measures studied — [CAIS](https://aisel.aisnet.org/cais/vol18/iss1/6)
- **What keeps users on-platform.** Industry guidance says sellers bear dispute risk and buyers must judge legitimacy alone once they leave; payment terms and credit (embedded finance) keep them on — [Hokodo](https://www.hokodo.co/resources/how-to-prevent-disintermediation-on-your-b2b-marketplace)
- Logistics, quality assurance, insurance and financing are named as the services that retain users — [TechFinitive](https://www.techfinitive.com/features/how-b2b-marketplaces-can-build-trust-reputation-and-credibility/)
- **Escrow mechanics.** Escrow holds funds until both parties meet obligations — [Razorpay](https://razorpay.com/blog/business-banking/the-future-of-marketplace-embracing-escrow-to-enhance-marketplace-security/)
- **Assay in practice (practitioner source).** Mineral-trade practitioners stress assay certificates, independent lab checks and complete shipping documentation to prevent disputes — [LinkedIn practitioner post](https://gh.linkedin.com/in/john-wolsey-583b1561)
- **Government-run centres.** Tanzania's mineral trading centres were created to fight smuggling and tax evasion by centralising inspection, weighing and royalty collection — [Mining Technology](https://www.mining-technology.com/features/inside-tanzanias-mineral-trading-hubs/); [The EastAfrican](https://www.theeastafrican.co.ke/business/Tanzania-in-plan-to-establish-more-mineral-trading-hubs/2560-5056560-e1e34o/index.html). This is evidence that trusted physical inspection is the anchor of the model.
- **Gemfields' standardised-lot model.** Producer-graded lots in tender auctions sell at high rates (45 of 46 lots in December 2025) — [Mining Weekly](https://www.miningweekly.com/article/gemfields-reports-254m-result-at-year-end-commercial-emerald-auction-2025-12-05). The 2025 ruby results were hurt by illegal mining and grade volatility — [Rapaport](https://rapaport.com/?p=120256)
- **Full-stack approach.** Metalbook positions itself as a "full-stack" marketplace bundling procurement, logistics and financing — [Entrackr](https://entrackr.com/fintrackr/metalbooks-gross-revenue-crosses-rs-1300-cr-in-fy25-10618334); [CXOToday](https://cxotoday.com/media-coverage/metalbook-launches-new-verticals-improving-technological-infrastructure-and-expanding-global-network-of-processing-centers-post-its-15m-series-a-fund-raise/)

### Inferences
- PakGeoLith's real advantage is licence verification (only licensed sellers), its own geodata and compliance reports, and assay coordination. Those should be the paid trust layer.
- Charge the success fee only when PakGeoLith-controlled escrow and assay is used. That gives both sides a reason to stay on-platform.
- Standardised grading per mineral (chromite Cr2O3 %, gemstone lot grading, marble block dimensions and grades) plus sealed-sample chain of custody is the obvious defence against disputes.

### Gaps
- I found no peer-reviewed study of mineral marketplace failures specifically, and no data on how assay-linked escrow changes off-platform leakage.
- I found no failure case studies for named startups such as Open Mineral; only its WEF Technology Pioneer selection appeared — [Startupticker](https://www.startupticker.ch/en/news/open-mineral-selected-among-world-economic-forum-s-technology-pioneers)

## Q3. Pricing benchmarks for geodata subscriptions, exploration and remote-sensing reports, and consultancy day rates

### Takeaway
Professional mining intelligence is priced at USD 1,000 to USD 30,000+ per user per year. PakGeoLith's USD 18–36/yr sits at hobbyist or newsletter levels: below even retail mining-stock newsletters (USD 199–399/yr). Satellite survey reports at USD 540–3,600 sit at or below one to two senior consultant days in the West, which looks underpriced for foreign clients but reasonable for small local leaseholders.

### Cited Findings

**Terminals and data platforms**
- S&P Capital IQ Pro is not publicly priced. Third-party estimates put it at about USD 12K–30K per user per year, with contracts reported from USD 10K to 50K+ depending on modules. Implementation adds a one-off USD 15K–50K — [CostBench](https://costbench.com/software/financial-data-terminals/sp-capital-iq/); [CostBench hidden costs](https://costbench.com/software/financial-data-terminals/sp-capital-iq/hidden-costs/)
- Fastmarkets prices are quote-only, via the sales team and demo request. Its offering is described as 1,500+ metals prices, with archive access depending on tier — [Fastmarkets](https://www.fastmarkets.com/insights/metal-bulletin-prices-are-coming-to-the-fastmarkets-platform/)

**Mining trade press (Aspermont)**

| Title | Standard | Premium | Users | Source |
|---|---|---|---|---|
| Mining Magazine | £735/yr (~USD 955, PKR ~265k) | £2,395/yr | up to 3 | [Mining Magazine](https://miningmagazine.com/subscribe) |
| Mining Monthly | $2,285/yr (AUD presumed) | $6,080/yr | up to 5 | [Mining Monthly](https://miningmonthly.com/subscribe) |
| Mining News | $2,360/yr | $6,155/yr | up to 5 | [MiningNews](https://miningnews.net/subscribe) |

**Retail and investor tier**
- Gold Stock Data offered Standard USD 199–299/yr and Premium USD 299–399/yr, depending on the year — [Gold Stock Data](https://www.goldstockdata.com/interviews/239-Interview-on-Mining-Stock-Daily.html)
- The Northern Miner Executive Edition includes a Mining Intelligence database of 2,500+ company profiles. I did not find its price — [Northern Miner](https://www.northernminer.com/subscribe-/)

**Consultancy day rates**
- UK geological consulting: £400–1,200/day for experienced professionals — [Palsatech](https://palsatech.fi/?p=5833)
- US public-sector billing schedule: Geologist I at USD 85–105/hr, Geologist VIII at USD 240–320/hr (about USD 680–2,560/day) — [Everett WA contract](https://lfportal.everettwa.gov/WebLink/0/doc/1911933/Page16.aspx)
- Kolabtree freelance geologists: roughly USD 13–150/hr — [Kolabtree](https://kolabtree.com/find-an-expert/subject/geological-engineering)
- Tanzania's Geological Survey charges TZS 350,000/day for a geoscientist working for large-scale miners, with lower rates for small-scale miners — [GST Tanzania](https://www.gst.go.tz/pages/consultancy-services)
- India's IBM publishes a government schedule of charges for testing and mineral services — [IBM](https://ibm.gov.in/writereaddata/files/17528215946879ef5ac0bb0Rev_Schedule_of_Charges_TMP_180725.pdf)

**Remote sensing**
- Free Landsat archives make regional screening the cheapest exploration step. Commercial imagery is bought per km² for narrowed targets — [Farmonaut](https://farmonaut.com/?p=171882) (vendor source)
- ASTER is widely used because of its relatively low cost and broad coverage — [NV5 Geospatial](https://www.nv5geospatialsoftware.com/Support/Maintenance-Detail/5040)

### Inferences
- A PakGeoLith satellite report at PKR 150k–1M (USD 540–3,600) costs about the same as 1–3 UK consultant days (£400–1,200/day). Since raw imagery is often free, the value is in interpretation plus local ground-truth. Foreign investors can bear USD-priced reports at USD 2,500–15,000 depending on area and deliverables, though this is my inference, not a sourced benchmark. Local small leaseholders likely cannot.
- The PKR 30k (USD 108) compliance report is cheap compared with any consultant day rate globally. A local-tier and a foreign or enterprise-tier price both look justified.

### Gaps
- I found no public prices for Mining Data Online, Mindat (a free, donation-based database to my knowledge, unverified here), MinEx Consulting, GlobalData mining or Wood Mackenzie. All appear to be quote-only.
- I found no per-km² price for remote-sensing alteration mapping and no South Asian or Pakistani exploration-report prices.
- I found no Pakistan geologist day-rate survey.

## Q4. Is PKR 5,000/yr underpriced? Recommended tiered pricing and Pakistan payment, escrow and tax considerations

### Takeaway
PKR 5,000/yr (USD 18) is probably fine as a local entry tier for students and small leaseholders. It is far below any professional benchmark: IndiaMART's average paying supplier is about USD 730/yr, Alibaba Gold about USD 3,500–6,500/yr, and Aspermont trade press about USD 950–6,000/yr. PakGeoLith should keep a cheap local tier, add PKR professional and business tiers, add USD tiers for foreign investors, and sell enterprise, API and government licences separately.

On payments and tax: escrow in Pakistan is still informal, with no dedicated escrow law. Raast suits low-cost settlement, and its merchant-fee subsidy ran to June 2026. Commission income attracts a 12% adjustable Section 233 withholding for filers in most categories, plus provincial sales tax on services.

### Cited Findings
- IndiaMART ARPU is about ₹64K/yr (~USD 730, PKR ~200k) across 220K paying suppliers — [Inc42](https://inc42.com/buzz/indiamart-q1-profit-soars-35-yoy-to-inr-154-cr)
- IndiaMART's entry verification bundle costs ₹50K/yr (~USD 570, PKR ~158k) — [IndiaMART help](https://help.indiamart.com/?p=4684)
- Professional mining data runs from about USD 955/yr (Mining Magazine, 3 users) to USD 12–30K per user per year (Capital IQ Pro) — [Mining Magazine](https://miningmagazine.com/subscribe); [CostBench](https://costbench.com/software/financial-data-terminals/sp-capital-iq/)

**Pakistan: escrow and payment rails**
- An IBA report describes escrow use in Pakistan as "limited and informal" and recommends an Escrow Services Act and digital escrow solutions — [IBA](https://ir.iba.edu.pk/sbselp/80) (student-level report)
- No SBP escrow framework was found. The SBP runs a regulatory sandbox, with six applicants shortlisted in January 2026 — [The Standard](https://thestandard.com.pk/sbp-shortlists-six-companies-to-test-digital-financial-solutions/)
- SBP licensing activity includes a full PSP licence for Safepay and in-principle PSO/PSP approval for B2B payments player Haball — [Profit](https://profit.pakistantoday.com.pk/?p=193897); [Digital Pakistan](https://digitalpakistan.pk/haball-secures-in-principle-pso-psp-approval-to-revolutionize-b2b-payments)
- **Raast fees and subsidy.** Raast P2M carries no fee for consumers. Providers may charge merchants a "reasonable" fee, but the SBP encouraged waivers early on — [ProPakistani](https://propakistani.pk/2023/12/06/sbp-rolls-out-much-awaited-raast-p2m-service/); [Tribune](https://tribune.com.pk/story/2630109/digital-payments-target-merchant-growth?amp=1)
- The government allocated a PKR 3.5bn subsidy paying financial institutions 0.5% per eligible P2M QR transaction, September 2025 to June 2026 — [SBP PSPOD Circular 3/2025](https://www.sbp.org.pk/psd/2025/C3.htm); [Business Recorder](https://www.brecorder.com/news/amp/40384460)
- More than 2.6M merchants were on Raast P2M by March 2026, and NBP got approval for P2M acquiring in May 2026 — [Tribune](https://tribune.com.pk/story/2630109/digital-payments-target-merchant-growth?amp=1); [The News](https://www.thenews.pk/print/1414978-nbp-gets-approval-to-launch-raast-merchant-payment-service)

**Pakistan: tax on commission income**
- Section 233 withholding on brokerage and commission for 2025-26: 12% for filers and 24% for non-filers in the general "other persons" category. Advertising agents pay 10%/20% and small life-insurance agents 8%/16%. The tax is adjustable, not final — [PKRevenue](https://pkrevenue.com/advance-tax-rates-on-brokerage-commission-for-2025-26/)
- Reportedly unchanged for Tax Year 2027 under Finance Act 2026 — [PKRevenue](https://pkrevenue.com/brokerage-and-commission-tax-rates-in-pakistan-for-ty-2027/)
- IT and IT-enabled services keep a 4% withholding rate for FY2025-26 — [Profit](https://profit.pakistantoday.com.pk/?p=208309). This could matter if subscriptions and data are classed as IT-enabled services rather than commission.

### Inferences: recommended revenue model and prices
All PKR/USD figures below are my proposals, built from the benchmarks above at PKR 278/USD. They are not sourced prices.

**Subscriptions (data and intelligence)**

| Tier | PKR | USD |
|---|---|---|
| Free | 0 | 0 |
| Explorer (local, students and small leaseholders) | 5,000/yr | ~18 |
| Professional (single user, full maps and alerts, PKR) | 25,000–40,000/yr | ~90–145 |
| Business (≤5 seats, exports, verified-seller badge) | 120,000–180,000/yr | ~430–650, IndiaMART TrustSEAL band |
| International Investor (USD-priced) | — | USD 1,200–2,500/yr per seat, below Aspermont premium |
| Enterprise / API | — | USD 10K–40K/yr, custom, below Capital IQ per-seat levels |

**Government data licensing and white-label**
- Annual licence to provincial mines departments or PMDC-type bodies: PKR 5–25M/yr (USD 18K–90K), structured as a SaaS plus data-update contract. This is a proposal; there is no benchmark.
- White-label of portals or auction engines on the same terms, plus a share of any per-transaction fee.

**Reports**
- Keep PKR 150k–1M satellite reports for local clients. Add a USD price list for foreign investors (proposed USD 3K–15K by area and deliverables).
- Raise the compliance report to PKR 30k local and USD 300–500 foreign, compared with consultant day rates of £400–1,200 in the UK.

**Marketplace**
- Verified licensed-seller membership, as Business tier above.
- Success fee of 1–2% on escrow-settled deals (0.5% for bulk minerals like chromite and coal), compared with MSTC's 0.2% service charge and the <1% to 3–5% B2B benchmarks.
- Replace the flat PKR 5,000/lot auction fee with "greater of PKR 5,000 or 1–2.5% of hammer price" for gemstone lots. A flat USD 18 fee on high-value lots leaves revenue on the table.
- Ancillary: assay and inspection coordination at cost plus 10–20%, logistics referral, and trade-finance referral fees. These follow the Metalbook and Hokodo playbook, but PakGeoLith should not take inventory.

**Payments**
- Run escrow through a scheduled bank's escrow or trustee account, or partner with a licensed PSP or EMI such as Safepay, rather than holding funds itself. No escrow-specific law exists, and holding client funds likely needs SBP authorisation (inference).
- Use Raast for settlement legs.
- Budget for 12% s.233 withholding on commission receipts (as filer) and provincial services sales tax, which needs verification for each province.

### Gaps
- I did not verify provincial sales tax on services rates (Punjab, KP, Sindh, Balochistan) for commission or online marketplace services. Rates of 15–16% were not confirmed this session.
- I found no SBP rule on whether a marketplace holding buyer funds needs an EMI or PSP licence, and no named Pakistani escrow product.
- Raast merchant fees after June 2026 are unknown.
- I found no Pakistani willingness-to-pay data for geodata subscriptions.
- The INR/USD and GBP/USD rates used are assumptions, not sourced.
