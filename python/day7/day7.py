import fileinput
import functools

lines = [line.strip() for line in fileinput.input(files="day7-input.txt")]


class Hand:
  def __init__(self, cardValues: list[int], handRank: int, bid: int):
    self.cardValues = cardValues
    self.typeRank = handRank
    self.bid = bid

  def __str__(self):
    return f'(cards: {self.cardValues}, typeRank: {self.typeRank}, bid: {self.bid})'

  def __repr__(self):
    return f'(cards: {self.cardValues}, typeRank: {self.typeRank}, bid: {self.bid})'


def card2Value(symbol: str):
  if symbol.isdecimal():
    return int(symbol)
  elif symbol == 'T':
    return 10
  elif symbol == 'J':
    return 11
  elif symbol == 'Q':
    return 12
  elif symbol == 'K':
    return 13
  elif symbol == 'A':
    return 14


def hand2TypeRank(cardValues: list[int]):
  card2Count: dict[int, int] = {}
  for cardValue in cardValues:
    valueCount = card2Count.get(cardValue)
    if valueCount is None:
      valueCount = 1
    else:
      valueCount += 1
    card2Count[cardValue] = valueCount

  if len(card2Count.keys()) == 1:
    # Five of kind
    return 1000
  elif len(card2Count.keys()) == 2:
    if max(card2Count.values()) == 4:
      # Four of kind
      return 800
    else:
      # Full house
      return 600
  elif len(card2Count.keys()) == 3:
    if max(card2Count.values()) == 3:
      # Three of kind
      return 400
    else:
      # Two pairs
      return 300
  elif len(card2Count.keys()) == 4:
    # One pairs
    return 200
  else:
    return 100


def line2Hand(line):
  bits = line.split(' ')
  cardValues = [card2Value(character) for character in bits[0]]
  cardTypeRank = hand2TypeRank(cardValues)
  cardBid = int(bits[1])
  return Hand(cardValues, cardTypeRank, cardBid)


# Round 1

def compareByCardsOrder(hand1: Hand, hand2: Hand):
  for cardValue1, cardValue2 in zip(hand1.cardValues, hand2.cardValues):
    if cardValue1 < cardValue2:
      return -1
    elif cardValue1 > cardValue2:
      return 1
  return 0


def comparatorFn(hand1: Hand, hand2: Hand):
  if hand1.typeRank == hand2.typeRank:
    return compareByCardsOrder(hand1, hand2)
  elif hand1.typeRank < hand2.typeRank:
    return -1
  else:
    return 1


print(lines)
hands = [line2Hand(line) for line in lines]
print(hands)

sortedHands = sorted(hands, key=functools.cmp_to_key(comparatorFn))
print(sortedHands)

cardWinnings = [(index + 1) * hand.bid for index, hand in enumerate(sortedHands)]
print(cardWinnings)

for index, (hand, winning) in enumerate(zip(sortedHands, cardWinnings)):
  print(f'index: {index}, hand: {hand.cardValues}, typeRank: {hand.typeRank}, bid: {hand.bid}, RANK: {winning} ')

print(sum(cardWinnings))

# Round 2
print("round 2")
