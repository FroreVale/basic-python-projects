import random
from art import logo
print(logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards_list):
    total_score = sum(cards_list)
    if total_score == 21 and len(cards_list) == 2:
        return 0
    while 11 in cards_list and total_score > 21:
        cards_list.remove(11)
        cards_list.append(1)
        total_score = sum(cards_list)
    return total_score

def result(result):
    print(f"Your cards: {player_cards}, your current score: {calculate_score(player_cards)}")
    print(f"Computer's cards: {computer_cards}, computer score: {calculate_score(computer_cards)}")
    print(result)

play_another_game = True

while play_another_game:
    
    computer_cards = []
    player_cards = []

    for i in range(2):
        computer_cards.append(deal_card())
        player_cards.append(deal_card())

    if calculate_score(computer_cards) == 0 and calculate_score(player_cards) == 0:
        result("Both you and computer got a BlackJack! 😮 It's a draw")

    elif calculate_score(computer_cards) == 0:
        result("Computer wins with a BlackJack! 😤")

    elif calculate_score(player_cards) == 0:
        result("You win with a BlackJack! 😎")

    else:
        continue_dealing_cards = True

        while continue_dealing_cards and calculate_score(player_cards) < 21:
            print(f"Your cards: {player_cards}, your current score: {calculate_score(player_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
            response = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
            while response not in ['y','n']:
                print("Please give a valid response!")
                response = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
            if response == 'y':
                player_cards.append(deal_card())
            else:
                continue_dealing_cards = False
        
        if calculate_score(player_cards) > 21:
            result("You went over! You lose 😭")
        
        else:
            while calculate_score(computer_cards) < 17:
                computer_cards.append(deal_card())
            if calculate_score(computer_cards) > 21:
                result("Computer went over! You win 😁")

            else:
                if calculate_score(computer_cards) == calculate_score(player_cards):
                    result("Both you and the computer have the same score. It's a draw! 😬")
                elif calculate_score(computer_cards) < calculate_score(player_cards):
                    result("You win 😀")
                else:
                    result("You lose 😤")

    another_game = input("\nType 'y' to play another game or type 'n' to stop playing ").lower()

    while another_game not in ['y','n']:
        print("Please give a valid response!")
        another_game = input("\nType 'y' to play another game or type 'n' to stop playing ").lower()
    
    if another_game == 'n':
        play_another_game = False