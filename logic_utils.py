import json
import random

HIGH_SCORE_FILE = "high_scores.json"

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def get_attempt_limit(difficulty: str):
    """Return the number of attempts allowed for a given difficulty."""
    attempt_limit_map = {
        "Easy": 6,
        "Normal": 8,
        "Hard": 5,
    }
    return attempt_limit_map.get(difficulty, 8)


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def create_new_game_state(low: int, high: int):
    """Return a fresh state dictionary for a new game."""
    return {
        "secret": random.randint(low, high),
        "attempts": 1,
        "score": 0,
        "status": "playing",
        "history": [],
    }


def load_high_scores(path: str = HIGH_SCORE_FILE):
    """
    Load the best-score-per-difficulty map from disk.

    Returns an empty dict if the file is missing, unreadable, or corrupt,
    so a fresh install (or a bad file) never crashes the game.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}

    if not isinstance(data, dict):
        return {}
    return data


def update_high_score(scores: dict, difficulty: str, score: int):
    """
    Return (updated_scores, is_new_record).

    A new record is set when there is no prior score for the difficulty
    or the new score is strictly higher than the existing best. The input
    dict is not mutated.
    """
    updated = dict(scores)
    previous = updated.get(difficulty)
    if previous is None or score > previous:
        updated[difficulty] = score
        return updated, True
    return updated, False


def save_high_scores(scores: dict, path: str = HIGH_SCORE_FILE):
    """Persist the best-score-per-difficulty map to disk as JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2)
