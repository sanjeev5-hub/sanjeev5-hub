def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib(n -1 ) + fib(n - 2)

nums = [fib(i) for i in range(10)]
print(nums)
