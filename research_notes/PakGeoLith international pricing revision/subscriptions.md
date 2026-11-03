# International pricing benchmarks for PakGeoLith subscription tiers

FX convention: USD 1 = PKR 277 (spot reported at 277.04 on 8 Oct 2026, 277.23 on 9 Oct, 276.76 on 11 Oct 2026; no November 2026 print found) — [LongForecast](https://longforecast.com/usd-to-pkr-forecast); [30rates](https://30rates.com/usd-to-pkr-today-forecast-dollar-to-pakistani-rupee). Using 278 instead changes the numbers by less than 0.5%. Research date: 3 Nov 2026. Most enterprise vendors don't publish prices, so many figures come from procurement aggregators (Vendr, CostBench) and are marked that way.

## Mining data platforms and mining trade press: what do they charge?

### Takeaway
Mining intelligence prices fall into three bands. Retail and self-serve products cost USD 10–100/month (PKR 2.8k–28k). Professional databases cost about USD 4,400/user/year (PKR 1.2M). Institutional terminals cost USD 13k–215k per contract per year. Even PakGeoLith's old PKR 10,000/yr top tier (about USD 36) was below the cheapest global retail mining-data subscription (Opaxe Standard, USD 120/yr).

### Cited Findings
- **Mining Intelligence (miningintelligence.com)**: "Subscriptions start from US$4,400 per user", which covers the full dataset. That is about PKR 1.22M per user per year. Higher tiers are not published (quote only). — [Mining Intelligence](https://www2.miningintelligence.com/exploration)
- **Opaxe** (mining announcements/data): Standard USD 10/mo, Essential USD 50/mo, Premium USD 100/mo, with discounts for paying annually. Premium adds drill-result comparisons and resources/reserves data. In PKR that is about 2,770 / 13,850 / 27,700 per month. Homepage metadata may be stale. — [Opaxe](https://www.opaxe.com/)
- **Mining Data Online**: three packages. Research covers mine type, location, ownership, deposit, reserves, production, LOM, workforce and financials. Custom is Research plus selected modules. Ultimate is Research plus all modules, aimed at large corporates, consultancies and investors. Prices appear as monthly equivalents but are billed annually ("charged once per year"). Buyers choose the number of licences at checkout. Regional datasets cover Global, Oceania, USA, Canada, LatAm, Africa, and Europe+Asia. Dollar amounts were not visible on the page. Payments are non-refundable. — [Mining Data Online](https://miningdataonline.com/)
- **S&P Capital IQ Pro** (includes Metals & Mining): Vendr data shows contracts from about USD 14,800 to 215,000/yr, with a median around USD 53,000. A later Vendr snapshot shows USD 13,500–51,672. For firms with 8 or fewer seats, estimates run USD 7,875–18,750 per user per year. Per-user estimates overall vary by more than 10x. — [CostBench](https://costbench.com/software/financial-data-terminals/sp-capital-iq/); [GeminIQ](https://www.geminiq.com/blog/capital-iq-pricing-cost-explained); [AgentTrading](https://agenttrading.ai/blog/capital-iq-cost)
- **GlobalData** (Mining Intelligence Center): no public price. Vendr/ZoomInfo buyer data puts the median at USD 68,500/yr (range USD 43,000–73,875). Single mining reports sell for about USD 995. — [ZoomInfo/GlobalData pricing](https://pipeline.zoominfo.com/sales/globaldata-pricing); [GlobalData store](https://www.globaldata.com/store/report/rare-earths-mining-market-analysis/)
- **Mining Journal (Aspermont)**: after a 30-day free trial, digital access costs GBP 236/month, cancellable. A separate Dec 2025 item says the Mining Journal e-edition is now free. — [Mining Journal subscription](https://subscriptions.mining-journal.com/subscribe?sourcecode=MJDigitalMonthlyFreeFirstMonth); [Mining Journal news](https://www.miningjournal.net/news/2025/12/mining-journal-e-edition-available-at-no-charge/)
- **The Northern Miner**: digital is USD 134/yr in US and Canada (website plus digital replica edition). International buyers must call. Pocketmags sells the digital edition for GBP 64.99/yr or EUR 79.99/yr. — [Northern Miner](https://www.northernminer.com/subscribe-/); [Pocketmags](https://pocketmags.com/the-northern-miner-magazine)
- **ICMJ Prospecting & Mining Journal**: USD 31.95–48.95/yr, depending on region and format. — [ICMJ](https://www.icmj.com/subscribe/)
- **Western Australia government tenure/cadastre data (Landgate)**: tenure data costs AUD 4.00 per 10 records one-off, plus an extraction charge of AUD 213.40/hr (1.5 hr minimum). Cadastral data costs AUD 4.80 per 100 parcels one-off. Annual statewide access is priced per 10 parcels: AUD 0.48 for 1–2 seats, AUD 0.96 for 3–10 seats, AUD 2.40 for corporate. These pages are about 3.7 years old. Many WA datasets are free to download. — [Landgate tenure](https://www.landgate.wa.gov.au/location-data-and-services/discovering-landgate-data/tenure-data/); [Landgate cadastral](https://www.landgate.wa.gov.au/location-data-and-services/discovering-landgate-data/cadastral-data/); [QGIS in Mineral Exploration](https://qgis-in-mineral-exploration.readthedocs.io/en/latest/source/accessing_data_over_web/landgate.html)

### Inferences
- PakGeoLith is a mineral-occurrence and tenure atlas with a legal register, which puts it between Opaxe (USD 10–100/mo) and Mining Intelligence (USD 4,400/user/yr). For foreign users (juniors, consultancies, investors looking at Pakistan), a professional tier of USD 300–1,200/user/yr and a team or enterprise tier of USD 3k–15k/org/yr is plausible next to these anchors. That is about PKR 83k–330k and PKR 0.8M–4.2M.
- The seat-based and contract figures support three conventions: per-seat pricing at professional level, per-org contracts at enterprise level, and regional dataset packs (as Mining Data Online does). A "Pakistan-only" pack fits naturally into that model.
- Landgate's per-record and per-hour extract charges are a precedent for metering bulk tenure and extract exports separately from the subscription, for example on an API or data-export tier.

### Gaps
- No public prices were found for Wood Mackenzie, Fastmarkets, Benchmark Mineral Intelligence, Project Blue, CRU, MinEx Consulting, Natural Resource Holdings, Mindat, MiningIR, Mineral Hub, Tenement Hub, Spatial Dimension/Landfolio portals, or Canadian claims data (searches returned nothing usable). All appear to be quote-only.
- The dollar amounts for Mining Data Online's packages are not shown without logging in or requesting an invoice.

## Geospatial and Earth-observation platforms with public pricing

### Takeaway
Self-serve geospatial SaaS prices cluster at three levels: about USD 20–50/month for an individual analyst, USD 125–250/month for a professional or small team, and USD 500–1,250+/month for an enterprise org. Imagery and compute are usually metered by credits on top of the subscription.

### Cited Findings
- **EOS LandViewer**: Starter is free (vendor says 5 scenes/mo; a 2026 review says 10). Explorer is USD 19.99/mo and Pro is USD 49.99/mo (about PKR 5,540 and 13,850). High-resolution imagery is extra at USD 1.70–30.00 per km². — [EOS LandViewer](https://eos.com/landviewer/); [SoftwareWorld](https://www.softwareworld.co/software/eosda-landviewer-reviews/)
- **Sentinel Hub (Planet Insights Platform)**, third-party listing, unverified: Exploration EUR 30/mo for 1 user, Basic EUR 125/mo for 1 user, Enterprise EUR 500/mo for up to 10 users. Sentinel Hub's own documentation says commercial users need Basic or Enterprise, and batch processing requires Enterprise. Planet monitoring and processing add-ons require Basic or Enterprise S. — [toolfox.ru](https://toolfox.ru/services/s/sentinel-hub); [Sentinel Hub FAQ](https://www.sentinel-hub.com/faq/what-difference-between-different-license-packages); [Sentinel Hub forum](https://forum.sentinel-hub.com/t/about-planet-monitoring-and-processing-plans/8982)
- **Felt** (web GIS/collaborative maps): Team is USD 199/mo billed yearly or USD 249/mo monthly, and includes 3 seats, 25 viewers and 250 Felt AI credits/mo. Business is USD 599/mo and Enterprise starts at USD 1,250/mo (billed yearly). — [Felt pricing](https://felt.com/pricing); [Felt blog](https://felt.com/blog/felts-new-pricing)
- **UP42**: credit-based, where 100 credits = EUR 1. The minimum purchase is 10,000 credits (EUR 100). Credits expire after 24 months. Enterprise and support plans are quote-based. — [UP42 pricing](https://up42.com/pricing); [UP42 docs](https://docs.sa.up42.com/getting-started/purchase)
- **ArcGIS Online**: Creator includes 500 credits. Esri's US page does not publish the dollar price. Third-party figures: about USD 845/yr for a Creator package (undated), and a Business Analyst Web bundle with 1 Creator at USD 1,100/user/yr (G2). — [Esri pricing](https://www.esri.com/en-us/arcgis/products/arcgis-online/pricing); [Equator Studios](https://equatorstudios.com/what-will-arcgis-cost-personal-vs-team-pricing/); [G2](https://g2.com/products/arcgis-business-analyst/pricing)
- **Mapbox** (base-map cost to PakGeoLith): 50,000 free web map loads/mo, then about USD 5 per 1,000 loads, falling to about USD 3 per 1,000 above 200k. These figures are from third-party sources. — [Woosmap](https://www.woosmap.com/blog/mapbox-pricing); [StoreRocket](https://storerocket.io/learn/mapbox-pricing)

### Inferences
- A useful anchor ladder is: individual about USD 20–50/mo (LandViewer Explorer/Pro, Sentinel Exploration), professional about USD 125/mo (Sentinel Basic), and team about USD 200–600/mo for 3+ seats (Felt Team/Business, Sentinel Enterprise for 10 users at EUR 500).
- Felt's model (3 editor seats plus 25 viewers, with AI credits in the plan) is a close template for a PakGeoLith Team tier: a few full seats, read-only viewers, and a pooled AI allowance.
- Credit metering (UP42, Esri credits, LandViewer per km²) shows that pricing "5 km briefs" as credits or per-brief add-ons, on top of a subscription, is the market norm.

### Gaps
- Planet Explorer/Insights, SkyWatch, Farmonaut, Pixxel Aurora, Google Earth Engine commercial tiers, Earth Index and Preligens: no current public price found in this pass. The GEE pricing page exists ([Google Cloud](https://cloud.google.com/earth-engine/pricing)) but was not fetched.
- Sentinel Hub prices come from an unofficial listing and need checking on sentinel-hub.com/pricing.

## AI assistant pricing norms and fair pricing of token allowances

### Takeaway
General AI seats cost about USD 20–25/user/mo on standard plans and USD 100–200/mo for power users. Vertical legal and finance copilots cost USD 225–2,000/user/mo. At current API prices, 1M tokens/month costs PakGeoLith roughly USD 0.8 (mini-class model) to USD 4.4 (Sonnet-class). A 500K–1M token allowance can therefore be bundled into PKR-priced tiers at modest margin cost.

### Cited Findings
- **ChatGPT in Pakistan** (local-currency billing since Oct 2025): Go PKR 1,400/mo, Plus about PKR 5,700/mo, Business PKR 8,499/mo, Pro PKR 49,900/mo (launch reports). A May 2026 payment-provider blog cites Plus at PKR 6,900 on a bank card versus PKR 5,980 via SadaPay, which shows how card FX and tax add-ons affect the price. Go costs USD 8/mo in the US. — [ProPakistani](https://propakistani.pk/2025/10/10/chatgpt-go-brings-cheaper-gpt-5-access-to-pakistan/); [SadaPay](https://sadapay.pk/blogs/how-to-pay-for-chatgpt-plus-in-pakistan-in-2026); [OpenAI](https://openai.com/ur-IN/index/introducing-chatgpt-go/)
- **Claude**: Team Standard is USD 25/seat/mo monthly or USD 20 annually. Team Premium is USD 125 monthly or USD 100 annually, with about 5x usage. The minimum is reportedly 2 seats (some sources say 5). Max is an individual plan at USD 100 or 200/mo. These are third-party summaries. — [Krater](https://krater.ai/blog/claude-team-plan-pricing); [CostBench](https://www.costbench.com/software/ai-chatbots/claude/); [noqta](https://www.noqta.tn/blog/claude-code-pricing-2026)
- **Harvey** (legal AI): not public. Reported prices range from USD 100–200/user/mo for large deployments to USD 1,200–2,000+/user/mo, with minimums of about 20–25 seats on 12-month terms. — [Vaquill](https://www.vaquill.ai/blog/harvey-legora-cocounsel-pricing-reality-2026); [CostBench](https://www.costbench.com/software/ai-legal-tools/harvey/)
- **CoCounsel (Thomson Reuters)**: Core about USD 225/user/mo, All Access about USD 500/user/mo. A Westlaw Advantage solo bundle with CoCounsel is USD 639.20/user/mo on a 1-year term (June 2026). — [CostBench](https://www.costbench.com/compare/harvey-ai-vs-cocounsel/)
- **API token costs**: GPT-5 mini is USD 0.25 per 1M input tokens and USD 2.00 per 1M output. Claude Sonnet 5 is reportedly USD 2/10 (older Sonnet was USD 3/15). These figures are aggregator-sourced and should be checked against the official pricing pages. — [AnotherWrapper](https://anotherwrapper.com/llm-pricing/claude-sonnet-5); [race-mimo pricing report June 2026](https://race-mimo-v2.vercel.app/blog-ai-api-pricing-june-2026.html)
- **Felt Team** includes 250 AI credits/mo in a USD 199 plan, a precedent for bundling an AI allowance into a geospatial subscription. — [Felt pricing](https://felt.com/pricing)

### Inferences
These calculations are mine, from the prices above, assuming a 70% input / 30% output token mix:
- Mini-class model: about USD 0.78 per 1M tokens, or about PKR 215. 500K tokens costs about PKR 110; 1M about PKR 215.
- Sonnet-class model at USD 2/10: about USD 4.40 per 1M tokens, or about PKR 1,220. 500K tokens costs about PKR 610; 1M about PKR 1,220.
- Older pricing at USD 3/15: about USD 6.60 per 1M, or about PKR 1,830.
- RAG-style answers that retrieve law text or briefs are input-heavy, so cost may be at the lower end.
- A fair practice is to price allowances at 3–5x raw model cost. At the Sonnet-class rate that is about PKR 2,000–6,000/mo for 1M tokens; with a mini model as default it is far less.
- Raw model cost is small next to PakGeoLith's likely tier prices. The binding constraint is heavy users, so set hard caps, offer top-up packs (e.g., per 1M tokens), and use a cheaper default model with premium-model usage counted at a multiple.
- Vertical copilots charge 10–80x general chat seats (USD 225–2,000 vs USD 20–25) because of curated domain data. That supports pricing a mining-law and geology assistant above ChatGPT Go/Plus in Pakistan (PKR 1,400–5,700/mo). PakGeoLith's cost basis and willingness to pay are still far below Harvey or CoCounsel.
- Presenting allowances to users as "queries" or "credits" rather than raw tokens is common practice (Felt credits, Esri credits). This is not directly verified for AI assistants beyond Felt.

### Gaps
- Official Anthropic and OpenAI pricing pages were not fetched. Bloomberg GPT-like finance copilots (e.g., Bloomberg terminal AI) have no public pricing.

## Emerging-market and PPP pricing for Pakistan, and Pakistani B2B SaaS prices

### Takeaway
Global consumer SaaS in Pakistan typically sells for 15–40% of US list price. Examples: Spotify PKR 379/mo vs about USD 12 in the US; Canva Pro PKR 9,200/yr (about USD 33); ChatGPT Go PKR 1,400 (about USD 5) vs USD 8 in the US. B2B and professional tools like Microsoft 365 are often still billed in USD.

### Cited Findings
- **Spotify Pakistan** (official): Individual Rs 379/mo, Duo Rs 519/mo, Student Rs 199/mo. A Feb 2026 report said Spotify planned USD 1–2 increases in markets including Pakistan. — [Spotify PK](https://www.spotify.com/pk/premium/); [Arab News PK](https://www.arabnews.pk/node/2487581/pakistan)
- **Canva Pro Pakistan**: Rs 9,200/yr or Rs 1,150/mo for one person on canva.com (checked 29 Sep 2026 by a third-party guide). Canva sets prices by location. Grey-market resellers sell it for as little as PKR 1,000/yr. — [Pakera](https://pakera.pk/canva-pro-price-pakistan/); [Digiteazy](https://digiteazy.com/canva-pro-price-in-pakistan/)
- **Microsoft 365**: no PKR price. Pakistani buyers pay USD by card: Personal USD 99.99/yr, Family 129.99, Premium 199.99 (single guide). — [Pakera](https://pakera.pk/microsoft-365-price-pakistan/)
- **ChatGPT**: Pakistan is one of the markets with local-currency billing. Go at PKR 1,400 is about USD 5, against USD 8 in the US. — [ProPakistani](https://propakistani.pk/2025/10/10/chatgpt-go-brings-cheaper-gpt-5-access-to-pakistan/)
- **YouTube Premium Pakistan**: Rs 479 at its 2023 launch, with later unofficial figures around Rs 449/mo. No 2026 official price was found. — [ProPakistani 2023](https://propakistani.pk/2023/08/02/youtube-premium-and-music-arrive-in-pakistan-starting-at-rs-149/)
- **Card payments**: paying in USD by card adds a markup. The same ChatGPT Plus costs PKR 6,900 on a bank card vs PKR 5,980 via SadaPay, which argues for local PKR billing (bank transfer, JazzCash, Easypaisa). — [SadaPay](https://sadapay.pk/blogs/how-to-pay-for-chatgpt-plus-in-pakistan-in-2026)

### Inferences
- PPP practice suggests two price lists: a PKR list for Pakistan-resident individuals and SMEs at about 20–35% of the USD list, and a USD list for foreign and enterprise buyers. For example, if a global Professional tier is USD 49/mo, the Pakistan price would be about PKR 3,000–4,500/mo, or PKR 30–45k/yr with an annual discount.
- Consumer anchors set a floor for perceived value. ChatGPT Plus in Pakistan costs about PKR 68–83k/yr, and Canva Pro PKR 9,200/yr. PakGeoLith's old PKR 10,000/yr top tier was priced like a consumer design app, not a professional data tool.
- Enterprise buyers in Pakistan (mining companies, MDAs, banks, consultancies) normally pay USD-scale contracts for tools like M365 and ArcGIS. Per-org enterprise pricing in PKR millions is therefore defensible against Esri and S&P anchors.

### Gaps
- No official LinkedIn Premium or Adobe price for Pakistan was found (only a reseller range of Rs 6,000–40,000).
- No sourced data on typical Pakistani B2B SaaS prices (e.g., local ERP, HR or POS SaaS). This needs a separate search or the founder's local market knowledge.
