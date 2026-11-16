a, b = map(int, input().split())

# Please write your code here.
def count_369(i):
        return i%10 == 3 or i%10 == 6 or i%10 == 9 or i//10 == 3 or i//10 == 6 or i//10 == 9

def multiple(i):
        return i%3 == 0

cnt = 0

for num in range(a, b+1):
    if multiple(num):
        cnt += 1
    else:
        num = list(str(num))
        for i in num:
            if count_369(int(i)):
                cnt += 1
                break
print(cnt)
