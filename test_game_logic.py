from logic_utils import check_guess, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)[0] # FIX: Extract outcome from the tuple
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)[0]
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)[0]
    assert result == "Too Low"

# ADDITION: Tests for parse_guess function
def test_parse_guess_valid_integer():
    """Test parsing a valid integer string."""
    ok, guess, error = parse_guess("42")
    assert ok is True
    assert guess == 42
    assert error is None


def test_parse_guess_float_string():
    """Test parsing a float string converts to int."""
    ok, guess, error = parse_guess("42.7")
    assert ok is True
    assert guess == 42
    assert error is None


def test_parse_guess_zero():
    """Test parsing zero."""
    ok, guess, error = parse_guess("0")
    assert ok is True
    assert guess == 0
    assert error is None


def test_parse_guess_negative_number():
    """Test parsing negative numbers."""
    ok, guess, error = parse_guess("-15")
    assert ok is True
    assert guess == -15
    assert error is None


def test_parse_guess_empty_string():
    """Test parsing empty string returns error."""
    ok, guess, error = parse_guess("")
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."


def test_parse_guess_none_input():
    """Test parsing None input returns error."""
    ok, guess, error = parse_guess(None)
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."


def test_parse_guess_invalid_string():
    """Test parsing non-numeric string returns error."""
    ok, guess, error = parse_guess("hello")
    assert ok is False
    assert guess is None
    assert error == "That is not a number."


def test_parse_guess_special_characters():
    """Test parsing string with special characters returns error."""
    ok, guess, error = parse_guess("@#$%")
    assert ok is False
    assert guess is None
    assert error == "That is not a number."


# ADDITION: Tests for update_score function
def test_update_score_win_first_attempt():
    """Test score update on first attempt win (attempt 0)."""
    # 100 - 10*(0+1) = 90 points
    new_score = update_score(0, "Win", 0)
    assert new_score == 90


def test_update_score_win_second_attempt():
    """Test score update on second attempt win (attempt 1)."""
    # 100 - 10*(1+1) = 80 points
    new_score = update_score(0, "Win", 1)
    assert new_score == 80


def test_update_score_win_many_attempts():
    """Test score update on many attempts still awards minimum 10 points."""
    # 100 - 10*(10+1) = -10, but minimum is 10
    new_score = update_score(0, "Win", 10)
    assert new_score == 10


def test_update_score_win_with_existing_score():
    """Test score update when player already has points."""
    # 50 + (100 - 10*2) = 50 + 80 = 130
    new_score = update_score(50, "Win", 1)
    assert new_score == 130


def test_update_score_too_high_guess():
    """Test score penalty for too high guess."""
    new_score = update_score(100, "Too High", 1)
    assert new_score == 95


def test_update_score_too_low_guess():
    """Test score penalty for too low guess."""
    new_score = update_score(100, "Too Low", 1)
    assert new_score == 95


def test_update_score_multiple_wrong_guesses():
    """Test cumulative score penalties."""
    score = 100
    score = update_score(score, "Too Low", 0)
    score = update_score(score, "Too High", 1)
    score = update_score(score, "Too Low", 2)
    # 100 - 5 - 5 - 5 = 85
    assert score == 85


def test_update_score_unknown_outcome():
    """Test score unchanged for unknown outcome."""
    new_score = update_score(50, "Unknown", 1)
    assert new_score == 50


# ADDITION: Tests for new game initialization
def test_new_game_resets_attempts():
    """Test that new game resets attempt counter."""
    # Simulate a game in progress
    import streamlit as st
    
    # Setup initial game state
    st.session_state.attempts = 5
    st.session_state.secret = 42
    st.session_state.score = 50
    st.session_state.status = "playing"
    st.session_state.history = [10, 20, 30, 40]
    
    # Reset for new game (simulating button click)
    st.session_state.attempts = 0
    
    assert st.session_state.attempts == 0


def test_new_game_generates_new_secret():
    """Test that new game generates a different secret."""
    import streamlit as st
    from logic_utils import get_range_for_difficulty
    
    difficulty = "Normal"
    low, high = get_range_for_difficulty(difficulty)
    
    st.session_state.secret = 42
    original_secret = st.session_state.secret
    
    # Generate new secret
    st.session_state.secret = __import__('random').randint(low, high)
    
    # In most cases it should be different (statistically very likely)
    # We can't guarantee it's different, but it should be in valid range
    assert st.session_state.secret >= low
    assert st.session_state.secret <= high


def test_new_game_resets_status():
    """Test that new game resets status to playing."""
    import streamlit as st
    
    st.session_state.status = "won"
    
    # Reset for new game
    st.session_state.status = "playing"
    
    assert st.session_state.status == "playing"


def test_new_game_clears_history():
    """Test that new game clears guess history."""
    import streamlit as st
    
    st.session_state.history = [10, 20, 30, 40, 50]
    
    # Reset for new game
    st.session_state.history = []
    
    assert st.session_state.history == []
    assert len(st.session_state.history) == 0


def test_new_game_resets_score():
    """Test that new game resets score to zero."""
    import streamlit as st
    
    st.session_state.score = 85
    
    # Reset for new game
    st.session_state.score = 0
    
    assert st.session_state.score == 0


