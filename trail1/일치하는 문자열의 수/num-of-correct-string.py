n, A = map(str, input().split())
n = int(n)
cnt = 0
for i in range(n):
    target = str(input())
    if A == target:
        cnt += 1

print(cnt)