# Round 1
# 12 red cubes
# 13 green cubes
# 14 blue cubes

import fileinput


def isGamePossible(red: int, green: int, blue: int):
  return red < 13 and green < 14 and blue < 15


def grab2Counts(grab: str):
  redCount = 0
  greenCount = 0
  blueCount = 0

  for numberAndColor in grab.split(','):
    bits = numberAndColor.strip().split(' ')
    number = int(bits[0])
    if bits[1] == 'red':
      redCount = number
    elif bits[1] == 'green':
      greenCount = number
    elif bits[1] == 'blue':
      blueCount = number

  return (redCount, greenCount, blueCount)


def findPossibleGamesByMaximumCubeCount():
  possibleGameIndices = set()
  for line in fileinput.input(files=('day2-input.txt')):
    headerAndGrabs = line.strip('\n').split(':')
    gameIndex = int(headerAndGrabs[0].removeprefix('Game '))
    grabsLine = headerAndGrabs[1].removeprefix(' ')

    gameNotPossible = False
    for grab in grabsLine.split(';'):
      redCount, greenCount, blueCount = grab2Counts(grab)
      if not isGamePossible(redCount, greenCount, blueCount):
        gameNotPossible = True

    if (not gameNotPossible):
      possibleGameIndices.add(gameIndex)

  return possibleGameIndices


possibleGameIndices = findPossibleGamesByMaximumCubeCount()
print(possibleGameIndices)
print(int(sum(possibleGameIndices)))


def count2Power(count: int):
  if count == 0:
    return 1
  else:
    return count


def findGamesPowerByMinimumCubeCount():
  sumOfPowers = 0

  for line in fileinput.input(files=('day2-input.txt')):
    headerAndGrabs = line.strip('\n').split(':')
    grabsLine = headerAndGrabs[1].removeprefix(' ')

    maxRedCount = 0
    maxGreenCount = 0
    maxBlueCount = 0

    for grab in grabsLine.split(';'):
      redCount, greenCount, blueCount = grab2Counts(grab)
      if (maxRedCount < redCount):
        maxRedCount = redCount
      if (maxGreenCount < greenCount):
        maxGreenCount = greenCount
      if (maxBlueCount < blueCount):
        maxBlueCount = blueCount

    sumOfPowers += maxRedCount * maxGreenCount * maxBlueCount

  return sumOfPowers


print(findGamesPowerByMinimumCubeCount())
