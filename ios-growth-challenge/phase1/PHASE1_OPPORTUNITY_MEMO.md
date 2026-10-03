# Phase 1: iOS Market Opportunity Discovery and Investment Memo

**Date:** 2026-10-03
**Status:** Decision made. Primary concept selected; validation gates defined below.
**Budget committed so far:** $0 of $1,000

Evidence labels used throughout:
- **[C] Confirmed**: pulled directly from App Store data or tool output in this repo (`data/`), or from a cited benchmark dataset.
- **[R] Reported**: a third-party claim I have not verified independently.
- **[H] Hypothesis**: my estimate. It must be validated before money depends on it.

---

## 0. Decision (TL;DR)

**Primary: "Gut trigger finder", an IBS food and symptom diary with a guided low-FODMAP elimination → reintroduction program.**
**Backup: a migraine trigger tracker built on the same logging and correlation engine (about 70% code reuse [H]).**

Why this one:
1. **Existing spending at subscription prices [C]:** mySymptoms charges $9.99/mo, $39.99 per 6 months or $59.99/yr behind a hard paywall (4.0k ratings). Fig (food-sensitivity scanner, 16.4k ratings) charges $69.99/yr. Monash (2.6k ratings) is a paid upfront app. Nerva (IBS hypnotherapy) is reported at about $199/yr [R].
2. **The organic search results are weak [C]:** the #1 result for "ibs tracker" is Cara Care, last updated 2020-10-27 according to the App Store API. Its US availability is reported as uncertain after the Bayer acquisition [R]. Results #3, #7 and #8 have 13, 4 and 9 ratings. In practice there is no current, maintained category leader for that search term.
3. **The complaints point to a specific product gap [C]:** across 912 negative (1–3★) reviews of 8 competitors:
   - Monash users complain that the reintroduction guide is hard to follow and that updates erased years of diary data.
   - Bowelle users ask for correlations between food and symptoms ("I expected a bit more 'intelligence'").
   - mySymptoms users complain about a paywall they were not told about.
   - Cara Care users report crashes, broken PDF export and no support.

   Nobody owns "tell me what my triggers are, guide me through reintroduction, never lose my data."
4. **Recurring value is built in:** the standard low-FODMAP protocol runs for weeks. Elimination is typically 2–6 weeks and reintroduction about 6–8 weeks [R; dietitian review required]. IBS is chronic. That gives a natural 3-month commitment, then ongoing maintenance and flare tracking.
5. **The audience is large and reachable:** 6.1% of US adults meet Rome IV IBS criteria in an 89k-person national survey [C, Gastroenterology 2023], which is about 15M adults [H, arithmetic]. The population skews female. There are active subreddits and gut-health dietitians on Instagram and TikTok, which makes it a good fit for creators.
6. **Buildable in about 3–4 weeks without a paid backend [H]:** SwiftUI, SwiftData with CloudKit, RevenueCat and TelemetryDeck. The core value is statistics, not an LLM, so marginal cost per user is about $0.

**The thing that could invalidate this (stated up front):** at category-median benchmarks, paid search CAC (about $128) is higher than first-year net revenue per subscriber (about $40). The $1,000 can buy learning and some subscribers, but **paid ads alone will not produce a profitable engine at median performance.** The plan only works if we beat the medians, mainly through cheap long-tail keywords and higher intent, and if organic ASO in the weak "ibs tracker" search results does a large share of the work. The economics are in §8 and the kill criteria are in §11.

---

## 1. Method

| Step | Source | Output |
|---|---|---|
| Category conversion and retention benchmarks | RevenueCat *State of Subscription Apps 2026* (115k apps, $16B revenue) | §2 |
| Apple Ads cost benchmarks | AppTweak Apple Ads benchmarks, US, Jan–Dec 2025 (~2,800 advertisers) | §2 |
| Competitive density per keyword | iTunes Search API, top 10 US results for 21 keywords | `data/appstore_serp_snapshot_2026-10-03.txt` |
| Review mining | App Store customer-review RSS, up to 500 most recent reviews × 8 competitors (3,298 reviews; 912 at 1–3★) | `data/competitor_reviews_2026-10-03.json`, `data/negative_review_themes_2026-10-03.txt` |
| Pricing | App Store product pages and third-party roundups | §4, §5 |

