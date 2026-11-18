a, b = map(int, input().split())

# Please write your code here.
def calculate(num1, num2):
    if num1 < num2:
        num1 *= 2
        num2 += 25
    else:
        num2 *= 2
        num1 += 25

    return  num1, num2

a, b = calculate(a, b)
print(a, b)