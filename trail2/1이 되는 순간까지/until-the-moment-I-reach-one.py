N = int(input())

# Please write your code here.
def since_one(num, cnt=0):
    if num == 1:
        return cnt

    if num%2 == 0:
        return since_one(num//2, cnt+1)
        cnt += 1
    else:
        return since_one(num//3, cnt+1)

print(since_one(N))