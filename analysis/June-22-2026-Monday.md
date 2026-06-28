# Week Review — June 22–26, 2026 (EU & XAU)

**Reviewed:** 10 entries (5 days × 2 pairs)
**Trades taken:** 0 | **Present days:** Tue, Wed, Fri (both pairs) + Thu partial (XAU only)
**Analysis date:** June 27, 2026
**Prior review:** `2026-06-15_to_06-19-week-review.md`

---

## Headline

**Third consecutive zero-trade week — but this one is different from the last two.**

Last week's zero was driven by motivational erosion: a decaying start ritual, suppressed lethargy, identity pinned to a funding milestone. This week's zero is driven by **external disruption** (two family absences, one mid-session emergency, poor sleep from carry-over stress) combined with **genuinely sub-threshold markets**. Decision quality across every present session was high. The week also produced the most psychologically significant insight in three reviews: **the calculator functions as an emotional buffer** — removing subjective decision bias even when personal state is compromised.

---

## Status of Prior Action Items

| Item | Status | Notes |
|---|---|---|
| Process-based weekly score | ❌ Not implemented | User unfamiliar with the concept — defined below; to be implemented Week 5 |
| Hard-fix 4:30 start + timestamp log | ⚠️ Mostly kept | Only 10-min slip Friday (family stress bleed-through from Thursday conflict). No formal timestamp column yet. |
| NWOG backtest | ❌ Still not started | Week 3. Family conflict + pregnant wife + work pressure explain this week. Superseded by the NWOG implementation decision below. |
| Post-session notes every present day | ✅ Kept where applicable | Thu absences are legitimate exceptions |

---

## Decision-Quality Grade

| Day | Pair | P(t) | Decision | Grade | Why |
|---|---|---|---|---|---|
| Mon 22 | EU | — | Absent | — | Family event |
| Mon 22 | XAU | — | Absent | — | Family event |
| Tue 23 | EU | 45.33% | No trade | **A** | Sub-threshold. Smart read: anticipated first supply would be used as liquidity to reach higher OB. Played out exactly. |
| Tue 23 | XAU | 32.37% | No trade | **A** | Well sub-threshold. Price flipped supply and gave valid demand — but after killzone. Correctly stood down. |
| Wed 24 | EU | 62.72% → 40.5% | No trade | **A+** | OB #1 above threshold — valid setup, entry model never appeared. OB #2 sub-threshold — correctly avoided. Calculator explicitly saved a losing trade (supply invalidated, BSLQ taken). |
| Wed 24 | XAU | 60.52% | No trade | **A** | Above threshold, directionally correct, price hit SSLQ. No pullback = no entry model. Accepted without frustration — backtested response. |
| Thu 25 | EU | — | Absent | — | Family conflict — left work mid-day |
| Thu 25 | XAU | 20.85% | No trade | **A** | Pre-session completed, left at 6PM (family emergency). Sub-threshold, poor OB quality. Correctly marked absent. |
| Fri 26 | EU | 54.41% → 21.84% | No trade | **A** | Scenario 1: correctly identified early-seller-liquidity risk (daily OB not yet mitigated). Scenario 2: post-flip demand, very low numbers. Bias adapted cleanly under personal stress. |
| Fri 26 | XAU | 36.79% | No trade | **A** | Sub-threshold. Naked eye also not confident. Price ran anyway — correctly reframed: low P(t) ≠ price won't go there; it means it's not your trade. |

**Overall week grade: A−**
*(Deducted only for 3rd consecutive NWOG implementation miss — now resolved by the decision below.)*

---

## Key Finding: The Calculator as Psychological Buffer

**Friday quote:** *"The decision bias was completely taken away. Different moods in my personal life is not affecting my trading."*

He came into Friday carrying weight from a serious family conflict (Thursday), poor sleep, 10-minute late start. In most traders that combination produces clouded reads, premature certainty, forcing. In his session: two clean scenarios evaluated, threshold respected, bias correctly flipped when price flipped the supply.

**Why it works:** the calculator externalises the final verdict. You don't need emotional clarity to reach a correct decision — you need to correctly identify the factors. The judgment (which factors apply) still requires the trader; the conclusion doesn't require the trader to *feel* confident.

**Important distinction:**
- **The calculator** protects decision quality once you're at the desk
- **The process-based weekly score** (below) is what gets you to the desk

They solve different problems. One without the other leaves a gap.

---

## Patterns

