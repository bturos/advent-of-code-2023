import fileinput
import re

from findLocation import loadMappings
from findLocation import findLocation

lines = [line for line in fileinput.input(files="day5-input.txt")]
seeds = [int(value) for value in re.findall('[0-9]+', lines[0])]
mappingsChain = loadMappings(lines[1:])

minLocation = min([findLocation(mappingsChain, seed) for seed in seeds])
print(minLocation)
