# ? -----------------------------------------------------
# 13. Строки и их методы:
# https://egoroffartem.pythonanywhere.com/course/python/stroki-i-ikh-metodi
# https://www.youtube.com/watch?v=GmMD6gQYWe4
# ? -----------------------------------------------------
# -F- ---divider-------------------------------------------
def divider(ch):
    print(f'\n{ch} ', end = '')
    for i in range(50): print(f'{ch} ', end = '')
    print(f'{ch}\n')
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
def L1():
    list1 = [1, 1, 1]
    return list1
# -F- -----------------------------------------------------
def L2():
    list2 = [2, 2, 2]
    return list2
# -F- -----------------------------------------------------
# |--- -----------------------------------------------------
# print('--- list.append(x)                   добавляет значение x в конец списка; ---')
# |--- -----------------------------------------------------
def ListAppend():
    list1 = L1()
    print(f'\nИсх.:   {list1}')
    list1.append(555)
    print(f'Кон.:   {list1}\n')
# -F- -----------------------------------------------------
# |--- -----------------------------------------------------
# print('--- list.extend(list2)               расширяет список, добавляя в конец все элементы списка list2; ---')
# |--- -----------------------------------------------------

# -F- -----------------------------------------------------
# |--- -----------------------------------------------------
# print('--- list.insert(i, x)                вставляет на i-ое место значение x; ---')
# |--- -----------------------------------------------------

# -F- -----------------------------------------------------
# |--- -----------------------------------------------------
# print('--- list.remove(x)                   удаляет первый элемент в списке, имеющий значение x. ---')
# print('---                                  Если такого элемента не существует, произойдет ошибка ValueError; ---')
# |--- -----------------------------------------------------

# -F- -----------------------------------------------------
# |--- -----------------------------------------------------
# print('--- list.pop(i)                    удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент; ---')
# |--- -----------------------------------------------------

# -F- -----------------------------------------------------
# |--- -----------------------------------------------------
# print('--- list.index(x, [start [, end]])   возвращает положение (индекс) первого элемента со значением x ---')
# print('---                                  (при этом поиск в списке ведется в срезе от start до end); ---')
# |--- -----------------------------------------------------

# -F- -----------------------------------------------------
# |--- -----------------------------------------------------
# print('--- list.count(x)                    возвращает количество элементов со значением x; ---')
# |--- -----------------------------------------------------

# -F- -----------------------------------------------------
# |--- -----------------------------------------------------
# print('--- list.sort([key=функция])         сортирует список на основе функции; ---')
# |--- -----------------------------------------------------

# -F- -----------------------------------------------------
# |--- -----------------------------------------------------
# print('--- list.reverse()                   перестраивает элементы списка в обратном порядке; ---')
# |--- -----------------------------------------------------

# -F- -----------------------------------------------------
# |--- -----------------------------------------------------
# print('--- list.copy()                      возвращает поверхностную копию списка; ---')
# |--- -----------------------------------------------------

# ! -----------------------------------------------------
    # -C- -----------------------------------------------------
    list12 = list1                  # !!! Списки ссылаются на одну и ту же область памяти !!!
    print(f'Кон.:   {list12}      # !!! НЕ ВЕРНОЕ !!! копирование.\n')
# ! -----------------------------------------------------
# -F- -----------------------------------------------------
# |--- -----------------------------------------------------
# print('--- list.clear()                     очищает список. ---')
# |--- -----------------------------------------------------

# -F- -----------------------------------------------------
# print('---  ---')
# print()

# [ ] -------------------------------------------------->->->

print('\n')
bbrr('=')
print('=', '--- egoroff_channel ---'.center(99), '=')
print('=', '--- 13. Строки и их методы: ---'.center(99), '=')
bbrr('=')
print()

# br('-')
# print('--- list.append(x)                   добавляет значение x в конец списка; ---')
# br('-')
# ListAppend()

br('=')


# [ ] -------------------------------------------------<-<-<-
print()
