sentence = input()

cntee, cnteb = 0, 0
for i in range(len(sentence)-1):
    if sentence[i] == 'e' and sentence[i+1] == 'e':
        cntee += 1
    if sentence[i] == 'e' and sentence[i+1] == 'b':
        cnteb += 1

print(cntee, cnteb)