word = input()
num = int(input())
new = []
for i in word[::-1]:
    new.append(i)

if len(new) < num:
    for i in new:
        print(i, end='')
else:
    for j in range(num):
        print(new[j], end='')