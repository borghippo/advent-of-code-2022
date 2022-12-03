with open("input.txt") as f:
    lines = f.read().strip().split("\n")


def getVal(val):
    return ord(val) - 38 if val.isupper() else ord(val) - 96


total = 0

for line in lines:
    first = line[: len(line) // 2]
    second = line[len(line) // 2 :]

    val = set(first).intersection(set(second)).pop()

    total += getVal(val)

total2 = 0

for i in range(0, len(lines), 3):

    val = set(lines[i]).intersection(set(lines[i + 1]), set(lines[i + 2])).pop()

    total2 += getVal(val)

print(total)
print(total2)