**What held:**
- **Liquidity-as-liquidity read (EU Tue):** Correctly anticipated first supply's sellers would *become* liquidity for the move to the higher OB. Not structure-following — reading the market's intent.
- **Bias flip under stress (EU Fri):** Late start, carrying personal weight — still correctly adapted from sells to buys when price flipped supply. No anchoring.
- **Backtested acceptance of no-pullback moves (XAU Wed):** "6/10 times price hits liquidity straight. The 4/10 that pull back = 70–80% probability. Those are where my edge is." Calibrated response, not suppressed frustration.
- **XAU Fri reframe:** Low P(t) setup that hit target → interpreted correctly as a data point for year-end weight recalibration, not as a calculator failure.

**What to watch:**
- **"Damn sure" language (XAU Wed).** Directionally correct this time. The risk is when that certainty starts leaking into factor-filling on a day it's wrong. Watch for it.
- **Start time:** Only one slip this week and it was minor with clear cause. The formal timestamp log still hasn't been implemented — needed for the process score to be calculable.

---

## System Decision: NWOG Factor — Implemented

**Context:** identified Week 2 (XAU Tue June 16) as a live input gap — setup passed threshold but failed exactly as the naked eye suspected. NWOG was not modeled as a confluence factor.

**Decision (agreed June 27):** Add NWOG as **two separate factor rows** in the calculator, weight **1.6** each:

| Factor Row | Yes means | Bucket |
|---|---|---|
| NWOG — Target (price heading toward it, acts as magnet in trade direction) | Trade is targeting the NWOG | **Positive** |
| NWOG — Opposing (above for sells / below for buys — could invalidate entry) | NWOG could pull price through the entry | **Negative** |

**Logic:** at most one row is "Yes" per setup. Both can be "No" if NWOG is not relevant that session.

**Weight rationale:** 1.6 placeholder — reflects that NWOGs are materially stronger than FVGs (which run ~0.6–1.5 in the calculator). To be recalibrated via backtest when life circumstances allow (currently: work pressure + pregnant wife). The 1.6 placeholder does real work immediately; backtest refines it later.

**Formula reminder:**
> P(t) = (Σ positive weights − 0.5 × Σ negative weights) ÷ total factor count

A NWOG-opposing "Yes" at 1.6 → removes 0.5 × 1.6 = 0.8 from the numerator. Meaningful suppression on a marginal setup.

---

## Process-Based Weekly Score (New — Starting Week 5)

**Problem it solves:** the only visible progress signal is "did I get funded." Zero trades for three weeks = zero visible progress = motivation fuel depletes. The score gives a win condition reachable with zero trades.

**Scoring table (reviewer calculates this — trader just journals):**

| Behavior | Points | How reviewer checks |
|---|---|---|
| Present day started at or before 4:30 | 1 pt per present day | Start time written in pre-session notes |
| Post-session note written on every present day | 1 pt per present day | Directly from journal |
| Every setup: confluence calculator run and documented | 1 pt per setup | Factor table present in session updates |
| NWOG factor applied on relevant setups | 1 pt per relevant session | NWOG rows present where applicable |
| No rule breaks (forced trade, chased outside killzone, factor omitted to inflate score) | 3 pts for the week | Reviewer judgment from journal |

**Target:** 80%+ of possible points = winning week.
**Requirement from trader:** write actual start time in pre-session notes (e.g. `Started: 4:28`). Without it, start-time adherence cannot be scored.

---

## Action Items — Next Week

| Priority | Action | Detail |
|---|---|---|
| **P1** | **Add NWOG rows to the calculator** | Two rows, weight 1.6 each, as defined above. Apply from Monday. |
| **P2** | **Log start time in pre-session notes** | One line: `Started: 4:3X`. Required for process score to be calculable. |
| **P3** | **Process score goes live** | Reviewer will calculate and include in next week's report. |
| **P4** | **Keep** post-session notes on all present days | Working. Maintain. |

---

## Carried Forward

- **Session-liquidity instinct (deferred codification):** No new data point. Still deferred.
- **4H-OB-against-direction pattern:** No new instance this week. Still watching — do not adjust weight on 2 data points.
- **Motivational erosion (Week 2 flag):** This week's disruptions were external (family), not internal (lethargy). Monitor: if dry run extends into Week 5 with no external disruptions, does the lethargy pattern resurface?
- **NWOG backtest (full):** Deferred indefinitely given life circumstances. Placeholder weight 1.6 active. Revisit when bandwidth opens.

---

*Generated by the trade-mentor review process.*
