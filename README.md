# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The games purpose is to guess the random secret number ranging from 1-100 or depending on the dificulty.
- [ ] Detail which bugs you found.
Two bugs I found include wrong hint direction and 'restart' button malfunction.
- [ ] Explain what fixes you applied.
I fixed the logic for the hint direction outputs inside check_guess() method
```
if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"
```
I also fixed the stremlit issue when pressing the restart game button.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. I enter 40 in the guess box
2. Game returns "Go Higher"
3. I enter 55 in the guess box
4. Game returns "Go Lower"
5. I enter 50 in the guess box
6. Game returns "Go Lower"
7. I enter 45 in the guess box
8. Game return "Go Lower"
9. I enter 42 in the guess box
10. Game returns Correct! you won!

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
PS D:\CodePath Forks\Week3-Project1\ai110-module1show-gameglitchinvestigator-starter> python -m pytest tests/test_game_logic.py
=========================== test session starts ==============================================================================
platform win32 -- Python 3.13.3, pytest-9.1.0, pluggy-1.6.0
rootdir: D:\CodePath Forks\Week3-Project1\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.12.1, langsmith-0.7.3
collected 13 items                                                                                                                                                              

tests\test_game_logic.py .............                                                                                                                                    [100%]

=========================== 13 passed in 0.19s ==============================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
