from random import shuffle
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six',
         'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):

        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
       #   CREATE LIST
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # CREATE THE CARDS OBJECT
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # Note this doesn't return anything
        shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        # we remove one cards from the list of the top
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {self.all_cards} cards.'


player_one = Player("Player one: Mikiyas")
player_two = Player("Player two: Beba")
new_deck = Deck()
new_deck.shuffle()
# Split the Deck between players
len(new_deck.all_cards) / 2

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f"Round {round_num}")
    # check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print('Player one, out of cards, Player two win!!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player two, out of cards, Player one win!!')
        game_on = False
        break
    # Start a new game round and reset the cards, on the table
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # otheerwise, game is continue
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            # No longer at "war", time for the next round
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            # No longer at "war", time for the next round
            at_war = False

        else:
            print('WAR!!')
            # This occure the card values are equal.
            # Will grab another cards each players continue the current war.

            # First check the player has enough cards to play

            if len(player_one.all_cards) < 5:
                print("Player one unable to play war!!")
                print("Player two Win! Player one losses.")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player two unable to play war!!")
                print("Player one Win! Player two losses.")
                game_on = False
                break
            # otherwise , we are still at war, add another cards on the table
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
