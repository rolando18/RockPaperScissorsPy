from random import randint
import math

def main():
    # declare variables
    comp_score = 0
    player_score = 0
    moves = ["rock","paper","scissors"]
    # game start
    print("Enter number of rounds: ")
    num_of_games = int(input())
    while(num_of_games % 2 == 0 or num_of_games <= 1):
        print("Please enter an odd number greater than 1: ")
        num_of_games = int(input())
        # determine max score before win
    winning_moves = math.ceil(num_of_games/2)
    print(f"Alright! Best {winning_moves} of {num_of_games} wins!")
    while(comp_score < winning_moves and player_score < winning_moves):
        # assign random move to computer
        comp_move = moves[randint(0,2)]
        # accept player move
        print(f"Make a move: {moves}")
        player_move = input().lower()
        # check if move valid
        while(player_move not in moves):
            print(f"Please enter a valid move {moves}: ")
            player_move = input().lower()
        # determine round winner
        if comp_move == player_move:
            print("Draw!")
        elif comp_move == "rock":
            if player_move == "paper":
                player_score += 1
            else:
                comp_score += 1
        elif comp_score == "paper":
            if player_move == "scissors":
                player_score += 1
            else:
                comp_score += 1
        else:
            if player_move == "rock":
                player_score += 1
            else:
                comp_score += 1
        # determine leader
        print(f"Computer {comp_score} : Player {player_score}")
    # determine overall winner
    winner = "Computer" if comp_score > player_score else "Player"
    print(f"{winner} wins!")
    # game over


if __name__ == '__main__':
    main()