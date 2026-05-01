import random


def roll():
    dice_num = random.randint(1, 6)
    return dice_num


print("welcome to the PI game")


while True:
    players = input("Enter the number of player(2-4)")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("players number must be between 2 to 4")
    else:
        print("Enter a valid number , Try again")


max_score = 50

player_scores = [0 for i in range(players)]

while True:

    for index in range(players):
        print(f"player {index+1} turn:")
        current_score = 0
        while True:
            will = input("do you want to roll the dice? (y)")
            if will.lower() != "y":
                break
            value = roll()

            if value == 1:
                print("you rolled a 1")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled: {value}")
                print(f"Current turn score: {current_score}")
        player_scores[index] += current_score
        print(f"total score:{player_scores[index]}")

        if player_scores[index] >= max_score:
            print(f"player {index+1} wins")
            exit()
