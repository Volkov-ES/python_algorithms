'''6. Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.'''

n = int(input('Номер буквы в алфавите: '))
if  n > 0 and n <= 26 :
    n = ord('a') + n - 1
    print('Это буква', chr(n))
else :
    print(f'Буквы с таким номером в алфавите нет')

