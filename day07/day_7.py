
def get_hand_rank(hand: str, part1: bool = True) -> int:
    ordered_types = [
        [5],             # Five of a kind
        [4, 1],          # Four of a kind
        [3, 2],          # Full house
        [3, 1, 1],       # Three of a kind
        [2, 2, 1],       # Two pair
        [2, 1, 1, 1],    # One pair
        [1, 1, 1, 1, 1]  # High card
    ]
    if part1: 
        label_counts = [hand.count(card) for card in set(hand)]
    else: 
        label_counts = [hand.count(card) for card in set(hand) if card != 'J'] or [0]  # only jokers
    label_counts.sort(reverse=True)

    if not part1: 
        label_counts[0] += hand.count('J')
    return ordered_types.index(label_counts)

def get_cards_value(hand: str, part1: bool = True) -> tuple:
    if part1: 
        ordered_labels = 'AKQJT98765432'
    else: 
        ordered_labels = 'AKQT98765432J'
    return (ordered_labels.index(card) for card in hand)

# Read the input file
with open("day07/input.txt") as f:
    lines = [line.split() for line in f]


###############################################################################
#
#  PART 1
#
###############################################################################
hands_p1 = [
    (
        get_hand_rank(line[0]),
        *get_cards_value(line[0]),
        int(line[1])
    ) for line in lines
]

hands_p1.sort(reverse=True)
winnings_p1 = sum(
    rank * hand[-1]  # rank * bid
    for rank, hand in enumerate(hands_p1, start=1)
)

print(winnings_p1)

###############################################################################
#
#  PART 2"index": 1, 
#
###############################################################################
hands_p2 = [
    (
        get_hand_rank(line[0], part1=False),
        *get_cards_value(line[0], part1=False),
        int(line[1])
    ) for line in lines
]

hands_p2.sort(reverse=True)
winnings_p2 = sum(
    rank * hand_p2[-1]  # rank * bid
    for rank, hand_p2 in enumerate(hands_p2, start=1)
)

print(winnings_p2)