sentence = list(map(str, input()))
sentence.pop(1)
sentence.pop(-2)

print(''.join(sentence))