from logic_utils import (
    check_guess,
    create_new_game_state,
    load_high_scores,
    parse_guess,
    save_high_scores,
    update_high_score,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_create_new_game_state_resets_values():
    # Regression test for the new game button reset behavior.
    state = create_new_game_state(1, 100)

    assert 1 <= state["secret"] <= 100
    assert state["attempts"] == 1
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []


# --- Edge case tests ---------------------------------------------------------

def test_negative_number_is_accepted_but_out_of_range():
    # Edge case: a negative guess is parsed successfully even though no valid
    # secret (1-100) can ever be negative, so it is always "Too Low".
    ok, value, error = parse_guess("-50")
    assert ok is True
    assert value == -50
    assert error is None

    outcome, _ = check_guess(value, 50)
    assert outcome == "Too Low"


def test_decimal_input_is_truncated_not_rounded():
    # Edge case: "50.99" looks like it should round to 51, but parse_guess
    # truncates to 50, which can mislead the player about their real guess.
    ok, value, error = parse_guess("50.99")
    assert ok is True
    assert value == 50  # truncated, NOT 51
    assert error is None


def test_extremely_large_value_does_not_crash():
    # Edge case: Python ints have no max size, so a huge value is accepted and
    # must still be handled gracefully as "Too High" rather than overflowing.
    ok, value, error = parse_guess("99999999999999999999")
    assert ok is True
    assert value == 99999999999999999999
    assert error is None

    outcome, _ = check_guess(value, 50)
    assert outcome == "Too High"


# --- High score tracker tests ------------------------------------------------

def test_update_high_score_sets_first_record():
    # With no prior score for the difficulty, any score is a new record.
    scores, is_record = update_high_score({}, "Normal", 50)
    assert is_record is True
    assert scores["Normal"] == 50


def test_update_high_score_only_beats_strictly_higher():
    # An equal or lower score must NOT overwrite the existing best.
    scores, is_record = update_high_score({"Normal": 80}, "Normal", 80)
    assert is_record is False
    assert scores["Normal"] == 80


def test_update_high_score_does_not_mutate_input():
    # Pure function: the original dict stays untouched.
    original = {"Hard": 30}
    update_high_score(original, "Hard", 99)
    assert original == {"Hard": 30}


def test_save_and_load_high_scores_round_trip(tmp_path):
    # Saving then loading should return the same data (file persistence).
    path = str(tmp_path / "scores.json")
    save_high_scores({"Easy": 90, "Hard": 40}, path)
    assert load_high_scores(path) == {"Easy": 90, "Hard": 40}


def test_load_high_scores_missing_file_returns_empty(tmp_path):
    # A fresh install has no file yet — this must not crash.
    path = str(tmp_path / "does_not_exist.json")
    assert load_high_scores(path) == {}


def test_load_high_scores_corrupt_file_returns_empty(tmp_path):
    # A garbled file should degrade gracefully to an empty map.
    path = tmp_path / "corrupt.json"
    path.write_text("not valid json {{{", encoding="utf-8")
    assert load_high_scores(str(path)) == {}
