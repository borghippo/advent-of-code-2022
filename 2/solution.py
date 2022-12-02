with open("input.txt") as f:
    lines = f.readlines()

score = 0
score2 = 0

for line in lines:
    o, p = line.split()
    print(type((o, p)))
    score += {"X": 1, "Y": 2, "Z": 3}[p]
    score += {
        ("A", "X"): 3,
        ("A", "Y"): 6,
        ("A", "Z"): 0,
        ("B", "X"): 0,
        ("B", "Y"): 3,
        ("B", "Z"): 6,
        ("C", "X"): 6,
        ("C", "Y"): 0,
        ("C", "Z"): 3,
    }[(o, p)]
    score2 += {"X": 0, "Y": 3, "Z": 6}[p]
    score2 += {
        ("A", "X"): 3,
        ("A", "Y"): 1,
        ("A", "Z"): 2,
        ("B", "X"): 1,
        ("B", "Y"): 2,
        ("B", "Z"): 3,
        ("C", "X"): 2,
        ("C", "Y"): 3,
        ("C", "Z"): 1,
    }[(o, p)]

print(score)
print(score2)
