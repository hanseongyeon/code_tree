S, Q = map(str, input().split())
S = list(S)

for i in range(int(Q)):
    first, second, third = map(str, input().split())
    ans = []

    if first == '1':
        S[int(second)-1], S[int(third)-1] = S[int(third)-1], S[int(second)-1]
    else:
        for i in range(len(S)):
            if S[i] == second:
                S[i] = third

    print(*S, sep='')
