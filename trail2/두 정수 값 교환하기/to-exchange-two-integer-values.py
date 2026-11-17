n, m = map(int, input().split())

# Please write your code here.
def swap(num1, num2):
    num1, num2 = num2, num1
    return num1, num2

n, m = swap(n, m)
print(n, m)