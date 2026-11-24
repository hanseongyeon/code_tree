n = int(input())

# Please write your code here.

def up(num):
    if num == 0:
        return
    
    up(num-1)
    print(num, end=' ')
    
def down(num):
    if num == 0:
        return

    print(num, end=' ')
    down(num-1)

up(n)
print()
down(n)