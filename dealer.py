import deck

class Dealer():

    def __init__(self):
        self.hand = deck.Hand()
    
    def add_card(self, card):
        return self.hand.add_card(card)

    #this currently doesn't account for a soft 17, requires more rules
    #should be called after the dealers hand contains 2 cards
    def evaluate_hand(self):
        if self.hand.calc_value() < 17:
            self.hand.add_card(deck.Card())

    def clear_hand(self):
        self.hand.empty_hand()