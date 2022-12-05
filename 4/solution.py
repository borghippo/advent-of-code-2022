with open("input.txt") as f:
    lines = f.read().strip().split("\n")

total = 0
total2 = 0

lines = [line.split(",") for line in lines]

for line in lines:
    nums = line[0].split("-")
    nums2 = line[1].split("-")
    check = [int(nums[0]), int(nums[1])]
    check2 = [int(nums2[0]), int(nums2[1])]

    if (
        check2[0] >= check[0]
        and check2[1] <= check[1]
        or check[0] >= check2[0]
        and check[1] <= check2[1]
    ):
        total += 1

    if not (check[1] < check2[0] or check[0] > check2[1]):
        total2 += 1


print(total)
print(total2)
