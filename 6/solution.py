with open("input.txt") as f:
    lines = f.read().strip().split("\n")

seq = lines[0]

unique = set()

ans = 0
ans2 = 0
foundFirst = False

l = 0
for r in range(len(seq)):
    if len(unique) == 4 and not foundFirst:
        ans = r
        foundFirst = True
    if len(unique) == 14:
        ans2 = r
        break
    if seq[r] in unique:
        while seq[r] in unique:
            unique.remove(seq[l])
            l += 1
    unique.add(seq[r])

print(ans)
print(ans2)
