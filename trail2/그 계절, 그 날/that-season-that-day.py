Y, M, D = map(int, input().split())

# Please write your code here.
def leap_year(year):
    if year%4 == 0 and year%100 != 0:
        return True
    elif year%4 == 0 and year%100 == 0 and year%400 == 0:
        return True
    return False

def exist_date(year, month, day):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day <= 31:
            return True
        return False
    elif month in [4, 6, 9, 11]:
        if day <= 30:
            return True
        return False
    else:
        if leap_year(year):
            if day <= 29:
                return True
            return False
        else:
            if day <= 28:
                return True
            return False
    
        
if exist_date(Y, M, D):
    if M in [3, 4, 5]:
        print("Spring")
    elif M in [6, 7, 8]:
        print('Summer')
    elif M in [9, 10, 11]:
        print('Fall')
    elif M in [12, 1, 2]:
        print('Winter')
    else:
        print(-1)
else:
    print(-1)
