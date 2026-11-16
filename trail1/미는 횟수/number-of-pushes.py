A = str(input())
B = str(input())
cnt = 0
for i in range(len(A)):
    A = A[-1]+ A[:-1]
    cnt += 1

    if A == B:
        print(cnt)
        break
    elif cnt == len(A):
        print(-1)
