nums = [10, 20, 5, 40, 25]

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print("Largest Element:", largest)
