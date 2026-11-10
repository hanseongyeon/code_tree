sentence = str(input())
list_sentence = list(sentence) 
for word in list_sentence:
    if word == 'e':
        idx = list_sentence.index(word)
        list_sentence.pop(idx)
        print(''.join(list_sentence))
        break