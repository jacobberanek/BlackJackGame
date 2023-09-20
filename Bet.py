

class Bet():

    def __init__(self, pool, bet):
        self.pool=pool
        self.bet=bet

    def winBet(self, oBet):
        self.pool+=oBet.bet

    def loseBet(self, oBet):
        self.pool-=oBet.bet

    def __len__(self):
        return self.pool
