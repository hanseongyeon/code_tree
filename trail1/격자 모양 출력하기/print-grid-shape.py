N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
ans = [[0]*N for _ in range(N)]

for i in arr:
    ans[i[0]-1][i[1]-1] = i[0]*i[1]

for col in ans:
    for i in col:
        print(i, end=' ')
    print()