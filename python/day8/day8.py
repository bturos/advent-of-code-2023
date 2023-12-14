import fileinput
import re

# filename = 'day8-test-input-rl.txt'
# filename = 'day8-test-input-llr.txt'
filename = 'day8-input.txt'
lines = [line.strip() for line in fileinput.input(files=filename)]

moves = lines[0]
print(moves)

pattern = re.compile(r'(?P<term>[A-Z]{3})')


# Round 1
def loadEdgesFromLine(line: str):
  matches = list([result.groups()[0] for result in re.finditer(pattern, line)])
  return matches


def createMoveMaps(edges: list[(str, str, str)]):
  rightMoves = {}
  leftMoves = {}

  for node, leftEdge, rightEdge in edges:
    rightMoves[node] = rightEdge
    leftMoves[node] = leftEdge

  return (rightMoves, leftMoves)


def executeMoves(moves: list[str], rightMoves: dict[str, str],
    leftMoves: dict[str, str]):
  currentNode = 'AAA'
  moveNumber = 0
  totalMovesNumber = 0

  while moveNumber < len(moves):
    totalMovesNumber += 1
    nextNode = rightMoves[currentNode] if moves[moveNumber] == 'R' else \
    leftMoves[currentNode]
    # print(f'move number: {moveNumber}')
    # print(f'move: {moves[moveNumber]}')
    # print(f'next node: {nextNode}')

    if nextNode == 'ZZZ':
      print(f'returning on move {totalMovesNumber}')
      return totalMovesNumber
    else:
      currentNode = nextNode

    if (moveNumber == len(moves) - 1):
      print(f'resetting moves sequence, reached {len(moves)}')
      moveNumber = 0
    else:
      moveNumber += 1
  return totalMovesNumber


edges = [loadEdgesFromLine(line) for line in lines[2:]]
rightMoves, leftMoves = createMoveMaps(edges)

movesCount = executeMoves([move for move in moves], rightMoves, leftMoves)
print(movesCount)
