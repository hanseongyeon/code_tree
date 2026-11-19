A = input()

# Please write your code here.
def alphabet_cnt(alphabets):
    new = []
    for alphabet in alphabets:
        new.append(alphabet)

    return len(set(new))

if alphabet_cnt(A) >= 2:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)