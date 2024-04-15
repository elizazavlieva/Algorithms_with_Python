def left_or_right_left(result, side, side_idx):
    while side_idx < len(side):
        result.append(side[side_idx])
        side_idx += 1

    return result


def merge_arrays(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left:
        left_or_right_left(result, left, left_idx)
    if right:
        left_or_right_left(result,  right, right_idx)

    return result

def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid:]

    return merge_arrays(merge_sort(left), merge_sort(right))


numbers = [int(x) for x in input().split()]

print(*merge_sort(numbers), sep=' ')
