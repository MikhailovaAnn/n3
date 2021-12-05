from random import randint

k = int(input())
nums = [randint(1, k) for i in range(1, k + 1)]
def find_missing_nums(nums):
    normal_array = [i for i in range(1, k + 1)]
    sum = list(filter(lambda i: i not in nums, normal_array))
    return sum
