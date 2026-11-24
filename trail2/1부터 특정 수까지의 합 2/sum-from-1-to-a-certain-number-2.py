N = int(input())
sum = 0
# Please write your code here.
def specific_sum(num):
    global sum
    if num == 1:
        return 1
    
    sum += specific_sum(num-1) + num
    return sum

print(specific_sum(N))