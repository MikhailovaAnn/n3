def find_missing_nums(nums):
    normal_array = [i for i in range(1, k + 1)]
    sum = list(filter(lambda i: i not in nums, normal_array))
    return sum
