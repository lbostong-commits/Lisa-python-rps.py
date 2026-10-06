# ============================================================
# YOUR JOB: complete the five functions marked "# your code here":
#   beat, score, beat_last, expect_change, and play_rounds.
# Do not change the other functions.
# See README.md for details and how it is graded.
# ============================================================

import random

# ---------- (do not change) ----------


def random_move():
    n = random.randint(1, 3)
    if n == 1:
        return "rock"
    elif n == 2:
        return "paper"
    else:
        return "scissors"


def winner(player, computer):
    if player == computer:
        return "tie"
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "player"
    else:
        return "computer"


def play(player):
    computer = random_move()
    print("You chose:     ", player)
    print("Computer chose:", computer)

    result = winner(player, computer)
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win!")
    else:
        print("Computer wins!")


def validate_input(player):
    if player == "rock" or player == "paper" or player == "scissors":
        return True
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")
        return False


# ---------- helper: YOU WRITE THIS ----------


def beat(move):
    # move is a string: "rock", "paper", or "scissors"
    # Return the move that beats `move`.
    # For example, beat("rock") should return "paper".
    # your code here (make sure to remove `pass` when you write your code)
    pass


# ---------- score one round: YOU WRITE THIS ----------


def score(player, computer):
    # player is a string: "rock", "paper", or "scissors"
    # computer is a string: "rock", "paper", or "scissors"
    # Return 1 if the player wins, -1 if the player loses, 0 for a tie.
    # Hint: use winner(player, computer).
    # your code here (make sure to remove `pass` when you write your code)
    pass


# ---------- strategies ----------
# A strategy takes the round number and the computer's last move, and returns
# "rock", "paper", or "scissors". last_computer_move is None in round 1.

# --- example strategies (provided, study these) ---


def always_rock(round_number, last_computer_move):
    return "rock"


def play_random(round_number, last_computer_move):
    return random_move()


def cycle(round_number, last_computer_move):
    # Used as an OPPONENT. Plays rock, scissors, paper, in order, then repeats.
    remainder = round_number % 3
    if remainder == 1:
        return "rock"
    elif remainder == 2:
        return "scissors"
    else:
        return "paper"


def by_round(round_number, last_computer_move):
    if round_number % 2 == 0:
        if random.randint(1, 2) == 1:
            return "rock"
        else:
            return "paper"
    else:
        if random.randint(1, 2) == 1:
            return "paper"
        else:
            return "scissors"


# --- YOU WRITE THIS strategy ---


def beat_last(round_number, last_computer_move):
    # round_number is an integer: 1, 2, 3, ... (the current round)
    # last_computer_move is a string: "rock", "paper", or "scissors" (the computer's move in the previous round)
    # Play the move that beats the computer's last move.
    # In round 1 there is no last move (it is None), so play "rock".
    # your code here (make sure to remove `pass` when you write your code)
    pass


# --- YOU WRITE THIS strategy ---


def expect_change(round_number, last_computer_move):
    # Assume the computer will NOT repeat its last move, so it will play one
    # of the other two moves. You cannot cover both, so choose randomly
    # between the two moves that beat those two options.
    # Example: if the computer last played "rock", it will probably play
    # "paper" or "scissors" next. "scissors" beats paper and "rock" beats
    # scissors, so return "scissors" or "rock", chosen at random.
    # In round 1 last_computer_move is None, so return any random move
    # (you can use random_move()).
    # Hint: branch on last_computer_move and use random.randint(1, 2) to
    # choose between the two moves, the same randint pattern by_round uses.
    # your code here (make sure to remove `pass` when you write your code)
    pass


# ---------- the tournament: YOU WRITE THIS ----------
# Play one strategy against one opponent for `num_rounds` rounds and return the
# total score. Each side sees the other's move from the previous round, so
# start both "last move" variables at None and update them each round.


def play_rounds(strategy, opponent, num_rounds):
    # your code here
    pass


# ---------- the analysis ----------
# Once your functions are written, run this file to see the tournament.
# It prints the average score per round for each strategy against three
# opponents.

if __name__ == "__main__":
    num_rounds = 10000

    def report(title, opponent):
        print(title)
        print(
            "  always_rock:  ",
            round(play_rounds(always_rock, opponent, num_rounds) / num_rounds, 3),
        )
        print(
            "  play_random:  ",
            round(play_rounds(play_random, opponent, num_rounds) / num_rounds, 3),
        )
        print(
            "  beat_last:    ",
            round(play_rounds(beat_last, opponent, num_rounds) / num_rounds, 3),
        )
        print(
            "  expect_change:",
            round(play_rounds(expect_change, opponent, num_rounds) / num_rounds, 3),
        )
        print(
            "  by_round:     ",
            round(play_rounds(by_round, opponent, num_rounds) / num_rounds, 3),
        )
        print()

    print("average score per round over", num_rounds, "rounds")
    print()
    report("against a RANDOM opponent:", play_random)
    report("against an opponent that ALWAYS plays rock:", always_rock)
    report("against an opponent that plays ROCK, SCISSORS, PAPER in order:", cycle)
