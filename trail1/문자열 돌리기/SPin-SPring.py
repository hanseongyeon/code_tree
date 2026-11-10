input_str = str(input())
L = len(input_str)

print(input_str)
for i in range(L):
    input_str = input_str[-1]+input_str[:-1]
    print(input_str)