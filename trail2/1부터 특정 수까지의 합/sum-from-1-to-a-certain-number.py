n = int(input())

# Please write your code here.
sum = 0
def sum_program(num):
    global sum
    for i in range(1, num+1):
        sum += i
    sum //= 10
    return sum

ans = sum_program(n)
print(ans)