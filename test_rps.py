# Visible tests. Run with:  pytest test_rps.py
# These show the contract for each function you write. Passing them does not
# guarantee full credit: hidden tests check more cases.

from rps import always_rock, beat, beat_last, expect_change, play_rounds, score

def beat(move):
  if move == ("rock"):
    return "paper"
  elif move == ("paper"):
    return "scissors"
  elif move == ("scissors"):
    return "rock"

def score(player, computer):
 player_wins = 0
 computer_wins = 0

 if player == computer:
  return 0

 elif (player == "rock" and computer == "scissors"
    or player == "paper" and computer == "rock"
    or player == "scissor" and computer == "paper" ):
   return 1
 else:
   return -1


def beat_last(round_number, last_computer_move)
 if round_number == 1 or last_computer_move is None:
   return "rock"

   if round_number == 2 or last_computer_move == "rock":
     return "paper"
   elif round_number == 3 or last_computer_move == "paper":
     return "scissors"
   elif round_number == 4 or last_computer_move == "scissors"
     return "rock"



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



import random
BEATS = {"rock": "paper", "paper": "scissors", "scissors":"rock"}

def always_rock(prev_opponent_move):
  return "rock"

def play_random(prev_opponent_move):
    return random.choice(["rock","paper","scissors"])


def copycat_strategy(prev_opponent_move):
  if prev_opponent_move is None:
      return random.choice(["rock","paper","scissors"])
  return prev_opponent_move


def beat_last(prev_opponent_move):
  if prev_opponent_move is None:
    return random.choice(["rock", "paper", "scissors"])
  return BEATS[prev_opponent_move]

def expect_change(prev_opponent_move):
  if prev_opponent_move is None:
    return random.choice (["rock", "paper", "scissors"])

  options = ["rock", "paper", "scissors"]
  options.remove(prev_opponent_move)
  predicted_next = random.choice(options)
  return BEATS[predicted_next]

def cycle(prev_opponent_move):
  if prev_opponent_move is None:
    cycle.index = 0
  moves = ["rock", "scissors", "paper"]
  move = moves[cycle.index % 3]
  cycle.index += 1
  return move

def by_round(prev_opponent_move):
  if prev_opponent_move is None:
    by_round.round_num = 0
  by_round.round_num += 1
  moves = ["rock", "paper", "scissors"]
  return moves[by_round.round_num % 3]

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

  total_score = play_rounds(copycat_strategy, always_rock, num_rounds=10)
  print("Total strategy score after 10 rounds:",total_score)
  print()
    
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
