""" Solution ideas and notes:

First column: 
A = Rock
B = Paper
c = Scissors

Second column:
X = Rock
Y = Paper
Z = Scissors

Open the file, read each line, first calculate the score for the shape you selected, (1 for Rock, 2 for Paper, and 3 for Scissors)  

Rock paper scissors logic: If you win you get 6 points, draw = 3, loss = 0
"""

player1_dict = {
    "A": ["Rock", 1],
    "B": ["Paper", 2],
    "C": ["Scissors", 3]
}


player2_dict = {
    "X": ["Rock", 1],
    "Y": ["Paper", 2],
    "Z": ["Scissors", 3]
}

def rock_paper_scissors(file_name):
    with open(file=file_name) as file:
        total_score = 0
        line = file.readline()
        while line != '':
            player1_choice = line[0]
            player2_choice = line[2]
            print(f"Player 1 plays {player1_dict[player1_choice][0]}, \
Player 2 plays {player2_dict[player2_choice][0]}.")
            if player1_dict[player1_choice][0] == player2_dict[player2_choice][0]:
                print(f"The round was a draw, each player gets 3 points.")
                total_score += 3
            elif player1_dict[player1_choice][0] == "Rock" and player2_dict[player2_choice][0] == "Paper":
                print(f"Player 2 wins.")
                total_score += 6
            elif player1_dict[player1_choice][0] == "Rock" and player2_dict[player2_choice][0] == "Scissors":
                print(f"Player 1 wins.")
            elif player1_dict[player1_choice][0] == "Paper" and player2_dict[player2_choice][0] == "Scissors":
                print(f"Player 2 wins.")
                total_score += 6
            elif player1_dict[player1_choice][0] == "Paper" and player2_dict[player2_choice][0] == "Rock":
                print(f"Player 1 wins.")
            elif player1_dict[player1_choice][0] == "Scissors" and player2_dict[player2_choice][0] == "Rock":
                print(f"Player 2 wins.")
                total_score += 6
            elif player1_dict[player1_choice][0] == "Scissors" and player2_dict[player2_choice][0] == "Paper":
                print(f"Player 1 wins.")
            total_score += player2_dict[player2_choice][1]
            print(f"Current score is: {total_score}")
            line = file.readline()

def rock_paper_scissors_part2(file_name):
    with open(file=file_name) as file:
        total_score = 0
        line = file.readline()
        while line != '':
            player1_choice = line[0]
            player2_choice = line[2]
            print(f"Player 1 plays {player1_dict[player1_choice][0]}, \
Player 2 plays {player2_dict[player2_choice][0]}.")
            if player1_dict[player1_choice][0] == "Rock" and player2_choice == "X":
                total_score += 3
            elif player1_dict[player1_choice][0] == "Rock" and player2_choice == "Y":
                total_score += 4
            elif player1_dict[player1_choice][0] == "Rock" and player2_choice == "Z":
                total_score += 8
            elif player1_dict[player1_choice][0] == "Paper" and player2_choice == "X":
                total_score += 1
            elif player1_dict[player1_choice][0] == "Paper" and player2_choice == "Y":
                total_score += 5
            elif player1_dict[player1_choice][0] == "Paper" and player2_choice == "Z":
                total_score += 9
            elif player1_dict[player1_choice][0] == "Scissors" and player2_choice == "X":
                total_score += 2
            elif player1_dict[player1_choice][0] == "Scissors" and player2_choice == "Y":
                total_score += 6
            elif player1_dict[player1_choice][0] == "Scissors" and player2_choice == "Z":
                total_score += 7
            #total_score += player2_dict[player2_choice][1]
            print(f"Current score is: {total_score}")
            line = file.readline()


rock_paper_scissors('levels/level2/level2data.txt')
rock_paper_scissors_part2('levels/level2/level2data.txt')
