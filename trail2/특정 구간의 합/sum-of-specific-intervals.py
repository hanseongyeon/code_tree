n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# print(queries)
# Please write your code here.
def special_part_sum():
    
    global arr
    for query in queries:
        sum = 0
        for i in range(query[0]-1, query[1]):
            sum += arr[i]
        print(sum)
    return
special_part_sum()