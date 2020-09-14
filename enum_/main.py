import enum

class Suit(enum.Enum):
  diamond = enum.auto()
  heart = enum.auto()
  spade = enum.auto()
  club = enum.auto()

class Rank(enum.Enum):
  TWO = enum.auto()
  THREE = enum.auto()
  FOUR = enum.auto()
  FIVE = enum.auto()
  SIX = enum.auto()
  SEVEN = enum.auto()
  EIGHT = enum.auto()
  NINE = enum.auto()
  TEN = enum.auto()
  JACK = enum.auto()
  QUEEN = enum.auto()
  KING = enum.auto()
  ACE = enum.auto()

class Card:
  def __init__(self, suit: Suit, rank: Rank):
    self.suit = suit
    self.rank = rank
  
  @property
  def suit(self):
    return self._suit

  @property
  def rank(self):
    return self._rank

  @suit.setter
  def suit(self, suit: Suit):
    if suit not in Suit:
      raise Exception
    self._suit = suit

  @rank.setter
  def rank(self, rank: Rank):
    if rank not in Rank:
      raise Exception
    self._rank = rank

  def __repr__(self):
    return f'Card({self.rank} of {self.suit})'

class Deck:
  def __init__(self):
    self._diamond = [Card(Suit.diamond,r) for r in Rank]
    self._heart = [Card(Suit.heart,r) for r in Rank]
    self._spade = [Card(Suit.spade,r) for r in Rank]
    self._club = [Card(Suit.club,r) for r in Rank]

def main():
  test = Deck()

if __name__ == '__main__':
  main()