# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

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
| Negative number (`"-50"`) | (see prompt above) | `test_negative_number_is_accepted_but_out_of_range` | ✅ Yes | A negative guess is parsed as valid even though the secret is always 1-100, so it can never be a real answer — exposes missing range validation. |
| Decimal (`"50.99"`) | (see prompt above) | `test_decimal_input_is_truncated_not_rounded` | ✅ Yes | `int(float("50.99"))` truncates to 50 instead of rounding to 51, so the player's actual guess silently differs from what they typed. |
| Extremely large value (`"99999999999999999999"`) | (see prompt above) | `test_extremely_large_value_does_not_crash` | ✅ Yes | Python ints are unbounded, so a giant value must not overflow or crash — it should just be handled gracefully as "Too High". |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
