sentence = list(input())
for i in sentence:
    if i.isdigit() == True:
        print(i, end='')
    elif i.isalpha() == True:
        print(i.lower(), end='')