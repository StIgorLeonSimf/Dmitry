# file = open('text.txt', 'r', encoding='utf-8')
# # s = file.read(10)
# # print(s)
# # s = file.readline()
# # print(s)
# ls = file.readlines()
# print(ls)
# file.close()

# for i in open('text.txt', 'r', encoding='utf-8'):
#     print(i.strip())


with open('text.txt', 'r', encoding='utf-8') as file:
    ls = file.read().title().split()
    ls.sort()

print(ls)

with open('text1.txt', 'a', encoding='utf-8') as file:
    for k, sur in enumerate(ls, 1):
        file.write(f'{k}. {sur}\n')

print(ord('Е'))
print(chr(118))
for i in range(1040, 1106):
    print(i, chr(i))