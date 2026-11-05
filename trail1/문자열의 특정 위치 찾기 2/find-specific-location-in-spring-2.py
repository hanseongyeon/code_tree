str = ['apple', 'banana', 'grape', 'blueberry', 'orange'] 
word = input()
cnt = 0
for i in str:
    if i[2] == word or i[3] == word:
        cnt += 1
        print(i)
print(cnt)

