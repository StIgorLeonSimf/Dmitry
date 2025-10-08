"""list"""

"""    0   1   2   3   4   """
ls = [22, 33, 44, 55, 99]
"""   -5  -4  -3  -2  -1  """


print(ls[2])
print(ls[-3])
new = ls[2:-1]
new = ls[2::-1]
new = ls[:]
print(id(ls))
print(id(new))
print(new)
print(ls[::-1])

ls.append(33)  # O(1) - константная
print(ls)
ls.insert(0, 200)  # O(n) - линейная
print(ls)
print(id(ls))
ls.extend([1, 2])
# ls += [1, 2]
# ls = ls + [1, 2]
print(id(ls))
print(ls)
# l = []
# for i in range(10):
#     l.append(i ** 2)
# print(l)
# l = [i ** 2 for i in range(10)]
# print(l)

n = ls.pop()  # O(1)
n1 = ls.pop(0)  # O(n)
print(ls, n, n1)
# while 33 in ls:
#     ls.remove(33)
print(ls)

print(ls.index(33, 2, 6))
print(ls.count(33))
ls.reverse()
ls.sort(reverse=True)
print(ls)
# ls.remove(10)
# try:
#     ls.remove(9)
# except ValueError as er:
#     print('Нет такого значения в списке', er)
# except TypeError:
#     pass
# except Exception as err:
#     print(err)
# else:
#     print('ok', ls)
# finally:
#     print('allways')
print(list(range(len(ls))))
ls1 = ls.copy()
for i in range(len(ls)):
    print(i, ls[i], end='   ')
print()

cnt = 0
for i in ls:
    print(cnt, i, end='   ')
    cnt += 1
print()
ls1.reverse()
for i in enumerate(ls):
    print(i[0], i[1], end='   ')
print()
for k, i in enumerate(ls):
    print(k, i, end='   ')
print()

# k, i  = 0, 99
# k, i  = 1, 55
# print(k, i)

for i, j, k in zip(ls, ls1, ls):
    print(i, j, k)


""" Mary, Petrova, 20
    John, Bolton, 25
    Ivan, Andreev, 22
"""