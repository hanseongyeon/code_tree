A = input()

# Please write your code here.
cnt = 1
new_str = ''

if len(A) == 1:
    new_str += A
    new_str += str(len(A))
    
for i in range(1, len(A)):
    new = A[i-1]
    if A[i-1] == A[i]:
        cnt += 1
        if i == len(A)-1:
            new_str += new
            new_str += str(cnt)
    elif A[i-1] != A[i]:
        new_str += new
        new_str += str(cnt)
        cnt = 1
        if i == len(A)-1:
            new = A[i]
            new_str += new
            new_str += str(cnt)

print(len(new_str))
print(new_str)