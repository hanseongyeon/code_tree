N = int(input())
arr = []
cnt = 0
a_cnt = 0
for i in range(N):
    arr.append(input())

for word in arr:
    cnt += len(word)
    if word[0] == 'a':
        a_cnt += 1

print(cnt, a_cnt)