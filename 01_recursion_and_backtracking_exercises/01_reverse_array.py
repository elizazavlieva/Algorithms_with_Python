def reversed_array(numbers, result):

    if len(numbers) == 0:
        print(" ".join(result))
        return
    result.append(numbers.pop())
    reversed_array(numbers, result)


nums = input().split()

reversed_array(nums, [])