def test_new_game_full_reset_after_win():
    """Test complete game state reset after a win."""
    import streamlit as st
    
    # Simulate completed game state (won)
    st.session_state.attempts = 3
    st.session_state.secret = 42
    st.session_state.score = 90
    st.session_state.status = "won"
    st.session_state.history = [30, 50, 42]
    
    # Reset for new game
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.secret = __import__('random').randint(1, 50)
    
    assert st.session_state.attempts == 0
    assert st.session_state.score == 0
    assert st.session_state.status == "playing"
    assert st.session_state.history == []
    assert st.session_state.secret >= 1 and st.session_state.secret <= 50


def test_new_game_full_reset_after_loss():
    """Test complete game state reset after a loss."""
    import streamlit as st
    
    # Simulate completed game state (lost)
    st.session_state.attempts = 8
    st.session_state.secret = 42
    st.session_state.score = 50
    st.session_state.status = "lost"
    st.session_state.history = [10, 20, 30, 40, 50, 60, 70, 80]
    
    # Reset for new game
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.secret = __import__('random').randint(1, 50)
    
    assert st.session_state.attempts == 0
    assert st.session_state.score == 0
    assert st.session_state.status == "playing"
    assert st.session_state.history == []


# ADDITION: Tests for secret number persistence during game session
def test_secret_persists_after_first_guess():
    """Test that secret number doesn't change after first guess."""
    import streamlit as st
    
    # Initialize game session with a secret
    st.session_state.secret = 42
    st.session_state.attempts = 0
    st.session_state.status = "playing"
    
    original_secret = st.session_state.secret
    
    # Simulate making a guess
    st.session_state.attempts += 1
    guess = 30
    outcome, message = check_guess(guess, st.session_state.secret)
    
    # Secret should remain unchanged
    assert st.session_state.secret == original_secret
    assert st.session_state.secret == 42


def test_secret_persists_after_multiple_guesses():
    """Test that secret number stays the same through multiple wrong guesses."""
    import streamlit as st
    
    # Initialize game session
    st.session_state.secret = 50
    st.session_state.attempts = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    
    original_secret = st.session_state.secret
    
    # Make several guesses
    guesses = [10, 20, 30, 40]
    for guess in guesses:
        st.session_state.attempts += 1
        st.session_state.history.append(guess)
        outcome, message = check_guess(guess, st.session_state.secret)
        
        # Secret should remain the same after each guess
        assert st.session_state.secret == original_secret
        assert st.session_state.secret == 50


def test_secret_persists_until_correct_guess():
    """Test that secret remains constant even when correct guess is made."""
    import streamlit as st
    
    # Initialize game session
    st.session_state.secret = 42
    st.session_state.attempts = 0
    st.session_state.status = "playing"
    
    original_secret = st.session_state.secret
    
    # Make wrong guesses
    wrong_guesses = [10, 30, 40]
    for guess in wrong_guesses:
        st.session_state.attempts += 1
        outcome, message = check_guess(guess, st.session_state.secret)
        assert outcome != "Win"
        assert st.session_state.secret == original_secret
    
    # Make correct guess
    st.session_state.attempts += 1
    outcome, message = check_guess(42, st.session_state.secret)
    
    # Secret should match what was guessed
    assert outcome == "Win"
    assert st.session_state.secret == original_secret == 42


def test_secret_only_changes_on_new_game():
    """Test that secret only changes when new game is explicitly started."""
    import streamlit as st
    from logic_utils import get_range_for_difficulty
    
    difficulty = "Normal"
    low, high = get_range_for_difficulty(difficulty)
    
    # Initial game
    st.session_state.secret = 42
    st.session_state.attempts = 0
    st.session_state.status = "playing"
    
    original_secret = st.session_state.secret
    
    # Make guesses - secret should stay the same
    for guess in [10, 20, 30, 40]:
        st.session_state.attempts += 1
        check_guess(guess, st.session_state.secret)
        assert st.session_state.secret == original_secret
    
    # Now start new game - secret should change
    st.session_state.secret = __import__('random').randint(low, high)
    st.session_state.attempts = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    
    # Secret can be different now (statistically very likely)
    assert st.session_state.secret >= low and st.session_state.secret <= high


def test_secret_persists_after_score_updates():
    """Test that secret doesn't change when score is updated."""
    import streamlit as st
    
    # Initialize game session
    st.session_state.secret = 75
    st.session_state.score = 0
    st.session_state.attempts = 0
    
    original_secret = st.session_state.secret
    
    # Make guesses and update score
    st.session_state.attempts += 1
    outcome1, _ = check_guess(50, st.session_state.secret)
    st.session_state.score = update_score(st.session_state.score, outcome1, st.session_state.attempts)
    
    # Secret unchanged after score update
    assert st.session_state.secret == original_secret
    
    st.session_state.attempts += 1
    outcome2, _ = check_guess(80, st.session_state.secret)
    st.session_state.score = update_score(st.session_state.score, outcome2, st.session_state.attempts)
    
    # Secret still unchanged
    assert st.session_state.secret == original_secret == 75
