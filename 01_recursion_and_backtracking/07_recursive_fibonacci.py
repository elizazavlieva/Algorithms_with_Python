def fib_solution(number):
    fib_one = 1
    fib_two = 1
    result = 0
    for _ in range(number - 1):
        result = fib_one + fib_two
        fib_one = fib_two
        fib_two = result
    return result


n = int(input())
print(fib_solution(n))