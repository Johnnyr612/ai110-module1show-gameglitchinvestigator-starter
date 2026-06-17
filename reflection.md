# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game UI looked pretty confusing, the debug tools is at the top for some reason and is kinda bugy.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
I noticed the hints aren't give accurate hints that lead to the secrete number.
The 'new game' button doesn't actually restart the game, I have to actually refresh the page.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 20    |  Go Higher        | Go Lower        | None
| 10    |  Go Higher        | Go Lower        | None
| 5     |  Go higher        | Go Lower        | None

Kept giving me 'keep going lower' hints as I was inputing lower ones while the real secret number was 59 all along :|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude to tell me the step-by-step logic of the app.py and logic_utils.py files. I then asked it to fix the issues i found in section 1 and to also add pytest cases inside 'test_game_logic.py'.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I used claude to help me fix the hint directions and after review, it checked out with me and the pytest.(It was correct and I verified it)
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I dont believe the ai chat bot was incorrect with the prompts I gave it. I was pretty clear on what I wanted the bot to fix and it checked out with me.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
