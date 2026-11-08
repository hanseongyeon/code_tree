sentence = list(map(str, input()))
first = sentence[0]
second = sentence[1]

for i in range(len(sentence)):
    if sentence[i] == second:
        sentence[i] = first

print(''.join(sentence))