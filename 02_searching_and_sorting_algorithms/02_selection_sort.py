def selection_sort(numbers):
    for index in range(len(numbers)):
        current_num = numbers[index]
        min_index = index
        for num in range(index + 1, len(numbers)):
            if current_num > numbers[num]:

                min_index = num
                current_num = numbers[num]

        numbers[index], numbers[min_index] = numbers[min_index], numbers[index]

    return numbers


numbers = [int(x) for x in input().split()]

print(*selection_sort(numbers), sep=' ')
