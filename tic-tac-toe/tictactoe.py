class Play(object):
    game = [['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']]

    move_count = 1
    finished = False

    def __str__(self):
        return self.game[0].__str__() + '\n' + self.game[1].__str__() + "\n" + self.game[2].__str__()


def make_move(play, sign, x, y):
    if int(x) > 2 or int(y) > 2 or int(x) < 0 or int(y) < 0:
        raise EnvironmentError(" Arguments greater then 2 or less then 0 are not allowed")
    play.game[x][y] = sign
    play.move_count += 1
    print play


play = Play()

while not play.finished:
    if play.move_count%2 == 1:
        print ("First player, please")
        make_move(play, '0', input("insert x -> "), input("insert y -> "))
    else:
        print ("Second player, please")
        make_move(play, '+', input("insert x -> "), input("insert y -> "))