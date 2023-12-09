import fileinput


### Round 1
def charAsCipher(c: str):
  return ord(c) - 48


def calculateValueForLine(line: str):
  characters = line.strip('\n')
  ciphers = list(filter(lambda c: c.isdigit(), [*characters]))
  noOfCiphers = len(ciphers)
  if noOfCiphers == 0:
    return 0
  elif noOfCiphers == 1:
    return charAsCipher(ciphers[0]) * 10 + charAsCipher(ciphers[0])
  else:
    return charAsCipher(ciphers[0]) * 10 + charAsCipher(
        ciphers[noOfCiphers - 1])


def calculateCiphersOnly():
  calibrationValue = 0

  for line in fileinput.input(files=('day1-input.txt')):
    calibrationValue += calculateValueForLine(line)

  return calibrationValue


### Round 2
numbersAsCiphers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
numbersAsText = (
  'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
)
possibleNumbers = numbersAsCiphers + numbersAsText

candidateStrings2Values: dict[str, int] = {
  '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
  '0': 0,
  'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
  'eight': 8, 'nine': 9
}


def findAllNumberLocations(line: str):
  locationsMap = {}
  for candidateString in possibleNumbers:
    firstNumberIndex = line.find(candidateString)
    if firstNumberIndex > -1:
      locationsMap[firstNumberIndex] = candidateString
    lastNumberIndex = line.rfind(candidateString)
    if lastNumberIndex > -1:
      locationsMap[lastNumberIndex] = candidateString

  return locationsMap


def calculateValueForLineWithNames(line: str):
  locationsMap = findAllNumberLocations(line)
  locationIndices = list(locationsMap.keys())

  if len(locationIndices) == 0:
    return 0
  elif len(locationIndices) == 1:
    foundNumber = candidateStrings2Values[locationsMap[locationIndices[0]]]
    return foundNumber * 10 + foundNumber
  else:
    firstNumber = candidateStrings2Values[locationsMap[min(locationIndices)]]
    lastLocation = candidateStrings2Values[locationsMap[max(locationIndices)]]
    return firstNumber * 10 + lastLocation


def calculateNamesToo():
  calibrationValue = 0

  for line in fileinput.input(files=('day1-input.txt')):
    cv = calculateValueForLineWithNames(line.strip('\n'))
    calibrationValue += cv

  return calibrationValue

print(calculateCiphersOnly())
print(calculateNamesToo())
