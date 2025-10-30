ls = [22, 33, 44, 55]
# for i in ls:
#     print(i)
#
# for i in ls:
#     print(i)
#
#
# def num(start, stop):
#     while start <= stop:
#         yield start
#         start += 11
#
# gen = num(22, 55)
# print(gen)
# for i in gen:
#     print(i)
#
# for i in gen:
#     print(i)

res = (i for i in range(22, 56, 11))
print(type(res))
# for i in res:
#     print(i)
it = iter(ls)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))