import unittest
import problem_54


class TestPoker(unittest.TestCase):
    def test_royal_flush(self):
        hand = "TH JH QH KH AH"
        self.assertEqual(problem_54.evaluate(hand), 1)

    def test_straight_flush(self):
        hand = "TC JC QC KC 9C"
        self.assertEqual(problem_54.evaluate(hand), 2)
        self.assertEqual(problem_54.check_straight(hand), 'K')

    def test_four_of_kind(self):
        hand = "AC AH AD AS 2H"
        self.assertEqual(problem_54.evaluate(hand), 3)
        self.assertEqual(problem_54.check_card_series(hand, 4), 'A')

    def test_full_house(self):
        hand = "2C 2H 3S 3C 3H"
        self.assertEqual(problem_54.evaluate(hand), 4)
        self.assertEqual(problem_54.check_full_house(hand), [1, 0])

    def test_flush(self):
        hand = "2H AH KH 7H 3H"
        self.assertEqual(problem_54.evaluate(hand), 5)

    def test_straight(self):
        hand = "2H 3C 4H 5H 6H"
        self.assertEqual(problem_54.evaluate(hand), 6)
        self.assertEqual(problem_54.check_straight(hand), '6')

    def test_three_of_kind(self):
        hand = "AC AH AD QS TH"
        self.assertEqual(problem_54.evaluate(hand), 7)
        self.assertEqual(problem_54.check_card_series(hand, 3), 'A')

    def test_two_pairs(self):
        hand = "AC AH QD QS TH"
        self.assertEqual(problem_54.evaluate(hand), 8)
        self.assertEqual(problem_54.check_2_pairs(hand), [10, 12])

    def test_pair(self):
        hand = 'JH JC 2D 3H 7S'
        self.assertEqual(problem_54.evaluate(hand), 9)
        self.assertEqual(problem_54.check_card_series(hand, 2), 'J')

    def test_evaluation(self):
        hand = '7H 8C 3H TS 2D'
        self.assertEqual(problem_54.evaluate(hand), 10)
        self.assertEqual(problem_54.sort_by_highest_card_value(hand), [8, 6, 5, 1, 0])


if __name__ == '__main__':
    unittest.main()
