N = int(input())

# Please write your code here.
def strange_sequence(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    
    return strange_sequence(num//3) + strange_sequence(num-1)

print(strange_sequence(N))