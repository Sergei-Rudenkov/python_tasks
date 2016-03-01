class Play(object):
    def __init__(self):
        self.game = [['-', '-', '-'],
                     ['-', '-', '-'],
                     ['-', '-', '-']]
        self.move_count = 1
        self.finished = False

    def __str__(self):
        return "\n".join(map(str, self.game))

    def check_finished(self):
        result = False
        for i in range(2):
            if self.game[i][0] == self.game[i][1] == self.game[i][2] != '-':
                result = self.game[i][0]
            elif self.game[0][i] == self.game[1][i] == self.game[2][i] != '-':
                result = self.game[i][0]
        if self.game[0][0] == self.game[1][1] == self.game[2][2] != '-':
            return self.game[0][0]
        elif self.game[0][2] == self.game[1][1] == self.game[2][0] != '-':
            return self.game[0][2]
        elif not any("-" in row for row in self.game):
            return "Draw"
        else:
            return result

    def make_move(self, sign, x, y):
        if self.game[x][y] != '-':
            raise ValueError("Field already occupied")
        self.game[x][y] = sign
        self.move_count += 1
        self.finished = self.check_finished()
        print self

    def check_satisfaction(self, x, y):
        try:
            x, y = int(x), int(y)
        except ValueError:
            return "Please enter integers, try again"
        if not (0 <= x <= 2 and 0 <= y <= 2):
            return "Arguments greater then 2 or less then 0 are not allowed, try again"
        if self.game[x][y] != '-':
            return "Field has been already occupied, try again"
        return "Ok"

    def winner(self):
        if self.finished == '+':
            return "First player (+) has won!"
        elif self.finished == '0':
            return "Second player (0) has won!"
        elif self.finished == 'Draw':
            return "The result is draw!"


def main():
    play = Play()
    while not play.finished:
        if play.move_count % 2 == 1:
            print ("First player, please")
            sign = '+'
        else:
            print ("Second player, please")
            sign = '0'

        x, y = raw_input("insert x -> "), raw_input("insert y -> ")
        satisfactory = play.check_satisfaction(x, y)
        while satisfactory != "Ok":
            print satisfactory
            x, y = raw_input("insert x -> "), raw_input("insert y -> ")
            satisfactory = play.check_satisfaction(x, y)
        play.make_move(sign, int(x), int(y))
    else:
        print play.winner()


if __name__ == "__main__":
    main()
