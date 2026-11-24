N = int(input())

# Please write your code here.
def specific_sum(num):
    if num == 1:
        return 1
    
    return specific_sum(num-1) + num

print(specific_sum(N))