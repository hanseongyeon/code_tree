N = int(input())
arr = []

for i in range(N):
    arr.append(input())

condition = input()

cnt = 0
length = 0
for word in arr:
    if word[0] == condition:
        cnt += 1
        length += len(word)

print(f'{cnt} {length/cnt:.2f}')