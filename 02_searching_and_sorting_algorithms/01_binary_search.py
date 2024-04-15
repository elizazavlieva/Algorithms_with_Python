def binary_search(numbers, target):
    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2
        element = numbers[mid]
        if element == target:
            return mid
        elif element > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


numbers = [int(x) for x in input().split()]
target = int(input())


print(binary_search(numbers, target))


# Solution with recursion

def binary_search(start, end, numbers, target):
    if start > end:
        return -1

    mid = (start + end) // 2
    if numbers[mid] == target:
        return mid

    elif numbers[mid] > target:
        return binary_search(start, mid - 1, numbers, target)

    else:
        return binary_search(mid + 1, end, numbers, target)


numbers = [int(x) for x in input().split()]
target = int(input())
print(binary_search(0, len(numbers) - 1, numbers, target))
