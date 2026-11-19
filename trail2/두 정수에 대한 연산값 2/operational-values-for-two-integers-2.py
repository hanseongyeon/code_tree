a, b = map(int, input().split())

# Please write your code here.
def calculate(num1, num2):
    if num1 > num2:
        num1 *= 2
        num2 += 10
    else:
        num1 += 10
        num2 *= 2
    return num1, num2

a, b = calculate(a, b)
print(a, b)