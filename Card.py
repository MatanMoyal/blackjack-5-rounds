class Card:
    def __init__(self, suits:list, ranks:list):
        self.suits = suits
        self.ranks = ranks

    def __str__(self):
        return self.ranks +' ' + self.suits