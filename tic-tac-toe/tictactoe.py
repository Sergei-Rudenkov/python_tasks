class Play(object):
    game = [['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']]

    move_count = 1
    finished = False

    def __str__(self):
        return "\n".join(map(str, self.game))

    def check_finished(self):
        for i in range(2):
            if self.game[i][0] == self.game[i][1] == self.game[i][2] != '-':
                result = self.game[i][0]
            elif self.game[0][i] == self.game[1][i] == self.game[2][i] != '-':
                result = self.game[i][0]
            elif self.game[0][0] == self.game[1][1] == self.game[2][2] != '-':
                result = self.game[0][0]
            elif self.game[0][2] == self.game[1][1] == self.game[2][0] != '-':
                result = self.game[0][2]
            elif map(str, self.game).__contains__("-"):
                result = "Draw"
            else:
                result = False
        return result

    def make_move(self, sign, x, y):
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
        else:
            return "Ok"


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
        while satisfactory is not "Ok":
            print satisfactory
            x, y = raw_input("insert x -> "), raw_input("insert y -> ")
            satisfactory = play.check_satisfaction(x, y)
        play.make_move(sign, int(x), int(y))
    else:
        if play.finished == '+':
            print "First player has won!"
        elif play.finished == '0':
            print "Second player has won!"
        elif play.finished == 'Draw':
            print "The result is draw!"


if __name__ == "__main__":
    main()
