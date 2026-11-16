n = int(input())

# Please write your code here.
def decision(num):
    return num%2 == 0 and (num//10+num%10)%5 == 0

if decision(n):
    print("Yes")
else:
    print("No")