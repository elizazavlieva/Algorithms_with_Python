def buble_sort(numbers):
    collection_length = len(numbers)
    while collection_length != 0:
        collection_length -= 1
        for idx in range(collection_length):
            if numbers[idx] > numbers[idx + 1]:
                numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]

    return numbers


numbers = [int(x) for x in input().split()]
print(*buble_sort(numbers), sep=' ')