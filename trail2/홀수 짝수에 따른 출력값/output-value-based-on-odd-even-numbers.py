N = int(input())

# Please write your code here.
def odd_even_sum(num):
    if num == 1:
        return 1
    if num == 2:
        return 2

    if num%2 == 1:
        return num + odd_even_sum(num-2)
    else:
        return num + odd_even_sum(num-2)

print(odd_even_sum(N))