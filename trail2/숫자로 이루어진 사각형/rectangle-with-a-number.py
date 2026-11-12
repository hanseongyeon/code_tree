n = int(input())

# Please write your code here.
cnt = 0
def square(n):
    global cnt
    arr = [[[0] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            cnt += 1
            if cnt == 10:
                cnt = 1
            arr[i][j] = cnt

    for col in arr:
        print(*col, sep=' ')
square(n)