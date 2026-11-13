A = input()
B = input()

# Please write your code here.
idx = 0
while B in A:
    idx = A.index(B)
    A = A[:idx]+A[idx+len(B):]

print(A)