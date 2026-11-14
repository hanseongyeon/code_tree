n, m = map(int, input().split())

# Please write your code here.
def least_common_multiple(num1, num2):
    start = max(num1, num2)
    for i in range(start, 10000):
        if i%num1 == 0 and i%num2 == 0:
            print(i)
            break

least_common_multiple(n, m)