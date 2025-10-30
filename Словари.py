"""dict"""

# d = {}
""" неупорядоченный набор пар (ключ: значение), где ключ уникален """
d = {'pb': 'ссвинец',
     'au': 'Золото',
     'fe': 'жжелезо'
     }

print(d['fe'])
try:
    print(d['fe1'])
except KeyError as err:
    print(err)
except Exception as err:
    print(err)

res = d.get('fe1', ['my object'])
print(res)
d["fe"] = 'Железо'
d["pb"] = 'Свинец'

d['zn'] = 'Цинк'
res = d.setdefault(2, 222)
print(res)
d.update({3: 33, 2: 22})

print(d)

n = d.pop(2)
n1 = d.popitem()
print(n, n1)
print(d)

print(d.keys())
print(list(d.keys()))
print(list(d))
print(list(d.values()))
for i, j in zip(list(d), list(d.values())):
    print(i, j)
print(list(d.items()))

for k, v in d.items():
    print(k, v)

for k in d:
    print(k, end=' ')
print()
for v in d.values():
    print(v, end=' ')
print()

ls = [22, 33, 44, 22]
dd = dict.fromkeys(ls, 'my object')
# dd = dict.fromkeys(ls, ['my object'])
dd = {i: [] for i in ls}
dd[22].append(100)

dd = {k: k ** 2 for k in range(10, 20)}
print(dd)
dd = {}
for k in range(10, 20):
    dd[k] = k ** 2
print(dd)

ls = [(1, 11), (2, 22), ('yes', 'it is')]
d = dict(ls)
print(d)