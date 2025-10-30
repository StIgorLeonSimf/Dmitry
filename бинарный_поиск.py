lst = [1, 2, 3, 4, 5, 6, 7, 8]

target = 2
left = 0
right = len(lst) - 1
mid = len(lst) // 2
while lst[mid] != target and left <= right:
    if target > lst[mid]:
        left = mid + 1
    else:
        right = mid - 1
    mid = (left + right) // 2
if left > right:
    print('Нет такого значения')
else:
    print(f'Индекс {target} == {mid}')