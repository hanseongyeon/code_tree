input_n, input_m = map(int, input().split())

# Please write your code here.
def greatest_common_divisor(n,m):
    ans = 0
    for i in range(1, min(n, m)+1):
        if n%i == 0 and m%i == 0:
            ans = i
    print(ans)
greatest_common_divisor(input_n, input_m)