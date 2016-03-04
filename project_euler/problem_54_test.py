import unittest
import problem_54


class TestPoker(unittest.TestCase):
    def test_royal_flush(self):
        hand = "TH JH QH KH AH"
        self.assertEqual(problem_54.evaluate(hand), 1)

    def test_straight_flush(self):
        hand = "TC JC QC KC 9C"
        self.assertEqual(problem_54.evaluate(hand), {'additional indicator': 11, 'combination': 2})

    def test_four_of_kind(self):
        hand = "AC AH AD AS 2H"
        self.assertEqual(problem_54.evaluate(hand), {'additional indicator': [12, 12, 12, 12, 12, 0], 'combination': 3})

    def test_full_house(self):
        hand = "2C 2H 2S 3C 3H"
        self.assertEqual(problem_54.evaluate(hand), {'additional indicator': [0, 1], 'combination': 4})

    def test_flush(self):
        hand = "2H AH KH 7H 3H"
        self.assertEqual(problem_54.evaluate(hand), {'additional indicator': [12, 11, 5, 1, 0], 'combination': 5})

    def test_straight(self):
        hand = "2H 3C 4H 5H 6H"
        self.assertEqual(problem_54.evaluate(hand), {'additional indicator': 4, 'combination': 6})

    def test_three_of_kind(self):
        hand = "AC AH AD QS TH"
        self.assertEqual(problem_54.evaluate(hand), {'additional indicator': [12, 12, 12, 12, 10, 8], 'combination': 7})

    def test_two_pairs(self):
        hand = "AC AH QD QS TH"
        self.assertEqual(problem_54.evaluate(hand),
                         {'additional indicator': [12, 10, 12, 12, 10, 10, 8], 'combination': 8})

    def test_pair(self):
        hand = 'JH JC 2D 3H 7S'
        self.assertEqual(problem_54.evaluate(hand), {'additional indicator': [9, 9, 9, 5, 1, 0], 'combination': 9})

    def test_evaluation(self):
        hand = '7H 8C 3H TS 2D'
        self.assertEqual(problem_54.evaluate(hand), {'additional indicator': [8, 6, 5, 1, 0], 'combination': 10})


if __name__ == '__main__':
    unittest.main()
