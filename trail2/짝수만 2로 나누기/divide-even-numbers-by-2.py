n = int(input())
input_list = list(map(int, input().split()))

# Please write your code here.
def check_element(arr):
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            arr[i] //= 2
    return arr

check_element(input_list)
for elem in input_list:
    print(elem, end=' ')
