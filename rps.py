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
  if move == ("rock"):
    return "paper"
  elif move == ("paper"):
    return "scissors"
  elif move == ("scissors"):
    return "rock"


# ---------- score one round: YOU WRITE THIS ----------


def score(player, computer):
 player_wins = 0
 computer_wins = 0

 if player == computer:
  return 0

 elif (player == "rock" and computer == "scissors"
    or player == "paper" and computer == "rock"
    or player == "scissor" and computer == "rock" ):
   return 1
 else:
   return -1


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
 if round_number == 1 or last_computer_move is None:
   return "rock"

   if round_number == 2 or last_computer_move == "rock":
     return "paper"
   elif round_number == 3 or last_computer_move == "paper":
     return "scissors"
   elif round_number == 4 or last_computer_move == "scissors"
     return "rock"


# --- YOU WRITE THIS strategy ---


def expect_change(round_number, last_computer_move):
    
  if last_computer_move is None:
   return random_move()

  if last_computer_move == "rock":
    if random.randint(1, 2) == 1:
      return "scissors"
  else:
      return "paper"

  if last_computer_move == "paper":
    if random.randint(1, 2) == 1:
     return "rock"
  else:
     return "scissors"

  if last_computer_move == "scissors":
    if random.randint(1, 2) == 1:
     return "paper"
    else:
      return "rock"


# ---------- the tournament: YOU WRITE THIS ----------
# Play one strategy against one opponent for `num_rounds` rounds and return the
# total score. Each side sees the other's move from the previous round, so
# start both "last move" variables at None and update them each round.

def always_rock(prev_opponent_move):
  return "rock"

def copycat_strategy(prev_opponent_move):
  if prev_opponent_move is None:
    return random.choice(["rock","paper","scissors"])
  return prev_opponent_move


def play_rounds(strategy, opponent, num_rounds):
  stra_score = 0 
  prev_strategy_move = None 
  prev_opponent_move = None

  for _ in range(num_rounds):

    move1 = strategy(prev_opponent_move)
    move2 = opponent(prev_strategy_move)

    prev_strategy_move = move1 
    prev_opponent_move = move2

    if move1 == move2:
       stra_score += 1 
    elif (move1 == "rock" and move2 == "scissors") or\
          (move1 == "paper" and move2 == "rock") or\
          (move1 == "scissors" and move2 == "paper"):

          stra_score += 3

  return stra_score

  total_score = play_rounds(copycat_strategy, always_rock, nums_round=10)
  print(f"Total strategy score after 10 rounds: {total_score}")
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
