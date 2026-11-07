sentence = input()
new = []

for i in range(len(sentence)):
    if i%2 == 1:
        new.append(sentence[i])

for i in new[::-1]:
    print(i, end='')
        
