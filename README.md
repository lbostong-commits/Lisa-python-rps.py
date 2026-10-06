# Rock, Paper, Scissors: Strategy Lab

In this project you write and test strategies for Rock, Paper, Scissors, then run a small tournament to see which strategies beat which opponents.

You will use only variables, functions, conditionals, `for` loops, and `while` loops. You do not need lists.

## A strategy is a function

A strategy takes the round number and the computer's last move, and returns `"rock"`, `"paper"`, or `"scissors"`:

```python
def always_rock(round_number, last_computer_move):
    return "rock"
```

Note that this strategy, `always_rock`,  ignores both of its parameters. Every strategy takes the same two parameters whether it uses them or not, so `play_rounds` can call any strategy the same way.

When a strategy does use `last_computer_move`, remember that it is `None` in round 1, since no move has been played yet, so your strategy has to handle that case.

## Provided for you

`rps.py` already contains:

- `random_move()`, `winner(player, computer)`, `play(player)`, and `validate_input(move)` from class.
- Three example strategies to study: `always_rock`, `play_random`, and `by_round`.
- An opponent, `cycle`, that plays rock, scissors, paper, in order, then repeats.

Do not change the provided functions.

## What you write

Fill in these five functions, each marked `# your code here`:

1. `beat(move)`: return the move that beats `move`. For example, `beat("rock")` is `"paper"`.
2. `score(player, computer)`: given the player's move and the computer's move (the same two moves that `winner` takes), return `1` if the player wins, `-1` if the player loses, and `0` for a tie.
3. `beat_last(round_number, last_computer_move)`: a strategy that plays the move which beats the computer's last move. In round 1, when there is no last move, play `"rock"`.
4. `expect_change(round_number, last_computer_move)`: a strategy that assumes the computer will not repeat its last move. Since it will play one of the other two moves, choose randomly between the two moves that beat those two. For example, if the computer last played `"rock"`, it will probably play `"paper"` or `"scissors"`, so play `"scissors"` (which beats paper) or `"rock"` (which beats scissors), chosen at random. In round 1, when there is no last move, play any random move.
5. `play_rounds(strategy, opponent, num_rounds)`: play `strategy` against `opponent` for `num_rounds` rounds and return the total score. Each round, each side sees the other side's move from the previous round.


## Run it

Run the file to see the tournament:

```
python rps.py
```

It prints the average score per round for each strategy against three opponents: a random opponent, an opponent that always plays rock, and one that cycles through rock, scissors, paper.

We report the average per round, not the total, because the average is stable from run to run while the total is not.

## Test it

The visible tests are in `test_rps.py`:

```
pytest test_rps.py
```

Note that in addition to passing the visible tests, your function will have to pass the hidden tests that verify you implemented the functions correctly.

## Explain your code

All of your code must be written on your own without the use of LLMs.

For each function you write, explain in your own words how it works, in a few sentences, in `writeup.md`. This is where most of the learning happens, so write it yourself. You should be able to explain any line of your code if asked. A function that passes the tests but that you cannot explain will not receive full credit.

You will also read the provided `by_round` strategy and explain, in your own words, how it works, even though you did not write it.

You may be asked to walk through your code in person, in class or in office hours. If you cannot explain how a submission you turned in works, it will not receive credit.

## The analysis

In `writeup.md`, paste the output of `python rps.py` and answer these questions:

1. Against the random opponent, how do the five strategies (`always_rock`, `play_random`, `beat_last`, `expect_change`, `by_round`) compare?
2. Against the always-rock opponent, which of the five strategies does best, and why?
3. `beat_last` does very well against one opponent and very badly against another. Identify those opponents.

## How it is graded (50 points)

Code (30 points), from the tests:

- `beat`: 5
- `score`: 5
- `beat_last`: 5
- `expect_change`: 5
- `play_rounds`: 10

Writeup (20 points): explaining your functions in your own words and answering the analysis questions.

Each function's points are all or nothing: you earn them when that function passes every test, including hidden tests that check more cases than the visible ones. So a bug in one function costs only that function's points, not the whole code score.

## Submitting

**You turn in the script `rps.py`, not a notebook.** You can write and test your code in Colab, but what you submit must be the Python file `rps.py`. The autograder only reads `rps.py`. If you upload a Colab notebook (a `.ipynb` file), the tests cannot import your code and the code score will be zero.

The file `rps.py` is already in your assignment repository. To submit, get your finished functions into that file:

1. Write and test your functions (in Colab if you like).
2. Open `rps.py` in your repository on GitHub and click the pencil (edit) button. Paste each finished function in place of its `# your code here`, leaving the provided functions unchanged. Keep the file named exactly `rps.py`. If you prefer, you can instead upload your edited `rps.py` with "Add file > Upload files", which replaces the file.
3. Fill in `writeup.md` the same way.
4. Before the deadline, check that `python rps.py` runs and that `pytest test_rps.py` passes.

*Do not upload the `.ipynb` notebook, and do not use Colab's "Save a copy in GitHub" for your submission, because that saves the notebook, not `rps.py`.*
