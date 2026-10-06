# Visible tests. Run with:  pytest test_rps.py
# These show the contract for each function you write. Passing them does not
# guarantee full credit: hidden tests check more cases.

from rps import always_rock, beat, beat_last, expect_change, play_rounds, score


# a simple opponent the tests use
def always_paper(round_number, last_computer_move):
    return "paper"


# ---------- beat ----------


def test_beat_rock():
    assert beat("rock") == "paper"


# ---------- score ----------


def test_score_win():
    assert score("rock", "scissors") == 1


def test_score_loss():
    assert score("rock", "paper") == -1


def test_score_tie():
    assert score("rock", "rock") == 0


# ---------- beat_last ----------


def test_beat_last_round_one():
    assert beat_last(1, None) == "rock"


def test_beat_last_after_rock():
    assert beat_last(2, "rock") == "paper"


# ---------- play_rounds ----------
# Use strategies that ignore history on both sides, so the result is exact.


def test_play_rounds_all_ties():
    # rock vs rock every round: score 0 each round
    assert play_rounds(always_rock, always_rock, 100) == 0


def test_play_rounds_all_wins():
    # paper beats rock every round: +1 each round
    assert play_rounds(always_paper, always_rock, 100) == 100


# ---------- expect_change ----------


def test_expect_change_after_rock():
    m = expect_change(2, "rock")
    assert m == "scissors" or m == "rock"
