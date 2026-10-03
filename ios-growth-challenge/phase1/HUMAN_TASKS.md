# Human tasks: Phase 1 → Phase 2

Budget at start: **$1,000**. Spent so far: **$0**.
The tasks are independent, so run them in parallel. Task 3 is the most time-critical because it is a kill gate (G1).

---

## HUMAN TASK 1: Apple Developer Program enrollment

**Objective:** an active, paid developer account that can create the app record, the subscriptions and TestFlight builds.

**Decision (already made):**
- **If you already own an LLC or corporation with a D-U-N-S number, enroll as an Organization.**
  - Why: App Review Guideline 5.1.1(ix) says apps in "highly regulated fields (such as… healthcare)" should come from a legal entity. A personal food and symptom diary is probably not a healthcare *service*, but organization enrollment removes that rejection risk.
  - It also shows a company name as the seller.
- **If you do not, enroll as an Individual now.** Do not form an LLC for this. It costs time and money before any evidence exists. We will position the app as a personal self-tracking diary to reduce the 5.1.1(ix) risk.

**Steps:**
1. On an iPhone signed into the Apple Account you will use for this business, install the **Apple Developer** app from the App Store. Individual enrollment with identity verification is fastest there.
2. Make sure that Apple Account has two-factor authentication on (Settings → [your name] → Sign-In & Security).
3. In the Apple Developer app: **Account → Enroll Now**.
   - Choose Individual or Organization as above. Organization needs the D-U-N-S number, the legal entity name and a website on the company domain.
   - Complete ID verification and pay **$99 USD** (annual).
4. Wait for the confirmation email. Individual enrollment is usually fast; organization review can take days [R].
5. Sign in at https://appstoreconnect.apple.com → **Business** (called "Agreements, Tax, and Banking" in some versions).
   - Accept the **Paid Apps Agreement**.
   - Complete the **tax forms** (W-9 for a US person or entity).
   - Add a **bank account**.
   - Subscriptions cannot be sold until all three show *Active*.

**Expected cost:** $99. **Budget remaining after:** $901.

**What I need back:**
- Enrollment type (Individual / Organization).
- The exact seller name as Apple displays it.
- Team ID (developer.apple.com → Account → Membership details).
- Paid Apps Agreement status (Active / Pending).

**Why this matters:** without it nothing can ship, and the Paid Apps Agreement is required before we can create and test subscription products in the sandbox.

---

## HUMAN TASK 2: App Store Small Business Program

**Objective:** a 15% Apple commission instead of 30%. This raises net revenue per annual subscriber from $34.99 to $42.49.

**Steps:**
1. After Task 1 is complete and the Paid Apps Agreement is Active, go to https://developer.apple.com/app-store/small-business-program/ and click **Enroll**.
2. Sign in as the Account Holder.
3. Answer the associated-developer-accounts question truthfully. If you have no other developer accounts, the answer is "none".
4. Submit.

**Expected cost:** $0. **Budget remaining after:** $901.

**What I need back:** a screenshot or the text of the confirmation email.

**Why this matters:** every LTV and CAC number in the memo assumes 85% proceeds.

---

## HUMAN TASK 3: Keyword popularity pull (kill gate G1)

**Objective:** Apple's search popularity numbers for our candidate keywords. This decides between IBS (primary) and migraine (backup) **before** any build time is sunk.

**Background:** the iTunes Search API gave us ranking and competition, but not search volume. Popularity comes from Apple Ads data. Apple Ads keyword recommendations need a live app, so we use an ASO tool that exposes Apple's popularity score.

**Steps:**
1. Install **Astro** (macOS ASO tool, https://tryastro.app), or use **AppTweak** (https://www.apptweak.com). Use the free trial if one is offered.
   - **Hard cap: $30 total.** If neither has a usable free trial, buy one month of the cheaper plan and cancel immediately so it does not renew.
2. Set the store to **United States**, then enter every keyword below.
3. For each keyword, record **Popularity**, **Difficulty**, and the **number of apps ranking**.
   - Astro shows popularity on a 5–100 scale; 5 means minimum, effectively no volume. AppTweak uses its own volume score.
   - Record whatever the tool shows and tell me which tool you used.
4. Export to CSV if the tool allows it. If not, paste a table.

**Keywords (US):**

```
ibs
ibs tracker
ibs app
ibs diary
ibs diet
fodmap
low fodmap
fodmap diet
fodmap app
fodmap tracker
fodmap reintroduction
food symptom tracker
food symptom diary
food diary
food intolerance
bloating
bloating tracker
gut health
gut tracker
poop tracker
bowel movement tracker
sibo
sibo diet
ibs relief
monash fodmap
mysymptoms
bowelle
migraine
migraine tracker
headache tracker
headache diary
migraine buddy
```

**Expected cost:** $0–30. **Budget remaining after:** $871–901.

**What I need back:** a CSV or table with keyword, popularity, difficulty and #apps, plus the tool name.

**Why this matters:** this is gate G1 in the memo. If the core IBS/FODMAP terms are at minimum popularity, organic ASO can't carry the business and I switch to the backup concept before building anything.

---

## HUMAN TASK 4: Name and domain check (do not buy yet)

**Objective:** confirm the brand-name candidates are free before I finalize the listing.

Candidates I have pre-screened. All three have no App Store name collision as of 2026-10-03 [C]:
1. **GutCue**
2. **Easegut**
3. **Calmgut**

The App Store title will be `<Brand>: IBS & FODMAP Tracker` (30-character limit). The brand itself carries little ASO weight; the descriptive part does.

**Steps:**
1. For each name, search https://tmsearch.uspto.gov for **live** marks in classes 9 and 44 (also 42) with an identical or confusingly similar name. Record any hits.
2. Check `.com` availability for `<name>.com` and `get<name>.com` at Cloudflare Registrar or Porkbun.
3. **Do not buy yet.** I will choose after Task 3, because if G1 fails the name changes too.

**Expected cost:** $0 now; about $12 later. **Budget remaining after:** unchanged.

**What I need back:** for each name, trademark hits (yes/no plus mark name) and domain availability.

---

## HUMAN TASK 5: Community rules check (for validation gate G2)

**Objective:** find out where we may post a validation survey or landing page without breaking community rules. **Do not post anything yet.**

**Steps:**
1. Read the sidebar rules and the pinned "rules" or "wiki" post in each community: Reddit r/IBS, r/FODMAP, r/SIBO, r/ibs_c (if it exists), r/GERD.
2. For each one, record:
   - Are surveys allowed?
   - Is self-promotion or app promotion allowed, or limited to a weekly thread?
   - Is there a minimum account age or karma requirement?
   - Can moderators be messaged for approval?
3. If you are in any Facebook groups for IBS or low-FODMAP, record the same for those.
4. Check whether your Reddit account has existing post history. A brand-new account posting a link gets removed.

**Expected cost:** $0.

**What I need back:** a short table with community, members (as shown), survey rule, promotion rule and mod-approval path.

**Why this matters:** gate G2 (landing-page waitlist conversion) needs about 200 targeted visitors. Communities are the free source. Breaking their rules gets the account banned and burns the channel permanently.
