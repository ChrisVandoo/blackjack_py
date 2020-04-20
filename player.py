import deck 

class Player():
    #creates player with $10 and no cards
    def __init__(self):
        self.money = 10
        self.hand = deck.Hand()

    #checks if player has enough to place bet, returns -1 if he doesnt
    def bet(self, amount):
        if self.money < amount or amount < 1:
            return False
        else:
            self.money = self.money - amount
            return True

    #returns amount of money the player has
    def wallet(self):
        return self.money

    #updates the result of a bet
    def update_money(self, result):
        self.money = self.money + result
    
    #adds a card to the players hand
    #TODO do something if false is returned?
    def add_card(self, card):
        return self.hand.add_card(card)
    
    #removes all cards from the players hand
    def clear_hand(self):
        self.hand.empty_hand()
