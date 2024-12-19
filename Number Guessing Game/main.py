from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
chosen_number = random.choice(range(1,101))
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

while difficulty not in ['easy','hard']:
    print("Please give a valid response!")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

won_the_game = False

while not won_the_game and attempts > 0:

    print(f"You have {attempts} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))
    if guess == chosen_number:
        print(f"You guessed the correct number!")
        won_the_game = True
    elif guess < chosen_number:
        print("Too low.")
        attempts -= 1
    else:
        print("Too high.")
        attempts -= 1

if won_the_game == False:
    print(f"You have no attempts remaining. The correct number is {chosen_number}")