a, b = map(int, input().split())

# Please write your code here.

def sum_primenum(num):
    cnt = 0
    for i in range(1, num+1):
        if num%i == 0:
            cnt +=1
    if cnt == 2:
        return num

ans = 0
for i in range(a, b+1):
    if sum_primenum(i):
        ans += i
print(ans)