input_str = input()
target_str = input()
# Please write your code here.

if target_str in input_str:
    ans = input_str.index(target_str)
else:
    ans = -1

print(ans)