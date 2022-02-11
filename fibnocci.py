def sum(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return sum(n -1 ) + sum(n - 2)

nums = [sum(i) for i in range(10)]
print(nums)
