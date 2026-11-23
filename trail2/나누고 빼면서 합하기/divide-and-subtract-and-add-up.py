n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
new_list = []
def minus_devide(num):
    global new_list
    new_list.append(1)
    while num != 1:
        new_list.append(num)
        if num%2 == 1:
            num -= 1
        else:
            num //= 2

    return set(new_list)

ans = minus_devide(m)
sum = 0
for i in ans:
    sum += A[i-1]

print(sum)

        

        