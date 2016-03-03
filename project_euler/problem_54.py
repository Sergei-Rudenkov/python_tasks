import re

# https://projecteuler.net/problem=54


colors = ['C', 'D', 'S', 'H']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def evaluate(hand):
    result_map = {}
    if all(card in hand for card in "AKQJT") and check_flush(hand):
        return 1  # Royal Flush
    elif check_flush(hand) and check_straight(hand):
        result_map.update({'combination': 2, 'additional indicator': check_straight(hand)})
        return result_map  # Straight Flush
    elif check_card_series(hand, 4):
        result_map.update(
            {'combination': 3, 'additional indicator': [check_card_series(hand, 4)] + sort_by_highest_card_value(hand)})
        return result_map  # Four of a Kind
    elif check_full_house(hand):
        result_map.update({'combination': 4, 'additional indicator': check_full_house(hand)})
        return result_map  # Full House
    elif check_flush(hand):
        result_map.update({'combination': 5, 'additional indicator': sort_by_highest_card_value(hand)})
        return result_map  # Flush
    elif check_straight(hand):
        result_map.update({'combination': 6, 'additional indicator': check_straight(hand)})
        return result_map  # Straight
    elif check_card_series(hand, 3):
        result_map.update(
            {'combination': 7, 'additional indicator': [check_card_series(hand, 3)] + sort_by_highest_card_value(hand)})
        return result_map  # Three of a Kind
    elif check_2_pairs(hand):
        result_map.update(
            {'combination': 8, 'additional indicator': check_2_pairs(hand) + sort_by_highest_card_value(hand)})
        return result_map  # Two Pairs
    elif check_card_series(hand, 2):
        result_map.update(
            {'combination': 9, 'additional indicator': [check_card_series(hand, 2)] + sort_by_highest_card_value(hand)})
        return result_map  # Two of a Kind
    else:
        result_map.update({'combination': 10, 'additional indicator': sort_by_highest_card_value(hand)})
        return result_map  # No combinations


def check_flush(hand):
    regexp = "^\w%s(?: \w%s){4}$"
    for color in colors:
        if re.search(regexp % (color, color), str(hand)):
            look_up = '(.)[CDHS]'
            rx = re.compile(look_up)
            max_card = 0
            for n in rx.findall(hand):
                if cards.index(n) > max_card:
                    max_card = cards.index(n)
            return max_card
    return False


def check_straight(hand):
    for iteration in range(9):
        sub_card = cards[iteration: iteration + 5]
        if all(card in hand for card in sub_card[0: 4]):
            return cards.index(sub_card[4])
    if all(card in hand for card in "2345A"):
        return cards.index('5')


def check_card_series(hand, range):
    for card in cards:
        look_up = '%s[CDHS]' % card
        rx = re.compile(look_up)
        if len(rx.findall(hand)) == range:
            return cards.index(card)
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
        return result_set


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
        return sorted(result_set, reverse=True)


def sort_by_highest_card_value(hand):
    result_set = []
    look_up = '(.)[CDHS]'
    rx = re.compile(look_up)
    for n in rx.findall(hand):
        result_set.append(cards.index(n))
    return sorted(result_set, reverse=True)


def compare_hands(first_hand, second_hand):
    first_hand = evaluate(first_hand)
    second_hand = evaluate(second_hand)
    if first_hand['combination'] < second_hand['combination']:
        return 1  # first hand win
    elif first_hand['combination'] > second_hand['combination']:
        return -1  # second hand win
    elif first_hand['combination'] == second_hand['combination']:
        if first_hand['additional indicator'] > second_hand['additional indicator']:
            return 1  # first hand win
        elif first_hand['additional indicator'] < second_hand['additional indicator']:
            return -1  # second hand win
        else:
            return 0  # draw


def main():
    count_first_win = 0
    file = open('resource/poker.txt', 'r')
    for line in file:
        first_hand, second_hand = line[:len(line) / 2], line[len(line) / 2:]
        if compare_hands(first_hand, second_hand) == 1:
            count_first_win += 1
    print "First hand won %s times" % count_first_win


if __name__ == '__main__':
    main()


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

