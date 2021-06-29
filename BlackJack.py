from Deck import Deck
from Hand import Hand
from Utilities import values
from Card import Card


def ProblemAce(currentHand, newCard):
    if currentHand.sum + values[newCard.ranks] > 21:
        currentHand.add_card(Card("Ace", '1'))
    else:
        currentHand.add_card(Card("Ace", '11'))


def AnotherCard():
    if (UserHand.sum <= 21):
        return input("Do You Want Take Another Crad? (Yes/No): ")
    else:
        return 'no'


def StartNewGame(UserHand, DealerHand):
    CurrentDeck = Deck()
    CurrentDeck.shuffle_deck()
    UserHand.add_card(CurrentDeck.take_card())
    UserHand.add_card(CurrentDeck.take_card())
    DealerHand.add_card(CurrentDeck.take_card())
    DealerHand.add_card(CurrentDeck.take_card())
    return CurrentDeck


UserName = input("Enter Player Name: ")
DealerName = "Dealer"
UserHand = Hand(UserName)
DealerHand = Hand(DealerName)
CurrentDeck = StartNewGame(UserHand, DealerHand)
print(f'The Sum Of My Cards Is: {UserHand.sum}')
isContinue = True
question = AnotherCard()

while (isContinue):
    if (question.lower() == 'yes' or question.lower() == 'y'):
        # handaling User ace problem
        newCard = CurrentDeck.take_card()
        if newCard.ranks == "Ace":
            ProblemAce(UserHand, newCard)
        else:
            UserHand.add_card(newCard)

        # handaling Dealer ace problem
        newCard = CurrentDeck.take_card()
        if newCard.ranks == 'Ace':
            ProblemAce(DealerHand, newCard)
        else:
            DealerHand.add_card(newCard)

    else:
        if (UserHand.sum <= 21):
            if (DealerHand.sum > 21):
                print("You Win, Dealer is grater then 21\n")
                UserHand.money += 100
            elif (DealerHand.sum < UserHand.sum):
                print("You Win !")
                UserHand.money += 100
            elif (DealerHand.sum > UserHand.sum):
                print("You Loose")
                UserHand.money -= 100
            elif (DealerHand.sum == UserHand.sum):
                print("Draw You And Dealer !\n")
        else:
            print("You Loose !\n")
            UserHand.money -= 100
        AnotherGame = input("Do You Want Another Game? (Yes/No): ").lower()
        if (AnotherGame == 'yes' or AnotherGame == 'y'):
            UserHand.newGame()
            DealerHand.newGame()
            CurrentDeck = StartNewGame(UserHand, DealerHand)
        else:
            isContinue = False
            UserHand.__str__()
            print("Good Bye :)")
            break
    print(f'The Sum Of My Cards Is: {UserHand.sum}\n')
    question = AnotherCard()
