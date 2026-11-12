input_num = int(input())

# Please write your code here.

def square(n):
    # global cnt
    # arr = [[[0] for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += 1
            if cnt == 10:
                cnt = 1
            print(cnt, end=' ')
        print()
    # for col in arr:
    #     print(*col, sep=' ')
square(input_num)