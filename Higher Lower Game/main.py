from art import logo, vs
from game_data import data
from random import choice

print(logo)

person_one = choice(data)
person_two = choice(data)

while person_one == person_two:
    person_two = choice(data)

score = 0
game_over = False

while not game_over:
    print(f"Compare A: {person_one['name']}, a {person_one["description"]}, from {person_one['country']}")

    print(vs)

    print(f"Against B: {person_two['name']}, a {person_two["description"]}, from {person_two['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    while guess not in ['a','b']:
        print("Please give a valid response!")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if person_one['follower_count'] > person_two['follower_count']:
        answer = 'a'
    else:
        answer = 'b'

    if guess == answer:
        score += 1
        print(f"\nYou are right! Current Score: {score}\n")
        person_one = person_two
        person_two = choice(data)
        while person_one == person_two:
            person_two = choice(data)
    else:
        print(f"\nSorry that's wrong. {person_one['name'] if answer == 'a' else person_two['name']} has more followers than {person_two['name'] if answer == 'a' else person_one['name']}. Final score: {score}\n")
        game_over = True






