import fileinput
import re
import time

from findLocation import loadMappings
from findLocation import findLocation

from joblib import Parallel, delayed

if __name__ == '__main__':
  lines = [line for line in fileinput.input(files="day5-input.txt")]
  mappingsChain = loadMappings(lines[1:])

  seeds = [int(value) for value in re.findall('[0-9]+', lines[0])]
  seeds = [seeds[i: i + 2] for i in range(0, len(seeds), 2)]
  seeds = [range(s[0], s[0] + s[1], 1) for s in seeds]

  startTime = time.time()
  globalMinLocation = -1
  for seedRange in seeds:
    print(f'start: {seedRange.start}, stop: {seedRange.stop}.stop, scope: {seedRange.stop - seedRange.start}')
    rangeStartTime = time.time()

    locations = Parallel(n_jobs=200, backend='threading')(delayed(findLocation)(mappingsChain, seed) for seed in seedRange)
    minLocation = min(locations)

    rangeEndTime = time.time()
    print(f'range execution time: {(rangeEndTime - rangeStartTime) / 1000}s')

    print(minLocation)
    if globalMinLocation == -1 or globalMinLocation > minLocation:
      globalMinLocation = minLocation

  endTime = time.time()
  print(f'total execution time: {(endTime - startTime) / 1000}s')
  print(f'global min location: {globalMinLocation}')
