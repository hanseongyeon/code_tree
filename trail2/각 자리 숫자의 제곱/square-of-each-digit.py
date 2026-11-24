N = int(input())

# Please write your code here.
def each_num_square(num):
    if num < 10:
        return num**2
    return each_num_square(num//10)+((num%10)**2)

print(each_num_square(N))