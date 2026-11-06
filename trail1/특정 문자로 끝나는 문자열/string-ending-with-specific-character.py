arr = []
ans = 0
for i in range(11):
    arr.append(input())

for word in arr[:10]:
    if word[-1] == arr[10]:
        ans = word
        print(ans)

if ans == 0:
    print('None')
        
