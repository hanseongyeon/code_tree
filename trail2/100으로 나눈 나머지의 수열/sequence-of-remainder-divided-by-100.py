N = int(input())

# Please write your code here.
def devide_hundred(num):
    if num == 1:
        return 2
    
    if num == 2:
        return 4
    
    return (devide_hundred(num-1)*devide_hundred(num-2))%100

print(devide_hundred(N))