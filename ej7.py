# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"

def rps(p1, p2):
    valid_choices = {"rock", "paper", "scissors"}

    if p1 not in valid_choices or p2 not in valid_choices:
        return "Entrada no válida. Por favor, elija entre 'rock', 'paper' o 'scissors'."

    if p1 == p2:
        return "Draw!"
    elif (
        (p1 == "rock" and p2 == "scissors") or
        (p1 == "paper" and p2 == "rock") or
        (p1 == "scissors" and p2 == "paper")
    ):
        return "Player 1 won!"
    else:
        return "Player 2 won!"