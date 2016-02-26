import re

file = open('resource/poker.txt', 'r')

color = ['C', 'D', 'S', 'H']
card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']


def evaluate(hand):
    if str(hand).__contains__('A') and str(hand).__contains__('K') and str(hand).__contains__('Q') and str(
            hand).__contains__('J') and str(hand).__contains__('T') and re.search("\*", str(hand)):
        return 1
    if str(hand).__contains__('A'):
        return 2


for _ in range(10):
    line = file.next()
    first_hand, second_hand = line[:len(line) / 2], line[len(line) / 2:]
    # print "First hand: ", first_hand, " Second hand: ", second_hand
print evaluate('TD JD KD QD AD')
