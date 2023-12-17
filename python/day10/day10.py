import fileinput
from enum import Enum, IntEnum


class Move(IntEnum):
  South = 1
  East = 2
  West = 3
  North = 4
  End = 5
  DeadEnd = 6


class PipeType(Enum):
  Start = 0
  Nothing = 1
  NS = 2
  WE = 3
  NW = 4
  NE = 5
  SW = 6
  SE = 7


class Coords:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

  def __hash__(self):
    return self.x * 13 + self.y * 31

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __str__(self):
    return f'(x: {self.x} y: {self.y})'

  def __repr__(self):
    return f'(x: {self.x} y: {self.y})'

  def executeMove(self, move: Move):
    if move == Move.South:
      return Coords(self.x, self.y + 1)
    elif move == Move.West:
      return Coords(self.x - 1, self.y)
    elif move == Move.East:
      return Coords(self.x + 1, self.y)
    elif move == Move.North:
      return Coords(self.x, self.y - 1)


def character2PipeType(character: str):
  if character == '|':
    return PipeType.NS
  elif character == '-':
    return PipeType.WE
  elif character == 'L':
    return PipeType.NE
  elif character == 'J':
    return PipeType.NW
  elif character == '7':
    return PipeType.SW
  elif character == 'F':
    return PipeType.SE
  elif character == 'S':
    return PipeType.Start
  elif character == '.':
    return PipeType.Nothing
  else:
    raise Exception(f'Invalid symbol detected: {character}')


def pipe2OutMove(pipeType: PipeType, inMove: Move):
  if pipeType == PipeType.Start:
    return Move.End
  elif pipeType == PipeType.Nothing:
    return Move.DeadEnd
  elif pipeType == PipeType.NS:
    if inMove == Move.South:
      return Move.South
    elif inMove == Move.North:
      return Move.North
    else:
      return Move.DeadEnd
  elif pipeType == PipeType.WE:
    if inMove == Move.East:
      return Move.East
    elif inMove == Move.West:
      return Move.West
  elif pipeType == PipeType.NW:
    if inMove == Move.South:
      return Move.West
    elif inMove == Move.East:
      return Move.North
    else:
      return Move.DeadEnd
  elif pipeType == PipeType.NE:
    if inMove == Move.South:
      return Move.East
    elif inMove == Move.West:
      return Move.North
    else:
      return Move.DeadEnd
  elif pipeType == PipeType.SE:
    if inMove == Move.North:
      return Move.East
    elif inMove == Move.West:
      return Move.South
    else:
      return Move.DeadEnd
  elif pipeType == PipeType.SW:
    if inMove == Move.North:
      return Move.West
    elif inMove == Move.East:
      return Move.South
    else:
      return Move.DeadEnd


# filename = 'day10-test-input1.txt'
# filename = 'day10-test-input2.txt'
#filename = 'day10-test-input3.txt'
# filename = 'day10-test-input4.txt'
filename = 'day10-input.txt'
lines: list[str] = [line.strip() for line in fileinput.input(files=filename)]

start: Coords = Coords(0, 0)
coordinates: dict[Coords, PipeType] = {}
for lineIndex, line in enumerate(lines):
  for charIndex, character in enumerate(line):
    pipeType = character2PipeType(character)
    coordinates[Coords(charIndex, lineIndex)] = pipeType
    if pipeType == PipeType.Start:
      start = Coords(charIndex, lineIndex)
  print(f'number: {lineIndex} line: {line}')

print(coordinates)
print(f'start: {start}')


# Round 1
def buildPath(coordinates: dict[Coords, PipeType], startCoords: Coords,
    startMove: Move):
  coords2Distance: list[Coords] = []

  print('path')

  currentCoords = startCoords
  nextMove = startMove
  while currentCoords != startCoords or len(coords2Distance) == 0:
    nextCoords = currentCoords.executeMove(nextMove)
    currentPipe = None
    if coordinates.get(nextCoords) != None:
      currentPipe = coordinates[nextCoords]
    else:
      return None
    outMove = pipe2OutMove(currentPipe, nextMove)
    print(
      f'coords: {currentCoords} -> {nextCoords}, pipe: {currentPipe}, move: {nextMove}')

    if outMove == Move.DeadEnd:
      coords2Distance.append(nextCoords)
      return None
    elif outMove == Move.End:
      coords2Distance.append(nextCoords)
      return coords2Distance
    else:
      coords2Distance.append(currentCoords)
      nextMove = outMove
      currentCoords = nextCoords

  if len(coords2Distance) > 2:
    return coords2Distance
  else:
    return None


paths = [
  buildPath(coordinates, start, Move.West),
  buildPath(coordinates, start, Move.North),
  buildPath(coordinates, start, Move.East),
  buildPath(coordinates, start, Move.South)
]

print(paths)

maxDistances = [len(path) / 2 if len(path) % 2 == 0 else (len(path) - 1) / 2 for
                path in filter(lambda path: path != None, paths)]
print(maxDistances)
