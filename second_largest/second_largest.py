nums = [10, 5, 10]
# nums = [10, 20, 40, 30, 50]

# Initialize two variables with negative infinity
first = second = float('-inf')

for num in nums:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second Largest:", second)