Limits of this method (read before relying on it):
- **Rating count is a proxy for install volume and revenue, not a measurement.** I have no Sensor Tower or Appfigures revenue estimates for these apps.
- **Keyword search popularity is not measured yet.** The iTunes API returns ranking, not volume. Search popularity has to come from Apple Ads or an ASO tool ([Human Task 3](#12-human-tasks-now)).
- **The theme classifier is a regex keyword match.** It over-counts broad terms such as "track". Treat the percentages as directional. The quotes in §5 were read manually.

All three scripts in `scripts/` can be re-run to refresh the data.

---

## 2. Market benchmarks that constrain every decision [C]

| Metric | Value | Source |
|---|---|---|
| Download → trial, median | Business 9.1%, **Health & Fitness 6.9%**, Education 6.5%, Utilities 6.5% | RevenueCat 2026 |
| Trial → paid, median | Travel 43.5%, **Health & Fitness 37.7%**, Photo & Video 22.2% (lowest) | RevenueCat 2026 |
| Trial length | 17–32-day trials convert at 42.5%; trials under 4 days at 25.5% | RevenueCat 2026 |
| 3-day trial cancellations | 55.4% happen on day 0 | RevenueCat 2026 |
| Hard paywall vs freemium | D35 conversion 10.7% vs 2.1%; RPI at D60 $3.09 vs $0.38; 1-year retention 27% vs 28% | RevenueCat 2026 |
| Annual plan churn | About 72% cancel within year 1; 35% of annual cancellations happen in month 1 | RevenueCat 2026 |
| Health & Fitness revenue mix | 60.6% of revenue comes from annual plans | Reported via Mirava, citing RevenueCat [R] |
| Apple Ads US CPT | Health & Fitness $1.68, Productivity $1.74, Utilities $1.23, Education $1.52, Business $3.33, Finance $4.17 | AppTweak 2025 |
| Apple Ads US tap → install | Health & Fitness 50.3% (lowest of all categories), Photo & Video 67.5% | AppTweak 2025 |
| Implied US CPI, Health & Fitness | $1.68 / 0.503 ≈ **$3.34** | Derived |
| Long-tail CPT examples | About $0.25 for niche terms vs $2.50+ for head terms | Reported by an indie guide [R] |

**What these numbers mean for us:**
- **Use a hard paywall with a trial, not freemium.** Freemium earns roughly 8× less revenue per install with no retention benefit.
- **Use a 7-day trial, not 3-day.** Longer trials convert better, and most 3-day trial cancellations happen on day 0.
- **Annual-first pricing.**
- Paid search CPI in Health & Fitness is about $3.34 at the median. Our keywords need to come in below that.

---

## 3. Long list: 26 opportunities screened

Each idea was screened on five questions: does spending already exist, is the value recurring, is the search competition weak enough, is the MVP size realistic, and does Apple Review or regulation threaten it. Ratings counts come from `data/appstore_serp_snapshot_2026-10-03.txt` [C].

| # | Concept | Screen result | Deciding reason |
|---|---|---|---|
| 1 | **IBS / low-FODMAP trigger finder** | **Finalist** | Paid category; weak "ibs tracker" search results; clear review gaps |
| 2 | **Migraine trigger tracker** | **Finalist** | Migraine Buddy 41.9k ratings, premium reported at $89.99/yr [R]; data-sharing complaints |
| 3 | **Blood pressure log** | **Finalist** | Paid at $29.99–39.99/yr [R]; "data held hostage" complaints |
| 4 | **Licensing exam prep (CDL / FAA Part 107)** | **Finalist** | $59.99–89.99 price points [R]; high intent |
| 5 | **GLP-1 medication companion** | **Finalist** | Very large demand; MeAgain 35.5k and Shotsy 32.9k ratings |
| 6 | Contractor estimate/invoice | Cut | Invoice Simple 122.8k and Invoice Fly 107.7k ratings; Business CPT $3.33; payments and support burden |
| 7 | Teleprompter for creators | Cut | Five apps with 14k–36k ratings; Photo & Video has the lowest trial → paid (22.2%) |
| 8 | Book / reading tracker | Cut | Goodreads 756k, Fable 81k, Bookly 62k ratings; low willingness to pay (~$30/yr) |
| 9 | Server tip tracker | Cut | ServerLife and TipTracker ~9.5k ratings each; generous free tiers; ~$25/yr ceiling [R] |
| 10 | Sobriety tracker | Cut | I Am Sober 188k ratings; Reframe 44.9k |
| 11 | Gluten-free scanner | Cut | Yuka 100k, Find Me Gluten Free 28k ratings; needs a product database |
| 12 | Kegel / pelvic floor | Cut | Wins mainly through Meta ads, which is the wrong channel for $1k; Kegel Trainer 8.2k ratings |
| 13 | Tinnitus sound relief | Cut | Free OEM apps dominate (ReSound 19k ratings); medical-claim risk |
| 14 | Acid reflux / GERD tracker | Merge into #1 | Weak search results (top app 262 ratings), but smaller and overlapping; becomes a later expansion of #1 |
| 15 | Histamine intolerance diary | Merge into #1 | Very weak search results (top 874 ratings), but a small niche |
| 16 | SIBO diet | Merge into #1 | Uses the same low-FODMAP protocol; becomes a keyword target for #1 |
| 17 | Eczema trigger tracker | Backlog | Weak search results (top 217 ratings); unclear willingness to pay; photo-heavy |
| 18 | PCOS tracker | Cut | Medical complexity and hormonal claims; PCOS Pal holds 2.6k ratings |
| 19 | Gout / purine diary | Backlog | Weak search results; older men; uncertain willingness to pay |
| 20 | Plant ID / care | Cut | PictureThis-scale incumbents; Meta-driven |
| 21 | AI calorie photo counter | Cut | Saturated; large ad budgets |
| 22 | ADHD visual planner | Cut | Tiimo is the incumbent; heavy UX scope |
| 23 | Habit tracker | Cut | Habit apps typically sell at about $1–2/mo [R]; low ARPU |
| 24 | Accent / pronunciation coach | Cut | Needs speech AI; marginal API cost; ELSA and BoldVoice are well funded |
| 25 | Faith / prayer app | Cut | Hallow and Bible Chat spend at scale; content-heavy |
| 26 | Mileage tracker (gig drivers) | Cut | Stride is free; Finance CPT $4.17 |

**What the cuts have in common:** the categories where you can see a lot of money (invoice, teleprompter, sobriety, reading) already have 30k–750k-rating leaders. A $1,000 budget cannot win organic rank there. The finalists combine proven willingness to pay with search results that are thin or out of date.

---

## 4. Five finalists in detail

### 4.1 IBS / low-FODMAP trigger finder (PRIMARY)
- **Customer:** women aged 25–45 with diagnosed or suspected IBS. Many have just been told by a GI doctor or dietitian to "try low-FODMAP." They are mid-protocol and overwhelmed. They currently juggle the Monash app (food lookup) with notes or spreadsheets (symptoms), and often a dietitian at $100–200 per session [H].
- **Problem and frequency:** they need to log every meal and every symptom episode, every day, for 6–14 weeks of protocol. After that they track flares. A daily, high-stakes activity.
- **Competitors and pricing [C]:** mySymptoms $9.99/mo or $59.99/yr; Fig $69.99/yr; Bowelle premium IAP $2.49–17.99 (tiers not broken out); Monash paid upfront; Cara Care free (stale); Fast FODMAP free with 21.3k ratings (lookup only).
- **Differentiation:**
  1. A guided reintroduction program: day-by-day challenge schedule, dose escalation and washout, per FODMAP subgroup.
  2. A trigger report with confidence levels.
  3. iCloud sync and backup, plus free export forever.
  4. Logging in about 10 seconds.
  5. Transparent trial and paywall.
- **MVP complexity:** medium-low. No server and no AI. The hardest part is protocol content accuracy, which is why the dietitian review in §9 is budgeted.
- **Search opportunity:** "ibs tracker", "ibs diary", "fodmap diary", "food symptom diary", "fodmap reintroduction", "sibo diet", "bloating tracker". The search results are weak and stale [C]; popularity is unknown.
- **Apple Ads:** high intent, Health & Fitness benchmark CPI ≈ $3.34. Long-tail may be lower [H].
- **Social and creators:** strong. Gut-health dietitians and IBS "day in my life" creators exist on TikTok and Instagram [R; to be catalogued in Phase 2]. Meta health-condition targeting has been restricted since 2022 [R], which weakens Meta.
- **Risks:** see §10.

### 4.2 Migraine trigger tracker (BACKUP)
- **Customer:** episodic migraine sufferers with 4+ attacks per month, mostly women aged 25–50.
- **Evidence:** Migraine Buddy has 41.9k ratings [C]; its premium tier is reported at $89.99/yr [R]; complaints focus on price, a clunky interface and pharma data-sharing [R]. Ranks 2–9 for "migraine tracker" range from 10 to 2.9k ratings [C].
- **Why backup and not primary:** a single dominant, actively maintained incumbent with 42k ratings is harder to outrank than IBS's stale leader. The upside is that it reuses the logging, correlation, report and paywall code.

### 4.3 Blood pressure log
- **Evidence:** SmartBP has 60.3k ratings and two other apps have 9–15k [C]. Plans are priced at $29.99–39.99/yr [R]. Users complain that the free tier hides data older than 2 weeks [R].
- **Why not:** the market is crowded at the top and saturated with misleading "finger BP measurement" apps that inflate competition for ads [R]. It is a low-differentiation commodity, and older users are harder to reach on TikTok and Instagram.

### 4.4 Licensing exam prep (CDL / Part 107)
- **Evidence:** CDL apps price at $19.99–29.99/mo and $59.99–89.99/yr [R], with 27k–48k ratings [R]. Part 107 search results are thin: top app 1,963 ratings [C].
- **Why not:** retention is structurally capped because users cancel the day they pass. The question bank must be accurate to current FAA/FMCSA material, which is a heavy content and liability load. It produces one-time revenue spikes, which conflicts with the recurring-revenue objective.

### 4.5 GLP-1 companion
- **Evidence:** the largest demand of all five. MeAgain has 35.5k ratings, Shotsy 32.9k (reported $49.99/yr [R]), and there are 8+ newer clones [C].
- **Why not:** the market is crowded and still being cloned weekly. The two leaders hold about 68k ratings between them. We would be the 15th entrant with the smallest budget.

---

## 5. Review mining: what IBS/FODMAP customers repeatedly say [C]

From `data/negative_review_themes_2026-10-03.txt` (912 reviews at 1–3★). Percentages are regex-directional.

| Theme | Share of negative reviews | Where it concentrates | Our response |
|---|---|---|---|
| Price / subscription / surprise charges | 41% | Fig 74%, Monash 49%, mySymptoms 31% | Clear trial-disclosure screen; price stated in the App Store description; cancel instructions in Settings |
| Serving size / data accuracy | 26% | Fast FODMAP, Monash, Cara | We do not ship a FODMAP lab database. We point to Monash for lookups and focus on the user's *personal* tolerance data |
| Food database gaps / search | 24% | Monash 34%, Fast FODMAP 30% | Free-text food logging with recents and favorites; no database dependency |
| Wanted patterns / insights / reports | 23% | Cara 45%, mySymptoms 40%, Bowelle 54% | **Trigger report with lag window (0–48 h) and confidence** |
| UI / usability | 23% | All | 10-second logging; one-tap repeat meal |
| Bugs / crashes | 11% | Cara 26% | Native SwiftUI, small surface area |
| **Data loss / sync / export** | 10% | Monash, Cara, mySymptoms | **iCloud sync plus PDF/CSV export that is free forever, even after lapse** |
| Reintroduction guidance | 6% (Monash 13%) | Monash | **Guided challenge calendar** |

Representative quotes (verbatim, US App Store):
- Monash, 3★: *"I wish there was a better way the app can be used to guide the reintroduction… have a plan that actually helps you reintroduce these foods."*
- Monash, 1★: *"Latest update erased years of data!!!! … it's bizarre that it's even possible in 2025."*
- Bowelle, 3★: *"I expected a bit more 'intelligence' from the app. I was looking for some sort of correlations listed for types of food eaten and times and how they line up with my BM."*
- mySymptoms, 1★: *"The description in the App Store says that the app is free for logging… Once they have all your info they tell you it is a two week trial."*
- Cara Care, 3★: *"WAS the Best Tracking App… They sent me a PDF of my tracking… the data was all jumbled up."*
- Fig, 3★: *"I would pay $3.99/month but $70 is too much."*

**Conclusion:** users already pay. They are angry about being surprised, losing data and not getting insight, not about the idea of paying.

---

## 6. Scoring

Scale 1–5 (5 = best for us). Weights reflect the objective: recurring revenue with repeatable acquisition on $1k.

| Factor (weight) | IBS/FODMAP | Migraine | BP log | Exam prep | GLP-1 |
|---|---|---|---|---|---|
| Pain severity (2) | 5 | 5 | 3 | 4 | 4 |
| Use frequency (2) | 5 | 4 | 4 | 4 | 4 |
| Recurring value / retention (3) | 4 | 4 | 3 | 1 | 4 |
| Proven willingness to pay (3) | 4 | 4 | 3 | 5 | 4 |
| Incumbent weakness (3) | 5 | 3 | 2 | 3 | 2 |
| Organic search opening (3) | 5 | 3 | 1 | 3 | 1 |
| Paid acquisition viability (2) | 3 | 3 | 2 | 4 | 2 |
| Creator / community distribution (2) | 4 | 3 | 2 | 2 | 4 |
| MVP complexity (inverted) (2) | 4 | 4 | 5 | 2 | 4 |
| Review / regulatory risk (inverted) (2) | 3 | 3 | 3 | 3 | 2 |
| **Weighted total (max 120)** | **102** | **86** | **65** | **74** | **73** |

Scores are judgments [H] grounded in §2–§5. The ranking holds even if any single factor moves by ±1.

---

## 7. Product and MVP

**Working name:** to be chosen after the keyword popularity pull. The title should carry "IBS" and "FODMAP"; the subtitle "Food & Symptom Tracker".

**Core loop:** log meal → log symptom → see trigger report → follow today's protocol step.

**MVP scope (build only this):**
1. Onboarding (about 7 screens, personalized): diagnosis status, main symptoms, current protocol phase, goal, then a first log.
2. Logging:
   - **Meals:** free text with recents/favorites and optional FODMAP-group tags.
   - **Symptoms:** pain, bloating, gas, urgency, 0–10 severity.
   - **Bowel movements:** Bristol scale 1–7.
   - **Context:** stress, sleep, period. Optional HealthKit read for sleep and cycle.
3. Protocol engine:
   - **Elimination phase:** day counter and checklist.
   - **Reintroduction phase:** a 3-day escalating challenge per subgroup with washout days. The order and doses follow published dietitian methodology and are reviewed by an RD before launch.
4. Trigger report: per food or tag, symptom rate within a configurable lag window vs baseline, with a minimum-sample rule (never claim a trigger from fewer than 3 exposures) and plain-language confidence.
5. Doctor-ready PDF export and CSV export, **always free**.
6. Reminders: meal-time log nudges and reintroduction-day instructions. Every notification carries a concrete action.
7. Paywall after onboarding: annual (default, "best value") plus monthly, 7-day trial, explicit trial-end date shown on screen.
8. Analytics events: the full list from the brief. Instrumented with TelemetryDeck, which is privacy-first, needs no ATT prompt and has a free tier. RevenueCat handles subscription events.

**Explicitly out of MVP:** accounts and login (iCloud only), barcode scanning, FODMAP food database, AI meal photos, social features, Android, web.

**Stack:** SwiftUI, SwiftData + CloudKit, RevenueCat (free under $2.5k monthly tracked revenue [R]), TelemetryDeck, StoreKit 2, iOS 17+.

---

## 8. Subscription model and expected economics

**Pricing decision:** $49.99/yr (default) and $9.99/mo, 7-day free trial on annual. No weekly plan and no lifetime plan at launch.
- **Why $49.99:** incumbents anchor at $59.99 (mySymptoms) and $69.99 (Fig). Price is the #1 complaint theme (41%). Coming in about $10–20 below the anchors while staying in the proven band is a deliberate positioning choice. First price test: $59.99 after 100 paywall views.
- **Why no weekly plan:** the value is clearly a multi-month protocol. A weekly plan would raise refund and anger risk in a category already full of "scam" reviews.
- **Proceeds:** 85% under the App Store Small Business Program, so $42.49 net per annual subscriber and $8.49 per monthly.

| Metric | Median case (benchmarks) | Target case [H] | Basis |
|---|---|---|---|
| Apple Ads CPI (US) | $3.34 | $1.75 | AppTweak H&F; target assumes long-tail and exact match |
| Install → trial | 6.9% | 10.5% | RevenueCat H&F; target assumes search intent plus personalized onboarding |
| Trial → paid | 37.7% | 38% | RevenueCat H&F |
| Install → paid | 2.6% | 4.0% | Product of the two rows above |
| **CAC (paid)** | **$128** | **$44** | CPI ÷ install→paid |
| Plan mix | 70% annual / 30% monthly | same | H&F 60.6% annual revenue share [R] |
| Year-1 net revenue per subscriber | ≈ $40 | ≈ $40 | 0.7 × $42.49 + 0.3 × ($8.49 × 4-month average monthly lifetime [H]) |
| 24-month LTV (net) | ≈ $48 | ≈ $48 | Adds annual renewal at about 28% (RevenueCat 1-year retention 27–28%) |
| **Break-even CAC** | **≈ $48** | **≈ $48** | Equals the 24-month LTV |
| LTV : CAC | 0.4 | 1.1 | |
| Payback | Not reached | About 13–18 months | |

**Plain reading:** at median performance, paid acquisition loses money. At target performance (CAC ≈ $44, just under the ≈ $48 break-even) it pays back in about 13–18 months. That is thin; the margin for error is small. We get to a profitable engine only through:
1. Organic installs from ranking in weak search results.
2. Creator and community traffic.
3. A funnel that beats the medians.

This is why the budget below spends on measurement first and scales only on evidence.

**What $1,000 realistically buys [H]:** with about $600 of acquisition spend at a $44–128 CAC, roughly 5–14 paid subscribers come from paid channels. Every milestone beyond that has to come from organic, creator and community channels. I will report against this honestly; I will not dress up downloads.

---

## 9. Budget plan ($1,000)

| Bucket | Item | Amount | When |
|---|---|---|---|
| Infrastructure | Apple Developer Program | $99 | Now |
| Infrastructure | Domain (landing page, privacy policy, support) on free GitHub Pages hosting | ~$12 | Now |
| Infrastructure | RevenueCat, TelemetryDeck, CloudKit | $0 (free tiers) | Build |
| Credibility / content | Registered dietitian review of the protocol and copy (freelance, fixed fee); also gives us "reviewed by an RD" social proof | $150 | Before TestFlight |
| Validation | Keyword data (ASO tool, 1 month, only if Apple Ads cannot provide popularity) | ≤$30 | Week 1 |
| Acquisition: test 1 | Apple Ads exact match, 5–10 keywords, $10/day | $50 | Launch +0 |
| Acquisition: test 2 | Expand to winning keywords, competitor terms, Search Match discovery | $100 | After test 1 gate |
| Acquisition: test 3 | Conversion-economics test on the best ad group | $200 | After test 2 gate |
| Acquisition: creators | 2–3 micro gut-health creators (flat fee plus affiliate/promo code) | $150 | Week 2 post-launch |
| Acquisition: scale | Best channel | ~$150 | Only if CAC ≤ $45 |
| Reserve | Contingency | ~$59 | |
| **Total** | | **$1,000** | |

The split is about 11% infrastructure, 18% validation and content, and 65% acquisition. Acquisition is staged; every stage has a gate (§11).

---

## 10. Risks that could invalidate the business

| Risk | Label | Mitigation / test |
|---|---|---|
| Search popularity for "ibs tracker"-type terms is too low to drive organic volume | [H], unmeasured | **Human Task 3.** Kill or reposition if the core terms are at minimum popularity |
| Paid CAC stays at the median (~$128) | [H] | Staged spend and kill criteria; lean on organic and creators |
| App Review: Guideline 1.4.1 (medical apps) and 5.1.1(ix) ("highly regulated fields such as healthcare… should be submitted by a legal entity") | [C] guidelines exist; [H] on how they apply to a diary | Position as a personal self-tracking diary: no diagnosis, no treatment claims, prominent "not medical advice." **Organization enrollment preferred if you already have an LLC** |
| Protocol content error causes harm or bad reviews | [H] | RD review before TestFlight; cite sources in-app |
| Meta conversion optimization restricted for health apps | [R], not verified | Not relying on Meta. Will verify before any Meta spend |
| Correlation engine shows false triggers | [H] | Minimum-exposure rule, confidence labels, "discuss with your clinician" framing |
| Incumbent wakes up (Bowelle ships correlations, Monash rebuilds) | [H] | Speed; protocol guidance is the moat, not logging |
| New entrants are targeting the same gap: "Gutsy AI: IBS Trigger Finder" (22 ratings, updated 2026-09-26), "Settle: IBS & Gut Tracker" (0 ratings), GutPal, GastroLog, Triggerbites AI | [C] they exist; [H] they are early | Confirms others see the gap. None has review traction yet. Re-check the search results monthly; outrank on reintroduction guidance plus trust |
| Retention dies after reintroduction ends (~week 12) | [H] | Maintenance mode (flare tracking, "safe foods" list, monthly report). Measure first-renewal rate |

---

## 11. Validation gates and kill criteria

Gates run **in parallel with the build**. The MVP costs time, not cash; the cash goes to ads only after the gates.

| Gate | Pass | Kill / pivot |
|---|---|---|
| G1 Keyword popularity (Apple Ads or ASO tool) | At least 3 core terms above minimum popularity, and "ibs tracker" or "fodmap" in the top tiers | All core terms at minimum popularity → switch to backup (migraine) before spending |
| G2 Landing page with price shown, organic community traffic | ≥15% of visitors join the waitlist with the price visible | <5% after 200 visitors → rework positioning |
| G3 TestFlight (10–20 IBS users from the waitlist) | ≥60% log on 5 of the first 7 days | <30% → fix the core loop before launch |
| Ads test 1 ($50) | Tap-through ≥5%, CPI ≤$4 | CPI >$6 on all keywords → stop, fix the listing |
| Ads test 2 ($100) | Install → trial ≥7% | <4% → fix onboarding/paywall before more spend |
| Ads test 3 ($200) | Projected CAC ≤$70 with trend improving | CAC >$100 → stop paid; organic and creators only |
| Scale | CAC ≤$45 (below the ≈ $48 break-even) | |

---

## 12. Human tasks (now)

See `HUMAN_TASKS.md` for exact steps. In brief:
1. Enroll in the Apple Developer Program ($99).
2. Enroll in the App Store Small Business Program ($0).
3. Pull keyword popularity for the list in `HUMAN_TASKS.md` ($0–30).
4. Register the domain (~$12).
5. Check the self-promotion rules of the IBS communities ($0).

## 13. What I do next without you
- Phase 2 product spec: screen-by-screen onboarding, paywall, protocol engine, trigger-report math and analytics event schema.
- Xcode project scaffold (SwiftUI, SwiftData, CloudKit, RevenueCat, TelemetryDeck) committed to this repo.
- Landing page and privacy policy (static, for GitHub Pages).
- ASO draft: name, subtitle and keyword-field candidates, ready to finalize once Task 3 returns.
- Creator target list (gut-health dietitians and IBS creators) with audience fit notes.

---

## Sources
- RevenueCat, State of Subscription Apps 2026: https://www.revenuecat.com/state-of-subscription-apps and https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026
- Business of Apps, trial benchmarks: https://www.businessofapps.com/data/app-subscription-trial-benchmarks/
- AppTweak, Apple Ads benchmarks 2026: https://www.apptweak.com/en/aso-blog/apple-ads-benchmarks
- Mirava, subscription revenue by category: https://www.mirava.io/blog/subscription-revenue-by-app-category-2026-data
- Rome IV IBS prevalence in the US (Gastroenterology 2023): https://www.gastrojournal.org/article/S0016-5085(23)04889-8/fulltext
- mySymptoms App Store page: https://apps.apple.com/us/app/mysymptoms-food-diary/id405231632
- Bowelle App Store page: https://apps.apple.com/us/app/bowelle-the-ibs-tracker/id1436064640
- Monash FODMAP App Store page: https://apps.apple.com/us/app/monash-fodmap-diet/id586149216
- IBS app comparison (Cara Care US availability after the Bayer acquisition): https://www.lin.health/insights/best-apps-ibs
- Migraine Buddy pricing and complaints: https://www.getmigra.com/blog/best-migraine-tracker-app-2026/
- Blood pressure app pricing and complaints: https://apps.apple.com/us/app/blood-pressure-tracker/id1296471956
- CDL app pricing: https://apps.apple.com/us/app/cdl-practice-test-2025/id1469003902
- GLP-1 tracker landscape: https://shotsyapp.com/best-glp-1-tracker-apps/
- Joist pricing and complaints: https://www.getonecrew.com/post/joist-app-reviews
- Tip tracker pricing: https://tipjarapp.app/
- Indie revenue reference points: https://getappniche.com/guides/ios-app-success-stories
- Apple Ads long-tail CPT example: https://trysonar.app/blog/apple-search-ads-guide
