# This is changes from the banch I created in github.
def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib(n -1 ) + fib(n - 2)

nums = [fib(i) for i in range(10)]
print(f"The nums is {nums}")
print("Bye")
print("Bye Bye")
print("MyBranch")


