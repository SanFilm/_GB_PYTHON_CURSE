# -F- ---divider-------------------------------------------
def divider(num):
    r = '- - -'
    print()
    for i in range(5): print(f'{r} {num}. ', end = '')
    print(f'{r}\n')
# -F- -----------------------------------------------------
def br(ch):
    print(f'\n{ch} ', end = '')
    for i in range(50): print(f'{ch} ', end = '')
    print(f'{ch}\n')
# -F- -----------------------------------------------------
def bbrr(ch):
    print(f'{ch} ', end = '')
    for i in range(50): print(f'{ch} ', end = '')
    print(f'{ch}')
# -F- -----------------------------------------------------


# [ ] -------------------------------------------------->->->
print('\n')
bbrr('=')
print('=', '--- Диапазон (range): ---'.center(99), '=')
bbrr('=')
print()
# |--- -----------------------------------------------------
print('- - - Объявление диапазона и работа с ним - - -'.center(50))
divider(1)
print('- Вывод в столбик   \'range(5)\': -'.center(50))
r = range(5)                        # [0 - 4)
for i in r: print(i)                # 0 1 2 3 4 - вывод в столбик.
print()
print('- Вывод в строку   \'range(5)\': -'.center(50))
for i in r: print(i, end = ' ')     # 0 1 2 3 4 - вывод в строку.
print()
# |--- -----------------------------------------------------
divider(2)
print('- \'range(2, 5)\' -'.center(50))
r = range(2, 5)                     # [2 - 4)
for i in r: print(i, end = ' ')     # 2 3 4
print()
# |--- -----------------------------------------------------
divider(3)
print('- \'range(-5, 0)\' -'.center(50))
r = range(-5, 0)                    # [-5 – -1)
for i in r: print(i, end = ' ')     # -5 -4 -3 -2 -1
print()
# |--- -----------------------------------------------------
divider(4)
print('- \'range(1, 10, 2)\' -'.center(50))
r = range(1, 10, 2)                 # [1 - 9) шаг = 2
for i in r: print(i, end = ' ')     # 1 3 5 7 9
print()
# |--- -----------------------------------------------------
divider(5)
print('- \'range(100, 0, -20)\' -'.center(50))
r = range(100, 0, -20)              # [100 - 1) шаг = -20
for i in r: print(i, end = ' ')     # 100 80 60 40 20
print()
# |--- -----------------------------------------------------
divider(6)
print('--- Работа с текстом: ---\n'.center(50))
print('- \'qwe ty 123\' -'.center(50))
a = 'qwe ty 123'
for i in a: print(i, end = ' ')
print('          # через переменную.')
for i in 'qwe ty 123': print(i, end = ' ')
print('          # как строка.')
print()
# |--- -----------------------------------------------------
divider(7)
print('- Индексы   \'qwerty\': -'.center(50))
a = 'qwerty'
print(a[0], a[3], a[4])
# |--- -----------------------------------------------------
divider(8)
text = 'СъЕШЬ ещё этих МяГкИх французских булочек'
print('--- Работа с регионами текста (срезы): ---\n'.center(50))
print(f'Исх.:   \"{text}\"\n')
print(text[0])                      # С
print(text[1])                      # ъ
print(text[len(text)-1])            # к
print(text[-1])                     # к
print(text[-5])                     # л
print(text[:])                      # СъЕШЬ ещё этих МяГкИх французских булочек
print(text[:2])                     # Съ
print(text[len(text)-2:])           # ек
print(text[2:9])                    # ЕШЬ еще
print(text[6:-18])                  # ещё этих МяГкИх ф
print(text[0:len(text):6])          # СетГрсу
print(text[::6])                    # СетГрсу
print('--- Конкатенация: ---'.center(50))
txt = text[2:9] + text[-5] + text[:2]           # ЕШЬ ещелСъ
print(txt)
print()
bbrr('=')
# |--- -----------------------------------------------------
divider(9)
print('--- Создание списка на основе последовательности: ---\n'.center(50))
print('- \'list(range(15))\' -'.center(50))
list_of_ints = list(range(15))
print(list_of_ints)
print()
# |--- -----------------------------------------------------
print('--- Создание \'range()\' типа float: ---\n'.center(50))
print('- \'list(range(15))\' -'.center(50))
# -F- -----------------------------------------------------
# все аргументы обязательны
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step
# -F- -----------------------------------------------------
for i in frange(0.5, 1.0, 0.1): print(i, end = ' | ')
print()
for i in frange(0.5, 1.0, 0.1): print(round(i, 1), end=" | ")
print('\n')
for i in frange(1.5, 3.0, 0.1): print(i, end = ' | ')
print()
for i in frange(1.5, 3.0, 0.1): print(round(i, 1), end=" | ")
print('\n')
# [ ] -------------------------------------------------<-<-<-
