from Utilities import suits, ranks
from Card import Card
import random


class Deck:
    def __init__(self):
        self.deck = []
        self.inital_deck()

    def inital_deck(self):
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        empty_deck = ''
        for cards in self.deck:
            empty_deck += '\n' + cards.__str__()
        return empty_deck

    def shuffle_deck(self):
        shuffle1 = random.shuffle(self.deck)
        return shuffle1

    def take_card(self):
        card = self.deck.pop()
        return card
