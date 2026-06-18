# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

## Agent Workflow

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

> Plan and implement a meaningful new feature — a "High Score" tracker that
> saves your best score to a file — then document the work.

**What did the agent do?**

Files modified:

**`logic_utils.py`** — added a `HIGH_SCORE_FILE` constant and three new
functions: `load_high_scores()` (reads the JSON file, returns `{}` if it is
missing or corrupt), `update_high_score()` (pure function returning the
updated map plus an `is_new_record` flag), and `save_high_scores()` (writes
the map to disk as JSON).

**`app.py`** — imported the new functions, added a `st.sidebar.metric`
showing the best score for the selected difficulty, and updated the win
handler to load → update → save the high score and announce new records.

**`tests/test_game_logic.py`** — added 6 pytest cases covering first-record
detection, the strictly-higher rule, no input mutation, a save/load file
round-trip (via `tmp_path`), a missing file, and a corrupt file.

**`.gitignore`** — added `high_scores.json` so the runtime data file is not
committed.

The agent tracked the best score **per difficulty** (Easy/Normal/Hard) since
each difficulty scores differently, and ran `pytest` to confirm all 13 tests
pass.

**What did you have to verify or fix manually?**

The agent ran `python -m pytest tests/test_game_logic.py -v` and all 13 tests
passed. I still need to launch `python -m streamlit run app.py` to confirm the
sidebar "Best score" metric shows and updates after a win. I reviewed the
high-score logic and agreed the "strictly higher" rule (an equal score is not a
new record) is the behavior I wanted.

## Test Generation

> Document how you used AI to help generate or improve tests.

**Prompt(s) used to generate the tests:**

```
Identify three potential "edge case" inputs (negative numbers, decimals, or
extremely large values) that might still break my number guessing game, then
write a pytest case for each against parse_guess() and check_guess() in
logic_utils.py.
```

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Why this edge case was chosen |
|-----------|-------------|-------------------|--------------|----------------|
| Negative number (`"-50"`) | (see prompt above) | `test_negative_number_is_accepted_but_out_of_range` | Yes | A negative guess is parsed as valid even though the secret is always 1-100, so it can never be a real answer — exposes missing range validation. |
| Decimal (`"50.99"`) | (see prompt above) | `test_decimal_input_is_truncated_not_rounded` | Yes | `int(float("50.99"))` truncates to 50 instead of rounding to 51, so the player's actual guess silently differs from what they typed. |
| Extremely large value (`"99999999999999999999"`) | (see prompt above) | `test_extremely_large_value_does_not_crash` | Yes | Python ints are unbounded, so a giant value must not overflow or crash — it should just be handled gracefully as "Too High". |

