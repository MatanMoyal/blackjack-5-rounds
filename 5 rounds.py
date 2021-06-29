from Deck import Deck
from Hand import Hand
from Utilities import values
from Card import Card


def ProblemAce(currentHand, newCard):
    if currentHand.sum + values[newCard.ranks] > 21:
        currentHand.add_card(Card("Ace", '1'))
    else:
        currentHand.add_card(Card("Ace", '11'))


def StartNewRound(PlayerHand):
    PlayerHand.add_card(CurrentDeck.take_card())
    PlayerHand.add_card(CurrentDeck.take_card())


def AnotherCard():
    if (player.sum <= 21):
        return input("Do You Want to Take Another Card? (Yes/No): ")
    else:
        return 'no'


def Game():
    while (isContinue):
        print(f'The Sum Of My Cards Is: {player.sum}\n')
        question = AnotherCard()

        while not ConditionWrong(question):
            question = input("Must Write Yes Or No: ")

        if (question.lower() == 'yes' or question.lower() == 'y'):
            # handaling User ace problem
            newCard = CurrentDeck.take_card()
            if newCard.ranks == "Ace":
                ProblemAce(player, newCard)
            else:
                player.add_card(newCard)
        else:
            break


def ConditionWrong(question):
    if (((question.lower() == 'yes' or question.lower() == 'y')
         or (question.lower() == 'no' or question.lower() == 'n'))):
        return True
    return False


CurrentDeck = Deck()
CurrentDeck.shuffle_deck()
NumRound = 0
PlayerName = input("Enter Player Name: ")
player = Hand(PlayerName)
StartNewRound(player)

isContinue = True

while NumRound < 5:
    Game()
    if player.sum <= 21:
        player.TotalSum += player.sum
    else:
        player.TotalSum -= player.sum
    print("\n--------- New Round ---------\n")
    player.newGame()
    NumRound += 1
    StartNewRound(player)

print(f'Your Final Score Is: {player.TotalSum}\n')
