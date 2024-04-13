def calculate_sum(numbers, index):
    if len(numbers) - 1 == index:
        return numbers[index]

    return numbers[index] + calculate_sum(numbers, index + 1)


nums = [int(x) for x in input().split(" ")]
print(calculate_sum(nums, 0))
