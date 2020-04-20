import deck 
import dealer
import player 

def the_game():
    #init elements of the game
    my_dealer = dealer.Dealer()
    my_player = player.Player()
    my_deck = deck.Deck()

    #asks player if they want to play again or else exit
    action = main_menu()
    while action == 1:
        my_deck.shuffle()

        #gives the player 2 cards and the dealer 2 cards
        my_player.add_card(my_deck.deal())
        my_dealer.add_card(my_deck.deal())
        my_player.add_card(my_deck.deal())
        my_dealer.add_card(my_deck.deal())
        #shows cards that have been dealt
        display_player_cards(my_player)

        #this allows the player to place a bet
        bet_amt = place_bet(my_player)

        #player can decide to add more cards until they bust
        action = play_action()
        while action == 1:
            if my_player.add_card(my_deck.deal()):
                display_player_cards(my_player)
                action = play_action()
            else:
                #TODO round should end if player busts
                print("You busted!")
                display_player_cards(my_player)
                action = 2

        #ends round by clearing out players hands
        my_player.clear_hand()
        my_dealer.clear_hand()

        #allows player to exit or play again
        action = main_menu()

        

def play_action():
    print("--- Please Enter a Number ---")
    print("         Hit: 1")
    print("         Stand: 2")
    print("------------------------------")
    valid = False
    while not valid:
        try:
            val = int(input(">"))
            if val == 1 or val == 2:
                valid = True
            else:
                valid = False
                print("Please enter 1 or 2!")
        except ValueError:
            print("Please enter 1 or 2!")
    return val

#this function accepts the players bet, checks if it is valid and returns amt of bet
def place_bet(my_player):
    print("Please enter bet:")
    valid = False 
    while not valid:
        try:
            amt = int(input(">"))
            if my_player.bet(amt):
                valid = True 
            else:
                valid = False
                print(f"Your wallet only contains ${my_player.wallet()}, bet less than this amount (and more than nothing):") 
        except ValueError:
            print("Please enter a valid number!")
    return amt

def display_player_cards(my_player):
    print("You have:", end=" ")
    my_player.hand.dprint()
    print()

def main_menu():
    print("--- Please Enter a Number ---")
    print("         Play: 1")
    print("         Exit: 2")
    print("------------------------------")
    valid = False
    while not valid:
        try:
            val = int(input(">"))
            if val == 1 or val == 2:
                valid = True  
            else:
                valid = False
                print("Please enter 1 or 2!")
        except ValueError:
            print("Please enter 1 or 2!")
    return val

def main():
    the_game()

if __name__ == "__main__":
    main()
