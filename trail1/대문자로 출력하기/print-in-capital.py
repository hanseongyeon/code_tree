sentence = list(input())
ans = []

for i in sentence:
    if i.isalpha() == True:
        ans.append(i)

for i in ans:
    print(i.upper(), end='')
