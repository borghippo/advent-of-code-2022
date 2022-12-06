with open("input.txt") as f:
    lines = f.read().strip().split("\n")

stacks = [[] for _ in range(9)]
endOfStacks = 0

for i in range(len(lines)):
    if lines[i] == " 1   2   3   4   5   6   7   8   9 ":
        endOfStacks += 1
        break
    for c in range(1, len(lines[i]), 4):
        if lines[i][c] != " ":
            stacks[c // 4].insert(0, lines[i][c])
    endOfStacks += 1

for i in range(endOfStacks + 1, len(lines)):
    ins = lines[i].split(" ")
    amount = int(ins[1])

    f = stacks[int(ins[3]) - 1]
    t = stacks[int(ins[5]) - 1]

    t += f[len(f) - amount : len(f)]
    del stacks[int(ins[3]) - 1][len(f) - amount : len(f)]

ans = ""

for stack in stacks:
    if stack:
        ans += stack[len(stack) - 1]

print(ans)
