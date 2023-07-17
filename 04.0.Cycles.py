print()
print('= = = = = = = = = = = = = = = = = = ')
print()
# [ ] -----------------------------------------------------
print('--- Циклы ---')
# [ ] -----------------------------------------------------
print()
# -C- -----------------------------------------------------
print('->->-> while ->->->')
# |--- ----------------------------------------------------
print('- - - - - - - - - - - - - - - - - - ')
print('- Найти сумму цифр введённого числа \'N\' - ')
# |--- ----------------------------------------------------
n = 423
summa = 0
while n > 0:
    x = n % 10
    summa += x
    n //= 10
print('Сумма чисел = ', summa)  # 9
print('- - - - - - - - - - - - - - - - - - ')
# -------------------------------------------------------
""" print()
print('- - - - - - - - - - - - - - - - - - ')
i=0
while i < 5:
    # if i == 3:
    #     break
    i=i+1
else:
    print('Пожалуй')
    print('Фатит :)')
print(i)
print('- - - - - - - - - - - - - - - - - - ') """
# -------------------------------------------------------
print()
print('- - - - - - - - - - - - - - - - - - ')
print('- Поиск минимального делителя. -')
# |--- ----------------------------------------------------
print()
# n = int(input('Введите число: '))
n = 71
flag = True
i=2
while flag:
    if n % i == 0:      # если остаток при делении числа n на i равен 0 flag = False
        print(f'Минимальный делитель числа {n} = {i}')
        flag = False
    elif i > n // 2:    # делитель числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1
print('- - - - - - - - - - - - - - - - - - ')
print('<-<-<- while <-<-<-')
print()
print('= = = = = = = = = = = = = = = = = = ')
print()
# -C- -----------------------------------------------------
print('->->-> for ->->->')
# |--- ----------------------------------------------------
print('- - - - - - - - - - - - - - - - - - ')
for i in 1, -2, 3, 14, 5:
    print(i)        # 1 -2 3 15 5 - вывод в столбик.
print('- - - - - - - - - - - - - - - - - - ')
for i in 1, -2, 3, 14, 5:       # вывод в строку.
    print(i, end = ' ')         # end = ' ' - разделитель.
print()
print('- - - - - - - - - - - - - - - - - - ')
print('- Создание матрицы. -')
# |--- ----------------------------------------------------
print()
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += " * "
    print(line)
print('- - - - - - - - - - - - - - - - - - ')
print()
print('- Создание матрицы. -')
# |--- ----------------------------------------------------
print('- - - - - - - - - - - - - - - - - - ')
print()
print('<-<-<- for <-<-<-')
print()
print('--- Циклы ---')
print()
# |--- ----------------------------------------------------
print('- \'For\' - Изменение элементов списка без перезаписи: -'.center(70,'-'),'\n')
spisok = [10, 40, 20, 30]
print(f'Исх. список:   {spisok}')
print('В работе:     ', end = '')
for element in spisok:                      # 'element' = Элементу.
    print(element + 2, end = " ")
print(f'\nКон. список:   {spisok}\n')
# |--- ----------------------------------------------------
print('- \'For\' - Изменение элементов списка с перезаписью (вар.1): -'.center(70,'-'),'\n')
i = 0
print('В работе:     ', end = '')           # исключительно для контроля.
for element in spisok:                      # 'element' = Элементу.
    spisok[i] = element + 2
    print(spisok[i], end = " ")             # исключительно для контроля.
    i += 1
print(f'\nКон. список:   {spisok}\n')
# |--- ----------------------------------------------------
print('- \'For\' - Изменение элементов списка с перезаписью (вар.2): -'.center(70,'-'),'\n')
print('В работе:     ', end = '')           # исключительно для контроля.
for i in range(len(spisok)):                # 'i' = Индексу.
    spisok[i] = spisok[i] + 2 
    print(spisok[i], end = " ")             # исключительно для контроля.
print(f'\nКон. список:   {spisok}\n')
# |--- ----------------------------------------------------
print('- \'While\' - Изменение элементов списка с перезаписью: -'.center(70,'-'),'\n')
i = 0
print('В работе:     ', end = '')           # исключительно для контроля.
while i < len(spisok):                      # 'i' = Индексу.
    spisok[i] = spisok[i] + 2 
    print(spisok[i], end = " ")             # исключительно для контроля.
    i = i + 1 # или i += 1
print(f'\nКон. список:   {spisok}\n')
# |--- ----------------------------------------------------
print('- \'For\' - Вызов элементов списка: -'.center(70,'-'),'\n')
i = 1
#  'color' = Элементу.
for color in 'красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'фиолетовый':
# for color in {'красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'фиолетовый'}:     # так тоже работает...
# for color in ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'фиолетовый']:     # и так работает...
# for color in ('красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'фиолетовый'):     # и даже так...
    print('Цвет радуги №', i, ' - ', color, sep = '')
    i += 1
print()