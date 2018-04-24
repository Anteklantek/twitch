
W = '\033[0m'  # white (normal)
R = '\033[31m' # red
G = '\033[32m' # green
O = '\033[33m' # orange
B = '\033[34m' # blue
P = '\033[35m' # purple


class Stream(object):
    name = ''
    status = ''
    viewers = 0
    game = ''

    def __init__(self, name, status, viewers, game):
        self.name = name
        self.status = status
        self.viewers = viewers
        self.game = game

    def __str__(self):
        return R + self.name + ' | ' + O + str(self.game) + ' | ' + B + str(self.viewers) + '\n' + W + self.status + '\n'