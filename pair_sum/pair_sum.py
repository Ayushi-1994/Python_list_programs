nums = [2, 7, 11, 15]
target = 9

# seen = []
seen = set()

for num in nums:
    complement = target - num

    if complement in seen:
        print(complement, num)

    # seen.append(num)
    seen.add(num)
