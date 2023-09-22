import random 

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
playing = True

class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    
class Deck:
    
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in SUITS:
            for rank in RANKS:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()        
    
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Hand:
    
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += VALUES[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet'))
        except ValueError:
            print('The bet must be an integer')
        else:
            if chips.bet > chips.total:
                print('Your bet cannot be more than', chips.total)
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to hit or stand? 'h' or 's'")

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('Player stands. Dealer now plays')
            playing = False
        else:
            print('Pleaes try again')
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(chips):
    print('Player busts!')
    chips.lose_bet()

def player_wins(chips):
    print('Player wins!')
    chips.win_bet()

def dealer_busts(chips):
    print('Dealer busts!')
    chips.lose_bet()

def dealer_wins(chips):
    print('Dealer wins')
    chips.lose_bet()

def push():
    print('Dealer and Player tie! It is a push') 


if __name__ == '__main__':
    game_over = False
    # Let's play black jack
    while not game_over:
        print('Welcome to black jack!')

        the_deck = Deck()
        the_deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(the_deck.deal_one())
        player_hand.add_card(the_deck.deal_one())

        dealer_hand = Hand()
        dealer_hand.add_card(the_deck.deal_one())
        dealer_hand.add_card(the_deck.deal_one())

        player_chips = Chips()

        # Take the bet from the player
        bet(player_chips)

        show_some(player_hand, dealer_hand)

        while playing:
            hit_or_stand(the_deck, player_hand)
            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_chips)
                break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(the_deck, dealer_hand)

            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_chips)
            else:
                push()
        
        print('Player has winnings of', player_chips.total)

        new_game = input('Would you like to play again? \'y\' or \'n\'')

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print('Thanks for playing')
            break


        
        

        
        
