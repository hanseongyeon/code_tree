A = str(input())
direction = list(input())
cnt_L = direction.count('L')
cnt_R = direction.count('R')

for i in direction:
    if i == 'L':
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[:-1]

print(A)