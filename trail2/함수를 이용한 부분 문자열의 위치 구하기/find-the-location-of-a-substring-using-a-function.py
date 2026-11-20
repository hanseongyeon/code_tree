text = input()
pattern = input()

# Please write your code here.
def find_index(input_str, target_str):
    if target_str in input_str:
        return input_str.index(target_str)
    else:
        return -1

print(find_index(text, pattern))
