a, b = map(int, input().split())

# Please write your code here.\

def prime_number(num):
    cnt = 0
    for i in range(1, num):
        if num%i == 0:
            cnt += 1
    
    if cnt == 1:
        return True


def each_sum_even_num(num):
    sum = 0
    num = list(str(num))
    for i in num:
        sum += int(i)
    if sum%2 == 0:
        return True

ans = 0
for i in range(a, b+1):
    if prime_number(i) and each_sum_even_num(i):
        ans += 1

print(ans)