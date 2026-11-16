a, b = map(int, input().split())

# Please write your code here.
def decision_num(num):
    if num%2 == 0:
        return False
    elif num%10 == 5:
        return False
    elif num%3 == 0 and num%9 != 0:
        return False
    return True

cnt = 0
for i in range(a, b+1):
    if decision_num(i):
        cnt += 1

print(cnt)