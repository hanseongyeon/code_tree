n = int(input())

# Please write your code here.

def up(num):
    i = 1
    if i == num:
        print(i, end=' ')
        return
    
    while i < num:
        i += 1
    
    up(i-1)
    print(i, end=' ')
up(n)
print()
def down(num):
    i = 1
    if i == num:
        print(i)
        return
    
    while i < num:
        i += 1
    
    print(i, end=' ')
    down(i-1)
down(n)