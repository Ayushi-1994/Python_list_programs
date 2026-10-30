nums = [10, 20, 40, 30, 50]

# Initialize two variables with negative infinity
# first = second = float('-inf')
first = second = nums[0]

for num in nums:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second Largest:", second)
