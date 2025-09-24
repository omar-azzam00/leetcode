from functools import cache, lru_cache

# 0! = 1
# 5! = 5 * 4 * 3 * 2 * 1
# 7! = 7 * 6 * .... 1

# Cache Maxsize = 10
# Cache full
# I want to add a new Item
# 4, 5, 7, 8, 9, (10), (0), (2), (6), (11)

@lru_cache(maxsize=10)
def factorial(n):
    print("RUNNING FACTORIAL")
    if n < 0:
        raise Exception("n can't be less than zero")
    elif n == 0:
        return 1

    
    answer = 1
    for i in range(2, n + 1):
        answer *= i
    
    return answer

COUNT = 10
for i in range(COUNT):
    print(f"{i = }")
    print(f"{factorial(i) = }")
    print()

