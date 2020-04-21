import deck

class Dealer():

    def __init__(self):
        self.hand = deck.Hand()
    
    def add_card(self, card):
        return self.hand.add_card(card)
            
    def clear_hand(self):
        self.hand.empty_hand()
    
    def value(self):
        return self.hand.calc_value()

    def show_card(self):
        card = self.hand.cards[0]
        print(f"Dealer's hand: {card.get_face()}-{card.get_suit()}, ?????")

    def show_hand(self):
        print("Dealer's hand:", end=" ")
        self.hand.dprint()
        print()