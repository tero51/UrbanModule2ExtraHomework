import random

n = random.randint(3, 20)

def find_code():
    for i in range(1, int(n/2) + 1):
        for j in range(1, n):
            if i == j:
                continue
            if i + j == n:
                result = print(i,j)
    return result
print(n)
find_code()