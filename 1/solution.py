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

# part 1 solution
print(max(elves))

elves.sort()

totalElves = len(elves)

# part 2 solution
print(sum(elves[totalElves - 3 : totalElves]))
