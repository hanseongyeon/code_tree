str1 = list(input())
str2 = list(input())
new1 = ''
new2 = ''

for i in str1:
    if i.isdigit() == True:
        new1 += i

for i in str2:
    if i.isdigit() == True:
        new2 += i

print(int(new1) + int(new2))