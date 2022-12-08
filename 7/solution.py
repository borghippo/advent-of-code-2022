from collections import defaultdict

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

sizes = defaultdict(int)
path = []
for line in lines:
    curr = line.split()
    if curr[0] == "$" and curr[1] == "cd":
        if curr[2] == "/":
            path.append("/")
        elif curr[2] == "..":
            last = path.pop()
        else:
            currPath = path[-1]
            slash = "/" if path[-1] == "/" else ""
            dir = curr[2]
            newPath = currPath + slash + dir
            path.append(newPath)
    elif curr[0].isnumeric():
        for i in path:
            sizes[i] += int(curr[0])

print(sum(size for size in sizes.values() if size <= 100000))
print(
    min(size for size in sizes.values() if size >= 30000000 - (70000000 - sizes["/"]))
)
