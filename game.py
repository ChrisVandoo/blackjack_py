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
        my_player.hand.dprint()
        action = main_menu()

        my_player.clear_hand()
        my_dealer.clear_hand()


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
