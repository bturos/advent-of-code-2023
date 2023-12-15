import fileinput
import re

# filename = 'day9-test-input.txt'
filename = 'day9-input.txt'
lines = [line.strip() for line in fileinput.input(files=filename)]

allSequences = [[int(value) for value in re.findall(r'[-\d]+', line)] for line
                in
                lines]


# Round 1
def finalSequence(sequence: list[int]):
  return len(set(sequence)) == 1 and sequence[0] == 0


def findSequenceExtrapolatedValueFromSuffix(initialSequence: list[int]):
  lastSequenceValues: list[int] = []
  currentSequence = initialSequence
  while not finalSequence(currentSequence):
    print(currentSequence)
    lastSequenceValues.append(currentSequence[len(currentSequence) - 1])
    nextSequence = [currentValue - currentSequence[index - 1] for
                    index, currentValue in
                    enumerate(currentSequence) if index > 0]
    currentSequence = nextSequence
  lastSequenceValues.append(currentSequence[len(currentSequence) - 1])

  return sum(lastSequenceValues)


extrapolatedValues = [findSequenceExtrapolatedValueFromSuffix(sequence) for
                      sequence in
                      allSequences]
print(sum(extrapolatedValues))


# Round 2
def findSequenceExtrapolatedValueFromPrefix(initialSequence: list[int]):
  firstSequenceValues: list[int] = []
  currentSequence = initialSequence
  while not finalSequence(currentSequence):
    # print(currentSequence)
    firstSequenceValues.append(currentSequence[0])
    nextSequence = [currentValue - currentSequence[index - 1] for
                    index, currentValue in
                    enumerate(currentSequence) if index > 0]
    currentSequence = nextSequence

  firstSequenceValues.reverse()

  print(firstSequenceValues)

  currentValue = firstSequenceValues[0]
  for index, value in enumerate(firstSequenceValues):
    if index > 0:
      newCurrentValue = value - currentValue
      currentValue = newCurrentValue

  return currentValue


extrapolatedValues = [findSequenceExtrapolatedValueFromPrefix(sequence) for
                      sequence in
                      allSequences]
print(sum(extrapolatedValues))
