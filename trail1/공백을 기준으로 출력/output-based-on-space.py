str1 = input()
str2 = input()
ans = []

for i in str1:
    if i != ' ':
        ans.append(i)
for i in str2:
    if i != ' ':
        ans.append(i)

for i in ans:
    print(i, end='')