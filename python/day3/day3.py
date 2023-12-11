import fileinput


# Round 1

class Position:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

  def __str__(self):
    return "(x: {x:d}, y: {y:d})".format(x=self.x, y=self.y)

  def __repr__(self):
    return "(x: {x:d}, y: {y:d})".format(x=self.x, y=self.y)

  def __hash__(self):
    return self.x * 13 + self.y * 31

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y


class NumberWithLocations:
  def __init__(self, value: int, positions: list[Position]):
    self.value = value
    self.positions = positions

  def __eq__(self, other):
    return self.value == other.value and self.positions == other.positions

  def __hash__(self):
    positionsHash = sum(list(map(lambda p: int(p.__hash__()), self.positions)))
    return self.value * 31 + 13 * positionsHash


def collectTokensInLine(line: str):
  tokenIndices: list[list[int]] = []
  currentTokenIndices: list[int] = []

  for index, character in enumerate(line):
    isDigit = character.isdecimal()
    isEngineSymbol = character != '.'

    if len(currentTokenIndices) == 0:
      if isDigit:
        currentTokenIndices.append(index)
      elif isEngineSymbol:
        tokenIndices.append([index])
    else:
      if isDigit:
        currentTokenIndices.append(index)
      else:
        tokenIndices.append(currentTokenIndices.copy())
        currentTokenIndices.clear()
        if isEngineSymbol:
          tokenIndices.append([index])

  if len(currentTokenIndices) > 0:
    tokenIndices.append(currentTokenIndices)

  return tokenIndices


def collectPositionsInLine(lineIndex: int, line: str):
  location2Symbol: dict[Position, str] = {}
  location2Number: dict[Position, NumberWithLocations] = {}

  lineTokenIndices: list[list[int]] = collectTokensInLine(line)
  for tokenIndices in lineTokenIndices:
    if not line[tokenIndices[0]].isdecimal():
      location2Symbol[Position(lineIndex, tokenIndices[0])] = line[
        tokenIndices[0]]
    else:
      startIndex = tokenIndices[0]
      endIndex = tokenIndices[len(tokenIndices) - 1]
      numberValue = int(line[startIndex:endIndex + 1])
      locationsForCurrentNumber = list(
          map(lambda ti: Position(lineIndex, ti), tokenIndices))
      numberWithLocations = NumberWithLocations(numberValue,
                                                locationsForCurrentNumber)
      for cipherLocation in locationsForCurrentNumber:
        location2Number[cipherLocation] = numberWithLocations

  return (location2Symbol, location2Number)


def findLocations(lines: enumerate[str]):
  symbolLocations: dict[Position, str] = {}
  numberLocations: dict[Position, NumberWithLocations] = {}

  for lineIndex, line in lines:
    strippedLine = line.strip('\n')
    lineSymbolLocations, lineNumberLocations = collectPositionsInLine(lineIndex,
                                                                      strippedLine)
    symbolLocations.update(lineSymbolLocations)
    numberLocations.update(lineNumberLocations)

  return (symbolLocations, numberLocations)


def findAdjacentPositions(symbolLocation: Position):
  return [
    Position(symbolLocation.x - 1, symbolLocation.y),
    Position(symbolLocation.x + 1, symbolLocation.y),
    Position(symbolLocation.x, symbolLocation.y - 1),
    Position(symbolLocation.x, symbolLocation.y + 1),
    Position(symbolLocation.x - 1, symbolLocation.y - 1),
    Position(symbolLocation.x - 1, symbolLocation.y + 1),
    Position(symbolLocation.x + 1, symbolLocation.y - 1),
    Position(symbolLocation.x + 1, symbolLocation.y + 1)
  ]


def findPartNumbers(symbolLocations: dict[Position, str],
    numberLocations: dict[Position, NumberWithLocations]):
  partNumbers: list[int] = list()
  for symbolLocation in symbolLocations:
    adjacentPositions = findAdjacentPositions(symbolLocation)
    adjacentPartNumbers = set()
    for position in adjacentPositions:
      possiblePartNumber = numberLocations.get(position)
      if possiblePartNumber is not None:
        adjacentPartNumbers.add(possiblePartNumber)
    partNumbers.extend([partNumber.value for partNumber in adjacentPartNumbers])

  return partNumbers


fileLines = enumerate(fileinput.input(files=('day3-input.txt')))
symbolLocations, numberLocations = findLocations(fileLines)

partNumbers = findPartNumbers(symbolLocations, numberLocations)
print(sum(partNumbers))

# Round 2

fileLines2 = enumerate(fileinput.input(files=('day3-input.txt')))
symbolLocations2, numberLocations2 = findLocations(fileLines2)


def findGearRatios(symbolLocations: dict[Position, str],
    numberLocations: dict[Position, NumberWithLocations]):
  gearRatios = list()

  for symbolLocation in symbolLocations:
    adjacentPartNumbers = set()
    adjacentPositions = findAdjacentPositions(symbolLocation)
    for position in adjacentPositions:
      possiblePartNumber = numberLocations.get(position)
      if possiblePartNumber is not None:
        adjacentPartNumbers.add(possiblePartNumber)
    adjacentPartNumbersList = list(adjacentPartNumbers)
    if len(adjacentPartNumbersList) == 2:
      gearRatios.append(
        adjacentPartNumbersList[0].value * adjacentPartNumbersList[1].value)
  return gearRatios


gearRatios = findGearRatios(symbolLocations2, numberLocations2)
print(gearRatios)
print(sum(gearRatios))
