def drawing(n):
    if n == 0:
        return
    print('*' * n)  # pre-actions
    drawing(n - 1)  # recursive call
    print("#" * n)  # post-actions


num = int(input())
drawing(num)
