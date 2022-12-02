from enum import Enum


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


letter_shape_association = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS,
    # For first part
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSORS
}

shape_wins_who = {
    Shape.ROCK: [Shape.SCISSORS],
    Shape.PAPER: [Shape.ROCK],
    Shape.SCISSORS: [Shape.PAPER]
}

shape_loses_to = {
    Shape.ROCK: [Shape.PAPER],
    Shape.PAPER: [Shape.SCISSORS],
    Shape.SCISSORS: [Shape.ROCK]
}

scores = {
    Shape.ROCK: 1,
    Shape.PAPER: 2,
    Shape.SCISSORS: 3
}

LOSS_AMOUNT = 0
TIE_AMOUNT = 3
WIN_AMOUNT = 6


def points_from_game(you: Shape, opponent: Shape):
    if you == opponent:
        return TIE_AMOUNT
    elif opponent in shape_wins_who[you]:
        return WIN_AMOUNT
    else:
        return LOSS_AMOUNT


def solve():
    input_file = open('input', 'r')

    total = 0

    for line in input_file:
        game = line.split()

        opponent_shape = letter_shape_association[game[0]]
        seeking_condition = game[1]

        our_shape = None

        if seeking_condition == "Z":
            # Win
            our_shape = shape_loses_to[opponent_shape][0]
        elif seeking_condition == "X":
            # Lose
            our_shape = shape_wins_who[opponent_shape][0]
        else:
            # Tie
            our_shape = opponent_shape

        total += scores[our_shape]
        total += points_from_game(our_shape, opponent_shape)

    input_file.close()

    print(total)


if __name__ == "__main__":
    solve()
