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


new_deck = Deck()
new_deck.shuffle()
my_Card = new_deck.deal_one()
print(my_Card)
print(len(new_deck.all_cards))
print(new_deck.all_cards[0])
