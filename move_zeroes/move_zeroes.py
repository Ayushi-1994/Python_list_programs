nums = [1, 0, 2, 0, 3, 4]

result = []

for num in nums:
    if num != 0:
        result.append(num)

result.extend([0] * (len(nums) - len(result)))

print(result)
