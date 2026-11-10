alpha = str(input())

ask = ord(alpha)

if ask == 122:
    ans = 97
else:
    ans = ask+1

print(chr(ans))