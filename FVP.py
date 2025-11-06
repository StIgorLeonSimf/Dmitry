from functools import reduce

ls = [22, 33, 44, 55]
ls1 = [2, 333, 4, 555, 9]
# ls = ['22', '33', 44, 55]
print(ls)
res = []
for i in ls:
    res.append(int(i))
print(res)
res1 = [int(i) for i in ls]
print(res1)
# res = map(int, ls)
# for i in res:
#     print(i, end=' ')
# print(res)
# for i in res:
#     print(i, end=' ')
# print(res)

def power(n):
    return n * n


# res = list(map(int, ls))
# res = list(map(power, ls))
# res = list(map(lambda n: n * n, ls))
# res = list(map(lambda n, m: n - m, ls, ls1))
res = list(map(lambda n, m: n > m, ls, ls1))


# res = list(filter(lambda n: n > 22, ls))
# res = list(filter(lambda n: n % 2 == 0, ls))
# res = list(filter(lambda n: n % 2 != 0, ls))
# res = list(filter(lambda n: n % 3 == 0, ls1))
# print(res)

def prompt(x, y):
    print(f'X = {x}')
    print(f'Y = {y}')
    print(f'Result = {str(y) + str(x)}')
    return str(y) + str(x)

city = ['У', 'ф', 'а', '-', 4, 5]

# res = reduce(lambda x, y: str(x) + str(y), city)
res = reduce(prompt, city)
print(res)