# Writing Patterns to Avoid

Anti-slop guidance for Claude. Drop this into your project's `CLAUDE.md`, system prompt, or custom instructions to stop Claude generating the patterns that mark text as machine-written.

The guidance is structured in two tiers:

- **Tier A — zero exceptions.** Rhetorical moves with no human upside. Banned in every form, every variant. The "used once with clear intent" exception does NOT apply.
- **Tier B — avoid clustering.** Vocabulary, structural, and formatting tics. A single instance can work; clustering is the failure mode. Aim for varied, specific, imperfect human writing.

Two passes are required before returning any prose: scan once for Tier A violations, again for Tier B clustering. Both passes are mandatory, not optional.

---

## 1. Rhetorical patterns (Tier A — zero instances)

### Negative parallelism: "It's not X, it's Y"

The single most recognisable AI tell. Read this carefully because the rule is **semantic, not syntactic**.

**The rule:** do not write any sentence that asserts what something IS by first asserting what it ISN'T. Do not pair a negated identity claim with a positive identity claim about the same subject. State the positive claim directly, without the negation.

**The pattern, not the words.** This rule covers the rhetorical move regardless of which verbs, connectors, tenses, or punctuation are used. The shapes below are all the same violation:

- "It's not X, it's Y." / "It isn't X. It's Y." / "It isn't X — it's Y." / "It isn't X; it's Y."
- "Not X, but Y." / "Not just X, Y." / "Not X. Y."
- "Don't just X, Y." / "You don't just X, you Y." / "We don't just X, we Y."
- Verb-tense variants: "X was never A — it was B." / "X has never been A. It's B."
- Sense-verb variants: "It feels like A. It's actually B." / "It looks like A, but it's B." / "On the surface it's A. Underneath it's B."
- Disguised reframes: "X and calling it Y." / "X but really Y." / "What you call X is actually Y." / "X disguised as Y."
- Self-correcting variants: "I'm not saying X, I'm saying Y." / "It's less X, more Y."
- Expectation-vs-reality: "You think X. It's Y." / "You'd expect X. You get Y."

**The single test.** Read the sentence with the negated half removed. Does it still make the point? If yes — the negated half was rhetorical scaffolding (= AI tell) and must be cut. If no — the positive claim wasn't sharp enough; fix the claim, don't prop it up with a contrast.

**Different-subject contrast is fine — do not flag this:**

