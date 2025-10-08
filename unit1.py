x = 8  # одно имя - одно значение (переменная)
x = 2, 3, 4  # одно имя - множество значений (коллекция)

x = 5  # int
y = 5.45  # float
name = 'Mary'  # str
yes_no = True  # bool (False)

ls = [1, 2, 3]  # list (cписок)
tp = (2, 3, 4)  # tuple (кортеж)
st = {11, 2, 3}  # set  (множество)
d = {'key': 'values', 'k1': 'V1'}  # dict (словарь)
l = list(st)
print(l)
PI = 3.1415926
# PI = 2.7

print(x, y, name, sep='...', end='________')
print(x, y, name)

# n = int(input('Введите число: '))
# n1 = int(input('Введите число: '))
# n += n1
# print(n, type(n))
"""
+, -, *, **, /, //, %

>, <, <=, <=, !=, ==   -> bool
True and True and .... = True
False or False or .... = False
"""
a = 7
b = 7
c = a > b
print(c)

if a > b:
    print('A > B')
elif a == b:
    print('A = B')
else:
    print('A < B')

print('END')

# h = int(input('Введите время суток: '))
#
# if h >= 4 and h < 12:
#     print('Morning')
# elif h >= 12 and h < 17:
#     print('Day')
# elif 17 <= h < 24:
#     print('Evening')
# elif h >= 0 and h < 4 or h == 24:
#     print('Night')
# else:
#     print('Нет такого времени суток!!!')

# i = 0
# while i < 5:
#     i += 1
#     if i == 4:
#         continue
#     print(i, end=' ')

# i = 0
# while i < 5:
#     i += 1
#     if i == 14:
#         break
#     print(i, end=' ')
# else:
#     print('\nOK')

# n = int(input('> '))
# sm = 0
# k = 0
# while n != 0:
#     sm += n
#     k += 1
#     n = int(input('> '))
# print(sm, k)
""" s = 3 + 2 + 1
123 % 10 = 3
    //10 = 12   % 10 = 2
                //10 = 1    % 10 = 1
                            //10 = 0 

"""
# n = int(input('> '))
# nn = n
# sm = 0
# cnt = 0
# while n > 0:
#     m = n % 10
#     sm += m
#     cnt += 1
#     n //= 10
# print(f'В числе "{nn}" {cnt} ц. суммой {sm}')


# n = int(input('> '))
# res = 0
# while n != 0:
#     m = n % 10
#     res = res * 10 + m
#     n //= 10
#
# print(res)
# for i in 22, (1, 55):
#     print(i, 'yes')
print(list(range(10)))  # start = 0, stop, step = +1
# print(range(1, 10, 2))
# for i in range(0, 10, 2):
#     print(i, end=' ')
# for i in range(20, 10, -1):
#     print(i, end=' ')

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i * j:2}', end=' ')
#     print()

ss = 271.456988708984

print('Площадь = "', round(ss, 2), '"', sep='')
sf = f'Площадь = "{ss:.2f}"'
print(sf)