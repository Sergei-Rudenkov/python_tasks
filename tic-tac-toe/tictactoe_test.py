import unittest
import tictactoe


class TestPlay(unittest.TestCase):
    def test_satisfactory_int(self):
        play = tictactoe.Play()
        self.assertEqual(
            play.check_satisfaction(1, 4), "Arguments greater then 2 or less then 0 are not allowed, try again")

    def test_satisfactory_int_violation(self):
        play = tictactoe.Play()
        self.assertEqual(play.check_satisfaction("hello", 2), "Please enter integers, try again")

    def test_satisfactory_field_occupation(self):
        play = tictactoe.Play()
        play.make_move("+", 1, 1)
        self.assertEqual(play.check_satisfaction(1, 1), "Field has been already occupied, try again")

    def test_satisfactory_success(self):
        play = tictactoe.Play()
        self.assertEqual(play.check_satisfaction(1, 1), "Ok")

    def test_check_winner(self):
        play = tictactoe.Play()
        play.make_move("+", 1, 0)
        play.make_move("+", 1, 1)
        play.make_move("+", 1, 2)
        self.assertEqual(play.winner(), "First player (+) has won!")

    def test_check_draw(self):
        play = tictactoe.Play()
        play.make_move("+", 2, 1)
        play.make_move("+", 0, 2)
        play.make_move("+", 1, 0)
        play.make_move("+", 2, 2)
        play.make_move("0", 1, 1)
        play.make_move("0", 0, 0)
        play.make_move("0", 1, 2)
        play.make_move("0", 0, 1)
        play.make_move("0", 2, 0)
        self.assertEqual(play.winner(), "The result is draw!")

    def test_occupied_exception(self):
        play = tictactoe.Play()
        play.make_move("+", 2, 1)
        with self.assertRaises(ValueError):
            play.make_move("0", 2, 1)


if __name__ == '__main__':
    unittest.main()
