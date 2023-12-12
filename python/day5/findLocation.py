import re


class RangeMapping:
  def __init__(self, srcStart: int, destStart: int, rangeSize: int):
    if not all(
        isinstance(val, int) for val in [srcStart, destStart, rangeSize]):
      raise TypeError("All parameters must be integers")

    self.srcStart: int = srcStart
    self.destStart: int = destStart
    self.rangeSize: int = rangeSize

  def __str__(self):
    return f'(src: {self.srcStart} dest: {self.destStart} range: {self.rangeSize})'

  def __repr__(self):
    return f'(src: {self.srcStart} dest: {self.destStart} range: {self.rangeSize})'

  def isMapped(self, sourceMappingIndex: int):
    return self.srcStart <= sourceMappingIndex < (
        self.srcStart + self.rangeSize)

  def getDest(self, src: int):
    return src - self.srcStart + self.destStart


def loadMappings(lines: list[str]):
  seed2Soil: list[RangeMapping] = []
  soil2Fertilizer: list[RangeMapping] = []
  fertilizer2Water: list[RangeMapping] = []
  water2Light: list[RangeMapping] = []
  light2Temperature: list[RangeMapping] = []
  temperature2Humidity: list[RangeMapping] = []
  humidity2Location: list[RangeMapping] = []

  mappingsChainList: list[list[RangeMapping]] = [
    seed2Soil,
    soil2Fertilizer,
    fertilizer2Water,
    water2Light,
    light2Temperature,
    temperature2Humidity,
    humidity2Location
  ]

  mappingsChainIndex = -1
  for line in lines:
    line = line.strip()
    if line.find('map') != -1:
      mappingsChainIndex += 1
    elif len(line) > 0:
      mapping = [int(value) for value in re.findall('[0-9]+', line)]
      mappingsChainList[mappingsChainIndex].append(
          RangeMapping(mapping[1], mapping[0], mapping[2]))

  # print(seed2Soil)
  # print(soil2Fertilizer)
  # print(fertilizer2Water)
  # print(water2Light)
  # print(light2Temperature)
  # print(temperature2Humidity)
  # print(humidity2Location)

  return mappingsChainList


def findLocation(mappingsChainList: list[list[RangeMapping]], seed: int):
  #print(f'seed: {seed}')
  mappingsChainIndex = 0
  src: int = seed
  dest = -1
  while mappingsChainIndex < len(mappingsChainList):
    # print(f'source is {src}')
    for mapping in mappingsChainList[mappingsChainIndex]:
      if mapping.isMapped(src):
        dest = mapping.getDest(src)
    if dest == -1:
      dest = src
    mappingsChainIndex += 1
    src = dest
    # print(f'dest is {dest}')

  return src
