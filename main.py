import random

n = random.randint(3, 20)

# простенький вариант
# def find_code():
#     for i in range(1, int(n/2) + 1):
#         for j in range(1, n):
#             if i == j:
#                 continue
#             if i + j == n:
#                 print(i, "+",j)
# print(n)
# find_code()

result = []

def find_code():
    for i in range(1, int(n/2) + 1):
        for j in range(1, n):
            if i == j:
                continue
            if i + j == n:
                result.append(i)
                result.append("+")
                result.append(j)
print(n)
find_code()
print(*result)