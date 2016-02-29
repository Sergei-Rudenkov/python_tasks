import re

file = open('resource/poker.txt', 'r')

colors = ['C', 'D', 'S', 'H']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def evaluate(hand):
    if 'A' and 'K' and 'Q' and 'J' and 'T' in hand and check_flush(hand):
        return 1  # Royal Flush
    elif check_flush(hand) and check_straight(hand) > 0:
        return 2  # Straight Flush
    elif check_card_series(hand, 4):
        return 4  # Four of a Kind
    elif check_full_house(hand):
        return 5  # Full House
    elif check_flush(hand):
        return 6  # Flush
    elif check_straight(hand):
        return 7  # Straight
    elif check_card_series(hand, 3):
        return 8  # Three of a Kind
    elif check_card_series(hand, 2):
        return 9  # Two of a Kind


def check_flush(hand):
    regexp = "^\w%s(?: \w%s){4}$"
    for color in colors:
        if re.search(regexp % (color, color), str(hand)):
            return True
    return False


def check_straight(hand):
    iteration = 0
    while iteration < 9:
        sub_card = cards[iteration: iteration + 5]
        if sub_card[0] and sub_card[1] and sub_card[2] and sub_card[3] and sub_card[4] in hand:
            return sub_card[4]
        iteration += 1
    if 'A' and '2' and '3' and '4' and '5' in hand:
        print "Here1"
        return '5'


def check_card_series(hand, range):

    for card in cards:
        look_up = '%s[A-Z]' % card
        rx = re.compile(look_up)
        if len(rx.findall(hand)) == range:
            return True
    return False


def check_full_house(hand):
    pass




print evaluate('KC 4H 5H 4H 3D')


# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# line = file.next()
# first_hand, second_hand = line[:len(line) / 2], line[len(line) / 2:]
