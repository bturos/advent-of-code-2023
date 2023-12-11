# Round 1
import fileinput
import re


class Card:
  def __init__(self, cardNumber: int, winningNumbers: set[int],
      actualNumbers: set[int]):
    self.cardNumber = cardNumber
    self.winningNumbers = winningNumbers
    self.actualNumbers = actualNumbers
    self.hits = len(actualNumbers.intersection(winningNumbers))

  def __str__(self):
    return ("number: {number: d}, hits: {hits: d}"
            " winning: {winning}"
            " actual: {actual}\n").format(
        number=self.cardNumber, hits=self.hits, winning=self.winningNumbers,
        actual=self.actualNumbers)

  def __repr__(self):
    return ("number: {number: d}, hits: {hits: d}"
            " winning: {winning}"
            " actual: {actual}\n").format(
        number=self.cardNumber, hits=self.hits, winning=self.winningNumbers,
        actual=self.actualNumbers)


def readCard(cardNumber: int, cardLine: str):
  numberSets = cardLine[cardLine.find(':') + 1:].split('|')
  winningNumbers = [int(value) for value in
                    re.findall('[0-9]+', numberSets[0])]
  actualNumbers = [int(value) for value in
                   re.findall('[0-9]+', numberSets[1])]

  return Card(cardNumber, set(winningNumbers), set(actualNumbers))


allPoints = 0
for lineNumber, line in enumerate(fileinput.input(files="day4-input.txt")):
  strippedLine = line.strip('\n')
  card = readCard(lineNumber, strippedLine)
  hits = card.hits
  if hits > 0:
    allPoints += pow(2, hits - 1)

print(allPoints)

# Round 2
cards: dict[int, Card] = {}
for lineNumber, line in enumerate(fileinput.input(files="day4-input.txt")):
  strippedLine = line.strip('\n')
  cards[lineNumber + 1] = readCard(lineNumber + 1, strippedLine)

inputCards = cards.values()
outputCards = []
while len(inputCards) > 0:
  print(f'input cards: {len(inputCards)}')
#  print(f'input {inputCards}')
  wonCards = []
  for card in inputCards:
    cardNumber = card.cardNumber
    hits = card.hits
 #   print(f"hits: {hits} on card {card}")
    if hits > 0:
      for wonCardNumber in range(cardNumber + 1, cardNumber + hits + 1):
        if cards.get(wonCardNumber) is not None:
  #        print(f'collecting card {wonCardNumber} from card {cardNumber}')
          wonCards.append(cards[wonCardNumber])
  outputCards += inputCards
  inputCards = wonCards
  print(f'output cards: {len(inputCards)}')
  #print(f"output {outputCards}")

#print(outputCards)
print(len(outputCards))
