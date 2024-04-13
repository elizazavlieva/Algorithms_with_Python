def vector_generator(index, vector):
    if index >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[index] = num
        vector_generator(index + 1, vector)


n = int(input())
vector = [None] * n
vector_generator(0, vector)
