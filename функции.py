# def name(n):
#     print(n, 'good!')
#     return f'{n} good'
#
# nm = name('Mary')
# print(nm)
# # name('Sasha')

def smr(x=10, y=5) -> int:
    global z
    # z = 111
    z += 1
    print(x, y, z)
    return x + y


x = 1000
y = 500
z = 1000
# smr()
# print(x, y, z)

# res = smr('10', '20')
# print(res)
# res = smr(10, 20)
# print(res)
# res = smr(15)
# print(res)
# res = smr()
# print(res)
# res = smr(y=100)
# print(res)

# def sumr(*numbs, **kwargs):
#     print(numbs)
#     print(kwargs)
#     return sum(numbs)
#
# print(sumr())
# print(sumr(1, 2, x=5))
# print(sumr(1, 2, 3, 4, x=5, y=25))

# def num2(n):
#     if n > 1:
#         num1(n-1)
#     print(n)
#
# def num1(n):
#     if n > 1:
#         num2(n-1)
#     print(n)

def num(n):
    if n > 1:
        num(n-1)
    print(n)

#
# num(10)

"""
0 1 1 2 3 5 8 13 21 34 55 ......
n = (n-1) + (n-2)
"""

def fib(n):
    if n == 0:
        return  0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# print(fib(10))


def name(nm):
    cnt = 0
    def surname(snm):
        nonlocal cnt
        cnt += 1
        print(cnt, nm, snm)
    return surname

cnt = 100
surn = name('Mary')
sur = name('Sasha')
surn('Ivanova')
surn('Petrova')
surn('Andreeva')
sur('Ivanova')
sur('Petrova')
sur('Andreeva')