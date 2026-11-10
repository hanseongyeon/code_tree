sentence = input()
ans_list = []
for word in sentence:
    ans_list.append(word)

for i in range(len(ans_list)-1):
    idx = int(input())
    if idx >= len(ans_list):
        ans_list.pop()
    else:
        ans_list.pop(idx)
    print(''.join(ans_list))
    if len(ans_list) == 1:
        break