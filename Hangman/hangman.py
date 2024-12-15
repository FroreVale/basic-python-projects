import random

words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon",
    "avocado", "blueberry", "coconut", "dragonfruit", "guava", "jackfruit", "kumquat", "lime", "mandarin", "olive",
    "passionfruit", "pear", "persimmon", "pineapple", "plum", "pomegranate", "pumpkin", "starfruit", "tomato", "yuzu",
    "almond", "cashew", "hazelnut", "pecan", "walnut", "peanut", "pistachio", "macadamia", "acorn", "chestnut",
    "broccoli", "carrot", "cauliflower", "celery", "corn", "cucumber", "eggplant", "garlic", "lettuce", "onion",
    "pepper", "potato", "radish", "spinach", "squash", "zucchini", "beet", "cabbage", "kale", "mushroom",
    "basil", "cilantro", "dill", "ginger", "mint", "oregano", "parsley", "rosemary", "sage", "thyme",
    "bread", "cheese", "chocolate", "coffee", "honey", "jam", "milk", "pasta", "rice", "sugar",
    "tea", "vinegar", "water", "wine", "yogurt", "butter", "cream", "flour", "salt", "soup"
]

print("Welcome to Hangman")

random_word = random.choice(words)
empty_dashes = []
guessed_letters = []

for i in range(len(random_word)):
    empty_dashes.append("__")

won = False
lives = 6

while lives > 0 and won == False:

    print(f"Word to guess: {' '.join(empty_dashes)}")
    user_letter = input("Guess a letter: ")

    reduce_life = True

    if user_letter in guessed_letters:
        print("You already found the word! Try someother letter.")
        continue

    for i in range(len(random_word)):
        if random_word[i] == user_letter:
            empty_dashes[i] = random_word[i]
            guessed_letters.append(user_letter)
            reduce_life = False
    
    if reduce_life:
        lives -= 1
        if lives > 0:
            print(f"You guessed '{user_letter}'. That's not in the word. {lives} lives remaining!")
        else:
            print(f"You lost all of your lives! Game Over. The correct word is {random_word}")

    else:
        if "__" in empty_dashes:
            print(f"You guessed the correct letter '{user_letter}'. Keep Going. {lives} lives remaining!")    
        else:
            print(f"You Won! You guessed every letter of the word '{''.join(empty_dashes)}'")
            won = True
