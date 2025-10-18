"""set"""
"""неупорядоченный набор уникальных объектов (неизменяемые типы данных)"""

# st = set()
# print(st)
st = {22, 33, 44, 22}
# добавление объектов в множество
st.add(100)
st.update((1, 2))
# удаление объектов из множества

n = st.pop()
# st.remove(33)
st.discard(33)
# print(n)
# print(st)

st1 = {1, 2, 33}
st2 = {1, 2, 44}
# объединение множеств
# res = st1.union(st2)
# res = st1 | st2

# пересечение множеств
# res = st1.intersection(st2)
# res = st1 & st2

# вычитание множеств
# res = st1.difference(st2)
# res = st2 - st1

# симметрическая разность
res = st1.symmetric_difference(st2)
res = st1 ^ st2


print(res)