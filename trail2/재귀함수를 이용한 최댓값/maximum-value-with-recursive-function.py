n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def recursion_max(index, max_num):
    if index == len(arr):
        return max_num

    return recursion_max(index+1, max(arr[index], max_num))


print(recursion_max(0, arr[0]))