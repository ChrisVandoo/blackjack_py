import deck

class Dealer():

    def __init__(self):
        self.hand = deck.Hand()
    
    def add_card(self, card):
        return self.hand.add_card(card)