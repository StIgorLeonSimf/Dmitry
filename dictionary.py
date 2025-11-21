import json

# d = {'forest': ['лес', 'заповедник']}

with open('dict.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

while True:
    word = input('ВВедите слово: ')
    if word.lower() == 'exit':
        break
    elif word in d:
        print(f'{word}: {", ".join(d[word])}')
    elif word.lower() == 'add':
        word = input('ВВедите слово к которому добавить перевод: ')
        print(f'{word}: {", ".join(d[word])}')
        transl = input(f'Добавь слово в словарь "{word}": ')
        # d.setdefault(word, []).append(transl)
        d[word].append(transl)
        with open('dict.json', 'w', encoding='utf-8') as fl:
            json.dump(d, fl)
    else:
        transl = input(f'Введите перевод слова "{word}": ')
        d[word] = [transl]
        with open('dict.json', 'w', encoding='utf-8') as fl:
            json.dump(d, fl)