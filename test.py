class Number:
    def __init__(self, n):
        self.n = n
    def prin(self):
        print(self.n)

class N(Number):
    def caca(self):
        pass

num = Number(5)
n = N(6)

n.prin()
