n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def continuous_part_sequence(first_list, second_list):
    for i in range(0, len(a)-len(b)+1):
        if a[i:i+len(b)] == b:
            return 'Yes'
    return 'No'

print(continuous_part_sequence(a, b))