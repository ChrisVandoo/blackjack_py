import random
import pprint

class Card():

    #creates a new card, requires a suit and card type
    def __init__(self, suit, type):
        self.suit = suit
        self.type = type
        
        #need to fix how aces work, rn all set to 11
        if self.type == 14:
            self.value = 11
        elif self.type > 10:
            self.value = 10
        else:
            self.value = self.type
    
    #returns a string containing the suit of the card
    def get_suit(self):
        suits = {
            "0": "hearts",
            "1": "clubs",
            "2": "diamonds",
            "3": "spades"
        }
        return suits[str(self.suit)]
    
    #gets the face value of the card, if numerical returns number else returns string value
    def get_face(self):
        face = {
            "11": "jack",
            "12": "queen",
            "13": "king",
            "14": "ace"
        }
        if self.type > 10:
            return face[str(self.type)]
        else:
            return str(self.type)
    
#this class simulates a deck of cards
#creates a deck containing 52 unique cards
#deal deals a unique card up to 52 times
#shuffle resets the deck allowing all cards to be dealt again
class Deck():

    def __init__(self):
        self.deck = []
        self.dealt = []
        suit = 0
        for c in range(5):
            for x in range(2,15):
                card = Card(suit, x)
                self.deck.append(card)
            suit += 1 

    def debug_print(self):
        for c in self.deck:
            print(str(c.suit) + " " + str(c.value))

    def deal(self):
        num = random.randint(0, 52)
        while self.dealt.count(num) > 0:
            num = random.randint(0,52)

        self.dealt.append(num)
        return self.deck[num]

    def shuffle(self):
        self.dealt.clear()


class Hand():

    def __init__(self):
        self.cards = []
    
    #attempts to add a card to the hand
    #if values are greater than 21, returns false indicating you busted
    def add_card(self, card):
        self.cards.append(card)
        valid = self.calc_value()
        if valid > 21:
            return False
        else:
            return True
    
    def calc_value(self):
        count = 0
        for card in self.cards:
            count = count + card.value
        return count

    def empty_hand(self):
        self.cards.clear()

    def dprint(self):
        for card in self.cards:
            print(f"{card.get_face()}-{card.get_suit()},", end=" ")