import fileinput
import re

lines = [line for line in fileinput.input(files="day6-input.txt")]

# Round 1

def calculateNumberOfWayToBeatTheRecord(raceTimes: list[int],
    maxDistances: list[int]):
  recordBeatingSolutions = 1
  for (raceTime, maxDistance) in zip(raceTimes, maxDistances):
    betterDistanceCount = 0
    for holdTime in range(1, raceTime + 1):
      distanceReached = (raceTime - holdTime) * holdTime
      if distanceReached > maxDistance:
        betterDistanceCount += 1
    recordBeatingSolutions *= betterDistanceCount
  return recordBeatingSolutions

raceTimes = [int(value) for value in
             re.findall('[0-9]+', lines[0].removeprefix('Time:').strip())]
maxDistances = [int(value) for value in
                re.findall('[0-9]+',
                           lines[1].removeprefix('Distance:').strip())]
recordBeatingSolutions = calculateNumberOfWayToBeatTheRecord(raceTimes,
                                                             maxDistances)
print(f'solutions: {recordBeatingSolutions}')

# Round 2
raceTime = int(lines[0].removeprefix('Time:').replace(' ', '').strip())
maxDistance = int(lines[1].removeprefix('Distance:').replace(' ', '').strip())

print(raceTime)
print(maxDistance)

recordBeatingSolutions = calculateNumberOfWayToBeatTheRecord([raceTime], [maxDistance])
print(f'solutions: {recordBeatingSolutions}')
