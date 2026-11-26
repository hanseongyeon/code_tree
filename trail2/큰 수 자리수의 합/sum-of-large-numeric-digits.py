a, b, c = map(int, input().split())

# Please write your code here.
multi_num = a*b*c

def each_sum(num):
    if num < 10:
        return num
    return each_sum(num//10) + num%10

print(each_sum(multi_num))