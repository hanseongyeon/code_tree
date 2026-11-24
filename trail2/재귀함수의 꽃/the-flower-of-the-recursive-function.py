N = int(input())

# Please write your code here.
def down_up(num):
    if num == 0:
        return
    
    print(num, end=' ')
    down_up(num-1)
    print(num, end=' ')

down_up(N)