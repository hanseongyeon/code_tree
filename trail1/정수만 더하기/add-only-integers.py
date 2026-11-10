A = list(input())
sum = 0
for i in A:
    if i.isdigit() == True:
        sum += int(i)

print(sum)