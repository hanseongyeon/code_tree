cnt = 0
ans = []
for i in range(int(200)):
    word = str(input())
    if word == '0':
        break
    cnt += 1
    if cnt%2 == 1:
        ans.append(word)

print(cnt)
for i in ans:
    print(i)