A = input()

# Please write your code here.
def palindrome(str):
    new = str[::-1]
    return new

if A == palindrome(A):
    print('Yes')
else:
    print('No')