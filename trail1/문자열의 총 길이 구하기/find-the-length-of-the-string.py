arr = list(map(str, input().split()))

cnt = 0
for i in arr:
    cnt += len(i)
print(cnt)