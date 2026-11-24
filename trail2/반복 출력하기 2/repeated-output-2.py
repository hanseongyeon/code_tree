n = int(input())

# Please write your code here.
def hi(num):
    if num == 0:
        return
        
    hi(num-1)
    print('HelloWorld')

hi(n)