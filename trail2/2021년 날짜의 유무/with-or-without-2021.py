M, D = map(int, input().split())

# Please write your code here.
def date_in_2021(month, day):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day <= 31:
            return "Yes"
    elif month in [4, 6, 9, 11]:
        if day <= 30:
            return "Yes"
    elif month == 2:
        if day <= 28:
            return "Yes"

    return "No"

print(date_in_2021(M, D))