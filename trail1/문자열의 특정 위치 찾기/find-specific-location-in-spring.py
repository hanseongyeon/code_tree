sentence, word = map(str, input().split())

for i in sentence:
    if i == word:
        print(sentence.index(i))
        break

if word not in sentence:
    print('No')
    