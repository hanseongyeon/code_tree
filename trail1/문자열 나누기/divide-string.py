N = int(input())
arr = list(map(str, input().split()))
word = ''.join(arr)

for i in range(len(word)):
    print(word[i], end='')
    if i%5 == 4:
        print()


    