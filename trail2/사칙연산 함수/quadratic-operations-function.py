a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def calculate(num1, sign, num2):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1*num2
    elif sign == '/':
        return int(num1/num2)
    else:
        return False

if calculate(a, o, c):
    print(f'{a} {o} {c} = {calculate(a, o, c)}')
else:
    print(calculate(a, o, c))