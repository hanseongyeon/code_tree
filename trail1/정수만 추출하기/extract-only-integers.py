str1, str2 = map(str, input().split())
ans1, ans2 = 0, 0
for i in str1:
    if i.isdigit() == False:
        idx = str1.index(i)
        ans1 = str1[:idx]
        break
    else:
        ans1 = str1


for i in str2:
    if i.isdigit() == False:
        idx = str2.index(i)
        ans2 = str2[:idx]
        break
    else:
        ans2 = str2

print(int(ans1)+int(ans2))