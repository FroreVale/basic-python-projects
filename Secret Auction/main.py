from art import logo
print(logo)

bidding_continues = True
bidding_dictionary = {}

while bidding_continues:
    name = input("What is your name? :")
    bid = int(input("What is your bid?: $"))
    bidding_dictionary[name] = bid
    wrong_input = True
    other_bidders = ""
    while wrong_input:
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
        if other_bidders == "yes" or other_bidders == "no":
            wrong_input = False
        else:
            print("Enter a valid input.")
    if other_bidders == "no":
        bidding_continues = False
    else:
        print("\n" * 100)



winner = max(bidding_dictionary, key=bidding_dictionary.get)
max_bid = bidding_dictionary[winner]
print(f"The winner is {winner} with a bid of ${max_bid}")

    
