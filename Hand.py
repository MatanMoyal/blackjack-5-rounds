from Utilities import values


class Hand:
    def __init__(self, name: str):
        self.name = name
        self.card = []
        self.money = 0
        self.sum = 0
        self.TotalSum = 0


    def newGame(self):
        self.card = []
        self.sum = 0

    def __str__(self):
        if (self.money >= 0):
            print(f'The Game Is Done {self.name}, You Earn: {self.money} Shekels\n')
        else:
            print(f'The Game Is Done {self.name}, You Lose: {self.money} Shekels\n')

    # def __str__(self):
    #     myHand = ''
    #     for my in self.card:
    #         myHand += '\n' + my.__str__()
    #     return (self.name + myHand.__str__())

    def add_card(self, card):
        self.card.append(card)
        self.sum += values[card.ranks]

    # def add_card(self,card):
    #     for key in values:
    #         if key in self.myHand:
    #             print(key)
    #             self.sum += values[key]
    #     return f'the sum of my cards is: {self.sum}'
