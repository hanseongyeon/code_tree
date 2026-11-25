N = int(input())

# Please write your code here.
def fibonacci(num):
    if num == 1:
        return 1
    if num == 2:
        return 1

    return fibonacci(num-2) + fibonacci(num-1)

print(fibonacci(N))