import re

# file = open('resource/poker.txt', 'r')

colors = ['C', 'D', 'S', 'H']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def evaluate(hand):
    if all(card in hand for card in "AKQJT") and check_flush(hand):
        return 1  # Royal Flush
    elif check_flush(hand) and check_straight(hand) > 0:
        return 2  # Straight Flush
    elif check_card_series(hand, 4):
        return 3  # Four of a Kind
    elif check_full_house(hand):
        return 4  # Full House
    elif check_flush(hand):
        return 5  # Flush
    elif check_straight(hand):
        return 6  # Straight
    elif check_card_series(hand, 3):
        return 7  # Three of a Kind
    elif check_2_pairs(hand):
        return 8  # Two Pairs
    elif check_card_series(hand, 2):
        return 9  # Two of a Kind
    else:
        return 10  # No combinations


def check_flush(hand):
    regexp = "^\w%s(?: \w%s){4}$"
    for color in colors:
        if re.search(regexp % (color, color), str(hand)):
            return True
    return False


def check_straight(hand):
    for iteration in range(9):
        sub_card = cards[iteration: iteration + 5]
        if all(card in hand for card in sub_card[0: 4]):
            return sub_card[4]
    if all(card in hand for card in "2345A"):
        return '5'


def check_card_series(hand, range):
    for card in cards:
        look_up = '%s[CDHS]' % card
        rx = re.compile(look_up)
        if len(rx.findall(hand)) == range:
            return card
    return False


def check_full_house(hand):
    pair = False
    triple = False
    result_set = []
    for card in cards:
        look_up = '%s[CDHS]' % card
        rx = re.compile(look_up)
        if len(rx.findall(hand)) == 3:
            triple = card
            result_set.append(cards.index(triple))
        elif len(rx.findall(hand)) == 2:
            pair = card
            result_set.append(cards.index(pair))
    if pair and triple:
        return sorted(result_set, reverse=True)


def check_2_pairs(hand):
    first_pair = False
    second_pair = False
    result_set = []
    for card in cards:
        look_up = '%s[CDHS]' % card
        rx = re.compile(look_up)
        if len(rx.findall(hand)) == 2 and not first_pair:
            first_pair = card
            result_set.append(cards.index(first_pair))
        elif len(rx.findall(hand)) == 2 and first_pair:
            second_pair = card
            result_set.append(cards.index(second_pair))
    if first_pair and second_pair:
        return result_set


def sort_by_highest_card_value(hand):
    result_set = []
    look_up = '(.)[CDHS]'
    rx = re.compile(look_up)
    for n in rx.findall(hand):
        result_set.append(cards.index(n))
    return sorted(result_set, reverse=True)


#print sort_by_highest_card_value('3C 4H 3H 4C 3D')


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
