print()
print('= = = = = = = = = = = = = = = = = = ')
print()
# -C- -----------------------------------------------------
print('->->-> for ->->->')
# |--- ----------------------------------------------------
print('- - - Итеративный вывод в консоль. вар.1 - - - ')
# -F- -------------------------------------------------->->->
# -f- ----------------------------------------------------
def Out_1_Column():
    print('- - - Вывод через \'i\' в столбик: - - -')           # 1 2 3 4 5
    for i in Lst:
        print(i)                                                # вывод в столбик.
print('- - - - - - - - - - - - - - - - - - ')
# -f- ----------------------------------------------------
def Out_1_Row():
    print('- - - Вывод через \'i\' в строку: - - -')            # 1 2 3 4 5
    for i in Lst:                                               # вывод в строку.
        print(i, end = ' ')                                     # end = ' ' - разделитель.
# -f- ----------------------------------------------------
def Out_2_Row():
    print('- - - Вывод через \'range\' в строку: - - -')        # 1 2 3 4 5
    for i in range(len(Lst)):                                   # вывод в строку.
        print(Lst[i], end = ' ')                                # end = ' ' - разделитель.
# -F- -------------------------------------------------<-<-<-
Lst = [1, 2, 3, 4, 5]
Out_1_Column()
print('- - - - - - - - - - - - - - - - - - ')
Out_1_Row()
print()
print('- - - - - - - - - - - - - - - - - - ')
Tpl = (11, 22, 33, 44, 55)
Out_1_Row()
print()
print('- - - - - - - - - - - - - - - - - - ')
Out_2_Row()
print()
print()
print('- - - - - - - - - - - - - - - - - - ')
print('- Создание матрицы. -')
# |--- ----------------------------------------------------
print()
""" line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += " * "
    print(line) """
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
