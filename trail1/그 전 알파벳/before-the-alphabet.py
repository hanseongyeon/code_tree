alpha = str(input())

if alpha == 'a':
    ans = 'z'
else:
    ans = chr(ord(alpha)-1)
print(ans)