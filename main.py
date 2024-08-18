import collections
from random import choice

Card = collections.namedtuple('Card', ['suit', 'rank'])

class FrenchDeck:
    rank = [str(n) for n in range(2, 11)] + list('JKQA')
    suit = 'heart diamond spade club'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suit for rank in self.rank]
        
    def __len__(self):
        return len(self._cards)
        
    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()  # Create a deck of cards
print(len(deck))     # Print the number of cards in the deck (should be 52)
print(deck[0])       # Print the first card in the deck
print(deck[-1])      # Print the last card in the deck
print(choice(deck))
