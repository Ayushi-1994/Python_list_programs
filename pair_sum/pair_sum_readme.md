PROGRAM: Pair With Given Sum

PROBLEM:
Find two numbers whose sum equals target.

INPUT:
nums = [2, 7, 11, 15]
target = 9

OUTPUT:
2 7

LOGIC:
1. Store visited elements in a set.
2. For each element find complement = target - current.
3. If complement already exists, pair is found.
4. Otherwise add current element to set.

TIME COMPLEXITY:
O(n)

SPACE COMPLEXITY:
O(n)
