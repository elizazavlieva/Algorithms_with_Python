def numbers(n, nums, index):
    if index >= len(nums):
        print(*nums, sep=' ')
        return
    for i in range(1, n + 1):
        nums[index] = i
        numbers(n, nums, index + 1)


n = int(input())
nums = [None] * n
numbers(n, nums, 0)