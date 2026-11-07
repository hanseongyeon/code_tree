sentence = list(map(str, input()))
sentence[1] = 'a'
sentence[-2] = 'a'

print(''.join(sentence))