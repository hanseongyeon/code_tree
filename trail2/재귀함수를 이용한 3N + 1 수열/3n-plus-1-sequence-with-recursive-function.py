n = int(input())

# Please write your code here.
def threen_plus_one(num):
    if num == 1:
        return 0

    if num%2 == 0:
        return threen_plus_one(num//2) +1
    else:
        return threen_plus_one((3*num)+1) +1

print(threen_plus_one(n))