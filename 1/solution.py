with open("input.txt") as f:
    lines = f.readlines()

elves = []
currElfCal = 0
for line in lines:
    if line != "\n":
        currElfCal += int(line)
    else:
        elves.append(currElfCal)
        currElfCal = 0

print(max(elves))

elves.sort()

totalElves = len(elves)

print(sum(elves[totalElves - 3 : totalElves]))
