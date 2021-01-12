"""
Challenge #3:

Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20

Notes:
- Bonus: Try to complete this challenge in one line!
"""


def multiply_nums(nums):
    if nums == "":
        return "input is empty"
    nums_list = nums.split(", ")
    result = 1
    for num in nums_list:
        result *= int(num)
    return result

print(multiply_nums("2, 3"))
print(multiply_nums("1, 2, 3, 4"))

