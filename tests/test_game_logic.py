from logic_utils import check_guess, create_new_game_state, parse_guess

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
