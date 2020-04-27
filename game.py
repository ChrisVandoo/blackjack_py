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

    #shows wallet, allows player to repeat this as much as wanted
    while action == 2:
        if action == 2:
            print(f"Wallet contains ${my_player.wallet()}")
        action = main_menu()

    while action == 1:
        my_deck.shuffle()

        #gives the player 2 cards and the dealer 2 cards
        my_player.add_card(my_deck.deal())
        my_dealer.add_card(my_deck.deal())
        my_player.add_card(my_deck.deal())
        my_dealer.add_card(my_deck.deal())

        #shows cards that have been dealt, need to show one dealer card
        display_player_cards(my_player)
        display_dealer_cards(my_dealer, False)

        #this allows the player to place a bet
        bet_amt = place_bet(my_player)

        #player can decide to add more cards until they bust
        action = play_action()
        player_bust = False
        while action == 1:
            if my_player.add_card(my_deck.deal()):
                display_player_cards(my_player)
                action = play_action()
            else:
                #TODO round should end if player busts
                print("You busted!")
                display_player_cards(my_player)
                action = 2
                player_bust = True
        
        #calculates dealers hand
        if player_bust is False:
            dealer_bust = dealer_action(my_dealer, my_deck)
        else:
            dealer_bust = False

        #display all cards in dealers hand
        display_dealer_cards(my_dealer, True)

        if dealer_bust:
            #player wins
            print("Dealer busted!")
            my_player.update_money(bet_amt)
            print(f"You win :) Your wallet contains ${my_player.wallet()}.")
        elif player_bust:
            #dealer wins
            my_player.update_money(-bet_amt)
            print(f"You lost :( Your wallet contains ${my_player.wallet()}.")
        else:
            #calculate who wins
            if my_dealer.value() == my_player.value():
                #tie, return player bet
                print(f"You tied with the dealer :| Your wallet contains ${my_player.wallet()}.")
            elif my_dealer.value() > my_player.value():
                #dealer wins
                my_player.update_money(-bet_amt)
                print(f"You lost :( Your wallet contains ${my_player.wallet()}.")
            else:
                #player wins
                my_player.update_money(bet_amt)
                print(f"You win :) Your wallet contains ${my_player.wallet()}.")

        #ends round by clearing out players hands
        my_player.clear_hand()
        my_dealer.clear_hand()

        #allows player to exit or play again
        action = main_menu()
        #shows wallet, allows player to repeat this as much as wanted
        while action == 2:
            if action == 2:
                print(f"Wallet contains ${my_player.wallet()}")
            action = main_menu()

    #print out stats, num rounds, total winnings..., #blackjacks (reached 21)
    print(f"Total winnings: ${my_player.wallet() - 10}")

def dealer_action(my_dealer, my_deck):
    bust = False
    #checks if dealer has an ace
    ace = my_dealer.hand.has_ace()

    #rule for "soft" 17
    if ace is True and my_dealer.value() == 17:
        my_dealer.add_card(my_deck.deal())

    #plays dealers hand
    while my_dealer.value() < 17 and bust is False:
        my_dealer.add_card(my_deck.deal())
        if my_dealer.value() > 21:
            bust = True

    return bust

def display_dealer_cards(my_dealer, end):
    if end:
        #prints out all cards in dealers hand for end of game
        my_dealer.show_hand()
    else:
        #prints out single card
        my_dealer.show_card()


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
    print("         Play:   1")
    print("         Wallet: 2")
    print("         Exit:   3")
    print("------------------------------")
    valid = False
    while not valid:
        try:
            val = int(input(">"))
            if val == 1 or val == 2 or val == 3:
                valid = True  
            else:
                valid = False
                print("Please enter 1, 2 or 3!")
        except ValueError:
            print("Please enter 1, 2 or 3!")
    return val

def main():
    the_game()

if __name__ == "__main__":
    main()
