input_n, input_m = map(int, input().split())

# Please write your code here.
def greatest_common_divisor(n,m):
    ans = []
    for i in range(1, 101):
        if n%i == 0 and m%i == 0:
            ans.append(i)
    answer = max(ans)
    print(answer)
greatest_common_divisor(input_n, input_m)