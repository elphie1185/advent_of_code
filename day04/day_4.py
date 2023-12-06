import re

def split_winning_and_your_cards(card): 
    winning_numbers = card.split("|")[0]
    my_numbers = card.split("|")[1]
    return winning_numbers.split(), my_numbers.split()

def get_number_of_matches(card): 
    win_card, my_cards = split_winning_and_your_cards(card)
    return len(set(win_card).intersection(set(my_cards)))

def calculate_winning_total(n): 
    total = 0
    if n > 0: 
        total = 1
        for i in range(1, n): 
            total *= 2
    return total

def calculate_number_of_cards(card_win_dict, n_cards_list):
    for i in range(
        card_win_dict["card_number"], 
        (card_win_dict["card_number"]+card_win_dict["num_wins"])
    ):
        n_cards_list[i]+=1
    return n_cards_list 

with open("day04/input.txt") as f:
    lines = [line.strip() for line in f]

###########################################
#
# PART 1
#
###########################################

# remove the start of each line
cards = [re.sub(r'^Card   \d\:', '', line).strip() for line in lines]

# get the number of winning cards per draw
num_winning_per_games = [get_number_of_matches(card) for card in cards]
winning_scores = [calculate_winning_total(num_win) for num_win in num_winning_per_games]

print(sum(winning_scores))

###########################################
#
# PART 2
#
###########################################
total_cards = [1] * len(lines)

for card_number, n_cards in enumerate(num_winning_per_games):
    for i in range(n_cards): 
        total_cards[card_number + 1 + i] += total_cards[card_number]

print(sum(total_cards))