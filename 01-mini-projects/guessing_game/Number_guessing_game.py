import random


answer = input("wanna play guessnumber game?")
if answer.lower() != "yes":
    quit()

random_num = random.randrange(1, 10)
print(random_num)

print("well then! Guess a number between 1 to 10\n")
guesses = 0
# while True:
#     guesses += 1
#     guess = input("\n")

#     if guess.isdigit():
#         guess = int(guess)
#         if guess <= 0 or guess > 10:
#             print("enter a number in range!")
#     else:
#         print("please guess a number!")
#         continue

#     if int(guess) == random_num:
#         print("you won, congrats!")
#         break
#     elif int(guess) < random_num:
#         print("too small , guess bigger number")
#     elif int(guess) > random_num:
#         print("too big, guess smaller number")
#         continue

# print(f"you got it in {guesses} , attempts")


for i in range(5):
    guesses += 1
    guess = input("\n")

    if guess.isdigit():
        guess = int(guess)
        if guess <= 0 or guess > 10:
            print("enter a number in range!")
    else:
        print("please guess a number!")
        continue

    if int(guess) == random_num:
        break
    elif int(guess) < random_num:
        print("too small , guess bigger number")
    elif int(guess) > random_num:
        print("too big, guess smaller number")
        continue

if guess == random_num:
    print("congrats ! you did it ")
else:
    print("Time Out! you loose")
