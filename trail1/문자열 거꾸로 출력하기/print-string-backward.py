for i in range(10):
    word = str(input())
    if word == 'END':
        break
    for i in word[::-1]:
        print(i,end='')
    print()