- ✓ "Big clients don't buy software — they buy the safest choice." (different objects being purchased; informational substitution.)
- ✓ "Most doctors say Vitamin D — the truth is, even Vitamin D isn't necessary for everyone." (contrast against external authority, not the writer's own claim.)

**Genuine state-shift carve-out.** Same-subject negate-then-assert is allowed when reporting a real shift the subject has actually moved through:

- ✓ "After the diagnosis you stopped asking is this serious — you started asking what do I do now." (genuine shift from one real question to another.)

**Banned still:** pseudo-deepening with no real shift. The diagnostic: did the subject genuinely move from state A to state B (allowed), or is the writer using contrast for emphasis on a single unchanged fact (banned)?

- ✗ "Burnout isn't an energy problem. It's a meaning problem." (no shift — burnout was always a meaning problem from the writer's view; pure rhetorical scaffolding.)

### Triple countdown: "Not X. Not Y. Just Z."

Do not build tension by negating two or more things before revealing the point. State the point.

- ✗ "Not a bug. Not a feature. A fundamental flaw."

### Self-posed rhetorical questions

Do not pose a question and answer it yourself in the same beat.

- ✗ "The result? Devastating."
- ✗ "What does this mean? Everything."

### Tricolon overuse (rule of three)

One rule-of-three construction per section, at most. Never stack three tricolons together. Never add a third item to complete the pattern if it doesn't earn its place.

### Decorative lists

Banned when scene-painting; allowed when load-bearing AND conversational.

**Banned (the default failure mode):** comma-separated three-item lists used as scene-painting where each item is essentially decoration on the same idea. Tell-tale form:

- ✗ "downloaded the app, built the perfect template, maybe colour-coded it"
- ✗ "podcasts during commutes, feeds during meals, videos during workouts"
- ✗ "phone in one hand, coffee in the other, three tabs open"

**Allowed (the carve-out):** comma-list tricolons where (a) each item is concrete and DISTINCT (different informational weight), AND (b) the rhythm is conversational.

- ✓ "AI is genuinely excellent at the early stage — exploring ideas, stress-testing a structure, helping you find the skeleton." (each item is a different distinct action.)

**Diagnostic:** are the three items doing genuinely different work (allowed), or are they three coats of paint on the same idea (banned)? If the second — pick one and cut the others.

### Anaphora abuse

Do not repeat the same sentence opener three or more times in quick succession. The "survey-the-failures" opening is a textbook offender:

- ✗ "You've tried the apps. You've tried time-blocking. You've tried every productivity system on YouTube."
- ✗ "It's about X. It's about Y. It's about Z."
- ✗ "Maybe you've X. Maybe you've Y. Maybe you've Z."

Replace with one specific concrete reference, not a stacked list of similar ones.

### False ranges: "from X to Y"

Do not use "from X to Y" unless X and Y are real endpoints with a meaningful middle.

- ✗ "From innovation to implementation to cultural transformation."

### Gerund-fragment flourishes

Do not end sentences with -ing participial phrases that tack on pseudo-analysis. If the analysis is worth making, make it a full sentence.

- ✗ "...highlighting the importance of..."
- ✗ "...underscoring the shift..."

### False suspense transitions

Do not promise revelation before an unremarkable point. The whole **class** is banned, not just specific phrases. The pattern is "Here's [what/why/how]" as a vague-revelation tease that doesn't name the revelation in the same beat.

Banned (non-exhaustive):

- ✗ "Here's the thing." / "Here's the kicker." / "Here's where it gets interesting."
- ✗ "Here's what most people miss." / "Here's what changed." / "Here's what shifted."
- ✗ "Here's what surprised me." / "Here's what I learned." / "Here's what nobody tells you."
- ✗ "Here's the part that matters."

**Semantic test:** does the phrase NAME the revelation in the same beat, or tease that a revelation is coming? If it teases without naming — banned.

**Acceptable substitutes** name the revelation immediately: "But the truth is [X]," "Once I figured out [specific X]," "Here's the truth about [specific topic] — [the truth itself]."

**Colon-reveal variant.** Same violation, different shape: a noun phrase, a colon, then a dramatic lowercase reveal. "The detail that makes it work: a separate agent grades it." "The best part: it learns." In writing this reads as a cheap trick; spoken aloud it's a pause before a punch, so it's tempting to treat as harmless delivery — apply the same semantic test anyway. If the payoff after the colon is generic or could've been said plainly, it's banned. Say it as a plain sentence instead: "A separate agent does the grading, which is what makes it work."

**Faux-insight framing.** A near-miss on the same pattern that flatters the writer/speaker as the lone expert rather than teasing a real reveal: "This is the part most people skip." / "What most people get wrong." / "The part everyone misses." Cut the setup and make the claim stand on its own: "The part everyone misses: distribution is the moat" becomes "Distribution is the moat."

### Pedagogical framing

Do not default to a teacher-student voice. Do not announce what you're about to do.

- ✗ "Let's break this down." / "Let's dive in." / "Let's unpack this."

### Vague attributions

Do not attribute claims to unnamed authorities. Either name the person, study, or source — or cut the claim.

- ✗ "Experts argue that..." / "Research shows..." / "Industry reports suggest..."

### Invented concept labels

Do not coin abstract compound phrases and use them as if they were established, rigorously defined terms.

- ✗ "the supervision paradox" / "the acceleration trap" / "workload creep"

### "Despite its challenges..."

Do not perform balance by raising a counterpoint only to dismiss it. If a counterpoint is real, engage with it; if not, don't manufacture one.

- ✗ "Despite these challenges, the initiative continues to thrive."

### Filler transitions and vague-filler phrases

Do not use throat-clearing transitions, or non-specific filler that pretends to add weight without adding meaning.

- ✗ "It's worth noting that..." / "Notably..." / "Importantly..."
- ✗ "where it counts" → name the specific work.
- ✗ "running in the background" → name the specific drain.
- ✗ "in the wider scheme of things" → drop or replace with the specific stake.

**The pub test:** would two friends say this to each other over lunch? If no — rewrite. The fix is always to name the specific thing the filler is gesturing at.

**The portability test:** could this line move unchanged into a video about a completely different topic, product, or niche? If yes, it's filler — cut it or replace it with a fact, mechanism, number, or consequence specific to this video. A line that's true of any script is doing no work in this one.

### Privileged-insight claims

Do not assert clarity instead of demonstrating it.

- ✗ "The reality is simpler and less flattering."
- ✗ "The real story is..."

### Interpretive metadiscourse

Do not step outside the content to tell the viewer what to notice, how much weight to give it, or how to interpret it. This is distinct from filler — it's commentary about the script itself, layered on top of a point instead of the point doing the work.

- ✗ "That last part matters more than it sounds."
- ✗ "The key point is..."
- ✗ "As you can see..."
- ✗ "This distinction matters."

If the point is already clear, delete the aside entirely. If it isn't clear, the fix is a fact, example, mechanism, or consequence — not a line assuring the viewer it's important.

### Fake-profound kickers

Do not end a section or video on a manufactured "deep" line — a cute metaphor, aphorism, or mic-drop sentence that turns a concrete point into forced poetry. This is a distinct failure from the formulaic closers in §3 below: those announce a conclusion, this one performs profundity.

- ✗ Section ends on: "...and that's the real secret nobody talks about."
- ✗ Section ends on: "In the end, it's not about the code. It's about the craft."

Do not rewrite a fake-profound kicker into a better metaphor — cut it and end on the clearest concrete sentence already in the section (this is what the Payoff rules in the writer skills already require: land the lesson cleanly or leave an open loop, never a manufactured mic-drop).

### Grandiose stakes inflation

Do not inflate every topic to world-historical significance. Match the register to the subject.

- ✗ "This will fundamentally reshape how we think about everything."
- ✗ "Will define the next era of computing."

### Patronising analogy

Do not default to analogy mode. Most concepts do not need to be "thought of as" something else. **Even ONE forced analogy is too many** — the temptation peaks when explaining a counter-intuitive idea, and that's exactly when you must resist.

- ✗ "Think of it like a highway system for data."
- ✗ "It's like..."
- ✗ "Imagine if you tried X but..."
- ✗ Medical-metaphor variant: "the fever, not the infection" / "the symptom, not the disease."

Name the thing directly. The concept doesn't need translation — explaining it well does the work.

### Imagined-world framing

Do not open or pivot with "Imagine a world where..." or its variants.

### False vulnerability

Do not perform self-awareness as a rhetorical device. Fourth-wall breaks and fake bias disclosures are AI tells.

- ✗ "And yes, I'm openly in love with..."
- ✗ "Since we're being honest..."

### Forced empathy

Do not insert generic empathy statements algorithmically.

- ✗ "Feeling overwhelmed is completely normal."
- ✗ "It's okay to feel uncertain."

### Generic universal truths

Do not write statements that are technically true but teach nothing.

- ✗ "Consistency is important."
- ✗ "Nothing good comes easy."

### Phantom-future projection

Do not manufacture stakes by imagining the reader's future. Stakes must come from the present: a concrete cost they're already paying, a problem already in front of them. Imagined-future predictions read as AI-confected drama.

- ✗ "You'll be running this exact loop six months from now."
- ✗ "A year from today, you'll wish you'd..."
- ✗ "By the time you realise it, you'll have wasted..."
- ✗ "Picture yourself five years on, still..."

Replace with a present-tense observation the reader can verify against their own experience right now.

### Fabricated specificity

Do not invent specific numbers, days, percentages, timeframes, or named moments that aren't grounded in the source. The failure shape is fake-precise: "every system collapsed around day 11" — both the "around" hedge AND the specific day 11 are invented.

If the source doesn't supply a specific number, drop the number entirely. The instinct to invent specifics for narrative texture is a strong AI tell. Resist it.

Banned shapes:

- ✗ Invented day-counts: "around day 11"
- ✗ Invented percentages: "improved by 47%"
- ✗ Invented streaks: "on the seventh attempt"
- ✗ Invented timeframes: "within 18 months"

### Metaphorical verbs where a literal verb is clearer

Do not use a metaphorical verb when a literal one is equally compact and more accurate. The model defaults to fancy verbs to add texture; pick the verb a person would use at the pub. Three sub-shapes, all banned:

**Dramatic metaphors for ordinary failure:**

- ✗ "Every system DIES around day 11." → "fails" / "stops working" / "breaks down"
- ✗ "collapses" → "stops working"
- ✗ "evaporates" → "fades"

**Soft metaphors for ordinary actions:**

- ✗ "leaking into inbox triage" → "being wasted on inbox triage"
- ✗ "siphoning attention" → "stealing attention" / "distracting"
- ✗ "dovetails into" → "connects to" / "leads to"
- ✗ "percolates through" → "spreads through" / "reaches"

**The "lands / settles" delivery-verb tic:**

- ✗ "The point lands cleanly." / "It settles for the reader." / "The argument resonates."
- DO NOT replace with another fancy substitute. "Settles," "hits home," "registers," "resonates" are equally AI-coded.
- ✓ Use a normal verb: "The point works." / "The reader sees it." / "By the end of the section, you understand X."

**Test:** would a careful editor swap this for the literal verb without losing meaning? If yes, swap it. The metaphorical verb is acceptable only when the metaphor is doing real cognitive work the literal verb can't (rare).

### Breezed-past curiosity beats

Do not introduce a curiosity-loaded phrase and then move on without amplifying it. The pattern: a sentence raises an unexpected or surprising claim ("they all fail at the same point" / "the answer is the opposite of what you'd expect"), but the prose doesn't lean INTO that surprise. It doesn't name how unusual the claim is, doesn't dwell on the implication, just glides past.

If you raise a curiosity beat, **commit to it**: name how unexpected, unusual, or counter-intuitive it is, leverage the curiosity for the rest of the paragraph. If you can't commit, **remove the phrase**.

### Present-tense overuse

Default to past or future tense, not present. The model defaults to present tense for narration. This is wrong. Past or future tense are the defaults, context-dependent:

- **Past tense** — when describing something the reader or speaker has experienced.
  - ✗ "You hit 4pm and your brain shuts down."
  - ✓ "Have you ever hit 4pm and found your brain shut down?"
- **Future tense** — when describing what the reader will experience after applying the content.
  - ✗ "By Thursday afternoon, your phone migrates back to your desk."
  - ✓ "By Thursday afternoon, your phone will have migrated back to your desk."
- **Present tense** — only when the speaker is describing something they currently do, OR when present is genuinely the natural register (teaching a generalisation: "your brain runs on glucose" is correct present-tense generalisation).

**Diagnostic:** would the speaker actually say this in present tense out loud? If yes, keep. If they'd naturally say "I used to do X" or "you'll find that Y" — switch tense.

---

## 2. Formulaic openers (Tier A)

Do not open any piece, section, paragraph, or hook with these constructions or their variants:

- "In today's fast-paced world..."
- "In an age where..."
- "In a world where..."
- "More than ever before..."
- "At its core..."
- "Welcome to..."
- "Enter [AI / ChatGPT / the solution]..."

---

## 3. Formulaic closers (Tier A)

Do not announce conclusions. Competent writing lands without signposting.

- "In conclusion..."
- "In summary..."
- "Ultimately..."
- "To sum up..."
- "At the end of the day..."

---

## 4. Vocabulary (Tier B — avoid clustering)

Avoid the **type** of word, not just the examples shown. Single use can work; clustering is the failure.

**Grandiose nouns:** tapestry, landscape, realm, ecosystem, paradigm, synergy, framework, journey, tale, odyssey, testament, cornerstone, bedrock, hallmark, pillar, beacon, nexus, frontier, arena, fabric, treasure trove.

**Inflated adjectives:** robust, pivotal, crucial, vital, essential, significant, compelling, comprehensive, meticulous, innovative, transformative, groundbreaking, seamless, dynamic, multifaceted, intricate, rich, vibrant, ever-evolving, cutting-edge, paramount, unparalleled, nuanced, profound, staggering, breathtaking, daunting, bustling.

**Magic adverbs:** quietly, deeply, fundamentally, remarkably, arguably, notably, significantly, profoundly, inherently, undoubtedly, essentially, ultimately, invariably, seamlessly, effortlessly.

**Pompous verbs (incl. corporate-motivational subset — the worst offenders):** delve, unpack, navigate, harness, leverage, utilize, optimize, facilitate, foster, cultivate, embark, revolutionize, elevate, empower, unlock, transform, accelerate, streamline, spearhead, grapple, pivot, showcase, underscore, highlight, captivate, resonate, illuminate, amplify, galvanize, catalyze, transcend, embody, epitomize, curate, endeavour, alleviate, reverberate.

**The "serves as" family** — use "is" / "are" instead of: serves as, stands as, represents, marks, embodies, constitutes, functions as, operates as, emerges as.

- "The building serves as the headquarters." → "The building is the headquarters."

---

## 5. Structural patterns (Tier B)

**Over-uniformity of sentence length** — no three consecutive sentences should be similar in length. Mix short punches (3 to 5 words) with longer flowing sentences. Uniform 12-to-20-word sentences read as AI even when each is fine in isolation.

**Over-uniformity of paragraph length** — vary paragraph length. A one-sentence paragraph surrounded by longer ones creates emphasis. Every paragraph being three to four sentences is a strong AI signal.

**Fractal summaries** — do not summarise subsections, then sections, then the whole. Do not announce what's about to be said, then say it, then summarise what was just said.

**One-point dilution** — do not restate a single argument in eight different ways with different metaphors. An 800-word point should not become 4,000 words of rephrased repetition.

**Dead metaphor** — do not latch onto one metaphor and repeat it throughout. Introduce, use, move on.

**Historical analogy stacking** — do not rapid-fire list historical companies or tech revolutions to borrow authority. ("Apple didn't build Uber. Facebook didn't build Spotify. Stripe didn't build Shopify.") Feels smart, means nothing.

**Listicle in a trench coat** — do not disguise numbered lists as continuous prose via "The first... The second... The third..."

**Content duplication** — do not repeat entire paragraphs or ideas verbatim within the same piece.

**Fragment-paragraph spam** — do not use one-word or fragment "paragraphs" for manufactured emphasis. ("Platforms do." / "He published this. Openly. In a book. As a priest.") is an AI cadence, not a human one.

**Synonym cycling** — once a term is established, keep using it. Do not rotate between synonyms for style points ("the agent reviews the draft, the assistant scores the piece, the tool suggests fixes" — that's one thing being called three names). Repetition of the correct word is clearer than variety for its own sake, and it's also easier to say out loud without tripping over an unfamiliar synonym mid-take.

---

## 6. Formatting tics (Tier B)

**Em-dash addiction** — a human writer uses 2 to 3 em dashes per piece. AI uses 20+. Avoid em dashes except where they are clearly the correct choice. Prefer commas, parentheses, or a full stop.

**Bold-first bullets** — do not begin every bullet with a bolded phrase plus colon. ("**Security:** Environment-based configuration..." / "**Performance:** Lazy loading...")

**Unicode decoration** — do not use unicode arrows (→, ⇒), curly or smart quotes, or decorative unicode. Use straight quotes and standard punctuation.

**Emoji sprinkling** — do not insert emojis at the end of sentences for tone unless explicitly requested.

**Heavy markdown in prose** — do not inject H2s, H3s, or numbered lists into flowing prose where standard paragraphs would serve.

---

## Two-tier enforcement

**Tier A (§1, §2, §3) — zero exceptions.** These are pure AI tells with no human upside. Zero instances. The "used once with clear intent" exception below does NOT apply to Tier A. If any Tier A pattern appears in any form — declarative, imperative, second-person, third-person, plural, singular, or rhetorical — rewrite the line. "I only used it once" is not a defence.

**Tier B (§4, §5, §6) — avoid clustering.** Any single one of these patterns, used once with clear intent, can work. The failure mode is clustering: multiple tics compounding in the same piece, or one tic repeated across a piece. Aim for varied, specific, imperfect human writing. When in doubt, be more concrete and less elaborate. Do NOT over-correct into stilted prose with zero rhythm or analogy — humans use em-dashes, tricolons, and analogies; AI overuses them.

---

## Self-check — two passes before returning any prose

**Pass 1 (Tier A):** scan your output for any §1 rhetorical pattern, §2 formulaic opener, or §3 formulaic closer. If any are present, rewrite the line. Non-negotiable, zero instances. The patterns that slip through most often: NEGATIVE PARALLELISM (especially the period-separated and disguised-reframe variants), ANAPHORA (3+ identical sentence openers), DECORATIVE LISTS (three-comma scene-painting), PATRONISING ANALOGY (even one is too many), PHANTOM-FUTURE PROJECTION, FALSE SUSPENSE TRANSITIONS ("Here's..." including the colon-reveal variant — confirmed in live testing as one of the two most commonly missed patterns), TRIPLE COUNTDOWN ("Not X. Not Y. Just Z." — confirmed in live testing as the other).

**Pass 2 (Tier B):** scan for clustering of §4 vocabulary, §5 structural patterns, or §6 formatting tics. If clustering is present, rewrite. Single isolated instances are acceptable. Both passes are required, not optional.
