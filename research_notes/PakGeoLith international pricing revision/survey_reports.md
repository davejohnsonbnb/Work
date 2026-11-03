# International pricing benchmarks for satellite remote-sensing mineral exploration surveys and reports (PakGeoLith tier re-pricing)

Research date: 2026-11-03. Conversion used: PKR 278/USD (the assignment's figure; no newer rate was checked). Search budget was limited to about 15 tool calls. Several vendor pages (Upwork, Fiverr, LandInfo) returned HTTP 403 to the fetcher, so some figures come from search-engine extracts and are marked as such. **Overall, published vendor prices for finished mineral-exploration *reports* are very rare. Almost every analytics vendor (Farmonaut, VRIFY, Fleet Space, Pixxel Aurora) quotes per project. Published per-km² prices exist mostly for raw imagery.**

## 1. Published or reported prices from remote-sensing and GeoAI vendors (per project, per km², per deliverable)

### Takeaway
Finished-report vendors do not publish prices. Farmonaut, VRIFY DORA and Fleet Space ExoSphere are all quote-only, per project. The only hard per-km² numbers found are for raw imagery: WorldView-3 SWIR at about USD 25.50–34/km² (50 km² minimum), hyperspectral tasking at about USD 6–9/km² (Tanager, via a reseller) and USD 8/km² (Pixxel VNIR), and archive VHR optical at USD 8–26/km². No reliable price was found for GoldSpot, Minerva, Earth AI, Earth Genome, Photosat, SpecTIR/HyVista, Terra Remote Sensing, Fugro or the major consultancies (SRK, CSA Global, WSP, Snowden).

### Cited Findings
- **Farmonaut (mineral detection):** no per-km² price is published. Pricing is "project-based and customized" by total area, target minerals and report tier (Premium or Premium+). A quote (scope, price, timeline) comes back within one working day of submitting a boundary. — [Farmonaut FAQ](https://farmonaut.com/faqs); [Farmonaut Contact](https://farmonaut.com/contact/); [Farmonaut Mining Pro](https://farmonaut.com/?p=215433)
- Farmonaut's mining blog cites a GeoPera 2026 guide: 50 cm archive VHR imagery USD 8–18/km², 30 cm archive USD 17–26/km². It says hyperspectral tasking is "typically quoted per project, not per square kilometer". — [Farmonaut hyperspectral mineral mapping page](https://farmonaut.com/mining/hyperspectral-satellite-mineral-mapping-gold-rare-earths-aster) (secondary; GeoPera original not checked)
- **WorldView-3 SWIR (Maxar/Vantor, via reseller LandInfo, Jan 2026 sheet):** 3.7 m 8-band SWIR at USD 25.50/km² and USD 34.00/km², most likely archive and new collection respectively (the table layout was garbled in the extract). Minimum 50 km² contiguous for both. The July 2023 LandInfo list had USD 24 (archive, 25 km² minimum) and USD 34 (new collection, 100 km² minimum, 5 km minimum width). A 7.5 m SWIR archive product was USD 12/km². A 15° off-nadir constraint adds USD 2/km². — [LandInfo price sheet Jan 2026 (PDF)](https://landinfo.com/wp-content/uploads/Imagery_LandInfo_202601-1.pdf); [LandInfo satellite imagery pricing](https://landinfo.com/satellite-imagery-pricing/) (page 403 on direct fetch; figures from search extract)
- A Satellite Imaging Corp SWIR datasheet (May 2026) says SWIR is ordered by scene, from one scene up to 10,000 km² per order. This conflicts with the LandInfo per-km² minimums. — [SIC SWIR datasheet](https://satimagingcorp.com/wp-content/uploads/2026/05/ShortwaveInfrared-DS-SWIR.pdf)
- **Pixxel (hyperspectral tasking, official docs):** priced per km² by spectral band; VNIR is USD 8/km². Cloud cover of 10% or less carries a 15% uplift, and 20% carries none. No public price for the Aurora platform or analytics subscriptions. — [Pixxel docs – tasking pricing](https://docs.pixxel.space/documentation/getting_started/pricingandrefunds/imagery_pricing/tasking)
- **Planet Tanager (30 m hyperspectral):** reseller SkyWatch (June 2026 catalogue) lists "indicative" rates of USD 6.00 and 9.00/km² with a 100 km² figure, which is probably the minimum. The column labels were unclear. Planet's own page is contact-sales only. — [SkyWatch – Planet provider page](https://skywatch.com/geospatial-data-providers/planet/); [Planet hyperspectral](https://www.planet.com/products/hyperspectral)
- **Fleet Space ExoSphere:** no per-survey price is published. Trade press reports more than 150 ExoSphere surveys completed on five continents, and an A$150M Series D (Dec 2024; USD 100M at a USD 525M valuation). — [Mining.com](https://www.mining.com/fleet-space-technologies-launches-new-exosphere-features-for-global-mineral-exploration/); [OTPP release](https://otpp.com/en-ca/about-us/news-and-insights/2024/fleet-space-closes-usd-100m-series-d-with-usd-525m-valuation/); [InDaily](https://www.indailysa.com.au/news/business/2024/12/12/fleet-space-valuation-in-orbit-after-150-million-capital-raise)
- **VRIFY DORA (GeoAI prospectivity):** closed SaaS. A pricing page exists (vrify.com/pricing) but the search surfaced no figures. 26 early-adopter clients were reported at the USD 12.5M Series B (Feb 2025). Client announcements (e.g. Toogood Gold, Nevada Sunrise) give scope but no fees. — [Newswire Series B](https://www.newswire.ca/news-releases/vrify-lands-12-5m-series-b-to-advance-dora-the-world-s-first-ai-assisted-mineral-discovery-platform-828597303.html); [apis.io VRIFY](https://apis.io/providers/vrify/); [Toogood Gold release](https://www.newsfilecorp.com/release/265470)
- **Freelance (Upwork/Fiverr):** active listings exist for ASTER, Sentinel, Landsat, EMIT, PRISMA and AVIRIS alteration and mineral mapping (argillic, phyllic, propylitic, iron-oxide). Package prices could not be read: the pages returned 403 and search extracts showed none. — [Upwork service listing](https://www.upwork.com/services/product/development-it-satellite-remote-sensing-for-mineral-exploration-and-mining-targets-2068781736228471485); [Fiverr mapcraft_](https://fiverr.com/mapcraft_/do-remote-sensing-for-mineral-exploration-and-mining); [Fiverr bashar_moh1](https://www.fiverr.com/bashar_moh1/mineral-exploration-and-gold-detection-using-remote-sensing)

### Inferences
- For the sample T4 (~30 km², all free sensors: Sentinel-2, Landsat, ASTER, EMIT, Sentinel-1), data cost is zero. If PakGeoLith added WorldView-3 SWIR, the 50 km² minimum means at least about USD 1,275 (archive) to USD 1,700 (new tasking) per contiguous AOI, even for a 10 km² block. That is roughly PKR 355k–473k, more than the old T2 price on its own. Commercial SWIR should therefore be an add-on priced at cost plus margin, not bundled.
- Hyperspectral tasking (Tanager or Pixxel at about USD 6–9/km², about 100 km² minimum) implies a data floor of about USD 600–900 (PKR 167k–250k) per tasked AOI.
- Because competitors hide report prices, PakGeoLith's published USD tiers would be unusually transparent. That is a marketing advantage, but there are few direct benchmarks to anchor against.

### Gaps
- No published or reported prices found for: Pixxel Aurora analytics, Photosat, Exploration Remote Sensing / ASTER consultancies, Earth Genome, SpecTIR/HyVista airborne hyperspectral, GoldSpot, Minerva, Earth AI, Terra Remote Sensing, Fugro, SRK/CSA/WSP/Snowden remote-sensing studies. These were not reached within the search budget, or the searches returned nothing.
- No ASX/TSXV disclosure of a specific satellite-study or ExoSphere cost was found. Junior announcements on ASX (search "ExoSphere" plus "cost" in quarterly cash-flow reports) are a likely next source.
- Upwork/Fiverr package prices need manual browser checks.

## 2. Costs of follow-on alternatives (ground and airborne geophysics, geochem, NI 43-101, field days, junior budgets)

### Takeaway
Airborne and ground follow-up is far more expensive than satellite screening. Helicopter magnetics in North America runs about USD 35 to over 100 per line-km. A 50 km² tenement costs about AUD 150–250k by helicopter versus AUD 60–100k by drone (one blog estimate). Modelled UAV magnetics costs only about USD 1–10 per line-km. No sourced figures were found for NI 43-101 report fees, modern exploration soil assays or junior budgets.

### Cited Findings
- Helicopter-borne aeromagnetic surveys in North America "currently range between $35/line-km to over $100/line-km" (2022 peer-reviewed paper). — [Springer, Pure Appl. Geophys. 2022](https://springerlink.bibliotecabuap.elogim.com/content/pdf/10.1007/s00024-022-03025-9.pdf)
- Modelled UAV magnetics: about USD 1.38/line-km (USD 500/day operating cost spread over 16 flights × 22.5 km). Comparison crewed systems are modelled at about USD 5 and USD 10/line-km. These are model outputs, not market quotes. — [arXiv 2402.11797](https://ar5iv.labs.arxiv.org/html/2402.11797); [UCL IROS 2025](https://discovery.ucl.ac.uk/10218083/1/Saeedi_IROS_2025.pdf)
- March 2026 blog: a 50 km² tenement costs AUD 150,000–250,000 by helicopter magnetics versus AUD 60,000–100,000 by drone magnetics (unverified). — [MinerMundo blog](https://minermundo.pages.dev/blog/2026-03-08-geophysical-survey-drones-mineral-exploration)
- A drone-mag vendor claims drone surveys cost "less than half" of ground-based surveys and are replacing ground and airborne surveys under 2,000 line-km. — [Daniel Card drone mag](https://daniel-card.squarespace.com/drone-mag)
- The Geological Survey of Tanzania sells existing magnetic data at TZS 200,000 (or USD 100) per line-km. This is a data-sale price, not an acquisition cost. — [GST Geophysical Digital Data Charges 2025](https://www.gst.go.tz/uploads/documents/sw-1747303080-Geophysical%20Digital%20Data%20Charges.pdf)
- Soil and geochem: no current commercial exploration multi-element assay price was found. A 1982 BC assessment report shows about CAD 7.70/sample for Cu-Pb-Zn-Ba plus preparation, which is too old to use. — [BC ARIS 11123b](https://apps.nrs.gov.bc.ca/pub/aris/Report/11123b.pdf/)
- **India (IBM, 1 Apr 2025 schedule):** "Geological Mapping on 1:1000/1:2000 scale" costs INR 66,150 (INR 78,057 with 18% GST). The unit is not stated in the extract; it is presumably per assignment or block, with personnel man-days extra. "Preliminary Geological appraisal" report charge, first 3 copies: INR 26,460 (31,223 with GST). Due diligence of a mineral property: 5% of total cost. — [Indian Bureau of Mines Schedule of Charges TMP 18-07-2025](https://ibm.gov.in/writereaddata/files/17528215946879ef5ac0bb0Rev_Schedule_of_Charges_TMP_180725.pdf)
- S&P Global data shows exploration activity fell in Australia, Canada and the US as junior spending weakened (as of 2025). — [Mining.com – skills shortage](https://www.mining.com/blog/skills-shortage-tightens-grip-on-junior-explorers)

### Inferences
- The sample T4 (~30 km²) would cost roughly AUD 36–60k (drone) to AUD 90–150k (helicopter) as a magnetics survey, scaled linearly from the 50 km² blog figure. That is about USD 24k–100k, against the old T4 price of PKR 950k (~USD 3,400). Satellite targeting at even USD 5–10k remains a small fraction of the first ground or airborne follow-up. This value-framing argument supports raising prices.

### Gaps
- NI 43-101 / JORC technical report fees: none found in this search. Industry knowledge suggests tens of thousands of USD for a property-level report, but this is unsourced and should be verified.
- Ground magnetics per line-km, soil sample all-in cost (collection plus assay), field reconnaissance day rates, and median junior exploration budgets were not found with sources.

## 3. Geologist and consultant day rates (global and Pakistan/South Asia)

### Takeaway
Globally, even junior contract geologists now charge about USD/AUD 500–600 per day (anecdotal). In Pakistan, salaried geologists typically earn about PKR 40k–135k per month, roughly USD 145–485 per month or about USD 7–22 per working day. Indian government consultancy (IBM) bills a senior (Group A) officer at INR 8,710 per day (about USD 100). Local labour cost is a tiny share of an international benchmark, so price should follow value and the client's alternatives, not cost-plus.

### Cited Findings
- Recruiter quote (mining.com): "Even the younger guys coming in are charging $500 to $600 a day… That was a senior geologist four years ago." The currency and country are not specified (likely North America or Australia). — [Mining.com – skills shortage](https://www.mining.com/blog/skills-shortage-tightens-grip-on-junior-explorers)
- Survey: 39% of geologists were seeking pay rises of 25% or more. — [Mining.com remuneration survey](https://mining.com/global-mining-professionals-anticipate-surge-in-salaries-98747)
- **India IBM (1 Apr 2025):** consultancy personnel basic rate per day is INR 8,710 for Group A (INR 10,278 with GST), INR 6,725 for Group B (7,936), and INR 4,520 for Group C (5,334). — [IBM Schedule of Charges 2025](https://ibm.gov.in/writereaddata/files/17528215946879ef5ac0bb0Rev_Schedule_of_Charges_TMP_180725.pdf)
- **Pakistan salaries:** Payscale gives an average of PKR 650,000/yr (2026), range about PKR 98k to 1M per year. — [Payscale PK Geologist](https://www.payscale.com/research/PK/Job=Geologist/Salary). Paylab: 80% earn PKR 40,593–135,187 gross per month. — [Paylab PK Geologist](https://paylab.com/pk/salaryinfo/construction-real-estate/geologist). WageIndicator 2025: PKR 80,218–421,718 per month across the field. — [WageIndicator PK](https://acc.wageindicator.org/en-pk/work-in-pakistan/jobs-and-pay/geologists-and-geophysicists). Job ad (Dewan Cement, 2+ years' experience): PKR 50–80k per month. — [CareerOkay](https://www.careerokay.com/Job/job-listings-geogolist--104650)
- **Pakistan procurement:** GSP Lahore tender (closing 21 Feb 2026) for ArcGIS, ENVI and a geodata portal/mobile app, with ENVI and app lots listed at Rs 200,000 each. A 2024 GSP pre-qualification for remote-sensing-based 1:50,000 accelerated geological mapping listed only a PKR 1,000 document fee; no award value was found. — [PPRA EPMS TS0000000643E](https://epms.ppra.gov.pk/public/tenders/tender-details/TS0000000643E); [GSP letter 28-01-2026](https://gsp.gov.pk/wp-content/uploads/2026/02/Letter-to-PID-for-Web-Portal-Tender-28-01-2026-for-published.pdf); [GSP Notice 1-1-24](https://gsp.gov.pk/wp-content/uploads/2024/01/Notice-1-1-24.pdf)
- A UK–Pakistan partnership and a Feb 2026 consultancy RFP for GSP training and capacity building (digital mapping and GIS) exist, but no contract values were found. — [GOV.UK](https://www.gov.uk/government/news/new-uk-pakistan-partnership-will-bolster-pakistans-geological-survey); [Qureos listing](https://app.qureos.com/jobs/training-and-capacity-building-at-the-geological-survey-of-pakistan-gsp-in-support-of-pakistans-developing-mineral-sector-1771970974091)

### Inferences
- The old T2 (PKR 375k over 10 days, i.e. PKR 37.5k or about USD 135 per day) already sits above the South Asian public-sector senior rate (about USD 100/day IBM) but far below international contract rates (about USD 500–600/day). A USD tier priced at about USD 300–600 per analyst-day would place PakGeoLith between local and Western benchmarks. This is an inference, not a sourced market rate.
- The 2026 PKR/USD rate was not re-verified; 278 is the assumption.

### Gaps
- No Pakistan Engineering Council consultancy fee schedule, GSP fee schedule, or Pakistani university consultancy rate card was found.
- No sourced AusIMM or AIG 2025–26 consultant day-rate survey was found; the AusIMM survey surfaced dates from 2004.
- No World Bank contract award for remote-sensing mineral mapping in Pakistan or South Asia was found within the budget.

## 4. Satellite data costs if PakGeoLith adds commercial imagery

### Takeaway
Commercial data minimums set a floor of about USD 600–1,700 per AOI before any analysis. WV-3 SWIR costs USD 25.50–34/km² with a 50 km² minimum. Hyperspectral (Tanager/Pixxel) costs USD 6–9/km² with about a 100 km² minimum. VHR archive optical costs USD 8–26/km².

### Cited Findings
- WV-3 SWIR 3.7 m: USD 25.50 (archive) and 34 (tasking) per km², 50 km² minimum (Jan 2026). 7.5 m SWIR archive: USD 12/km² (2023 list). — [LandInfo Jan 2026 PDF](https://landinfo.com/wp-content/uploads/Imagery_LandInfo_202601-1.pdf)
- Apollo Mapping announced reduced 7.5 m SWIR archive and tasking prices in 2019 (no figures in extract; outdated). — [Apollo Mapping 2019](https://apollomapping.com/blog/worldview-3-swir-update-3-7-meter-resolution-updated-pricing)
- Pixxel VNIR tasking: USD 8/km². — [Pixxel docs](https://docs.pixxel.space/documentation/getting_started/pricingandrefunds/imagery_pricing/tasking)
- Planet Tanager: USD 6–9/km², about 100 km² (reseller, indicative). — [SkyWatch](https://skywatch.com/geospatial-data-providers/planet/)
- 50 cm archive: USD 8–18/km²; 30 cm archive: USD 17–26/km² (GeoPera 2026 via Farmonaut). — [Farmonaut](https://farmonaut.com/mining/hyperspectral-satellite-mineral-mapping-gold-rare-earths-aster)

### Inferences
- Commercial imagery should be priced as a pass-through line item (cost plus about 15–25% handling), with the minimum-order floor shown explicitly. This is a recommendation, not a sourced figure.

### Gaps
- Pixxel SWIR or full-range band pricing was not captured (only VNIR shown). Pricing for tasking priority tiers and for Pakistan-specific licensing or export restrictions was not checked.
