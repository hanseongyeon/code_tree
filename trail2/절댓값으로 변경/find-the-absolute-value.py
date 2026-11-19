n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def change_abs(num_list):
    for i in range(len(num_list)):
        num_list[i] = abs(num_list[i])

    return num_list

change_abs(arr)
print(*arr)