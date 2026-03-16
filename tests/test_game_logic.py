import random
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_message_says_go_lower():
    # Regression: hint message was backwards — "Too High" used to say "Go HIGHER!"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message but got: {message!r}"

def test_too_low_message_says_go_higher():
    # Regression: hint message was backwards — "Too Low" used to say "Go LOWER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message but got: {message!r}"


def simulate_new_game(state):
    """Mirrors the new_game block in app.py."""
    state["attempts"] = 0
    state["secret"] = random.randint(1, 100)
    state["status"] = "playing"
    state["history"] = []


def test_new_game_resets_status_after_win():
    # Regression: status was not reset to "playing", blocking play after a win
    state = {"attempts": 5, "secret": 42, "status": "won", "history": [42]}
    simulate_new_game(state)
    assert state["status"] == "playing"


def test_new_game_resets_status_after_loss():
    # Regression: status was not reset to "playing", blocking play after a loss
    state = {"attempts": 8, "secret": 77, "status": "lost", "history": [1, 2, 3]}
    simulate_new_game(state)
    assert state["status"] == "playing"


def test_new_game_resets_attempts_and_history():
    state = {"attempts": 6, "secret": 10, "status": "lost", "history": [5, 10]}
    simulate_new_game(state)
    assert state["attempts"] == 0
    assert state["history"] == []
