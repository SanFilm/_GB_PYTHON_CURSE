#   todo-tree.highlights.customHighlight
        # BUG ---------------
        # HACK ---------------
        # FIXME ---------------
        # TODO ---------------
        # XXX ---------------
        # -T- ---------------
        # -I- ---------------
        # -C- ---------------
        # -F- ---------------
        # -f- ---------------
        # [ ] ---------------
        # [*] ---------------
        # [x] ---------------
        # [--] ---------------
        # [-] ---------------
#   better-comments.tags
        # ! ---------------
        # ? ---------------
        # // ---------------
        # todo ---------------
        # * ---------------

# import numpy as np

# -F- ---divider--------------------------------------------
def divider(num):
    r = '- - -'
    print()
    for i in range(5): print(f'{r} {num}. ', end = '')
    print(f'{r}\n')
# -F- ---br-------------------------------------------------
def br(ch):
    print(f'{ch} ', end = '')
    for i in range(20): print(f'{ch} ', end = '')
    print(f'{ch}')
# -F- ---br_------------------------------------------------
def br_(ch):
    print(f'\n{ch} ', end = '')
    for i in range(50): print(f'{ch} ', end = '')
    print(f'{ch}\n')
# -F- ------------------------------------------------------

# -F- ------------------------------------------------------

# [ ] -------------------------------------------------->->->
br_('=')
# -C- ---------------
print('--- _AI-02.00...Библиотеки Numpy. ---'.center(60, '-'))
br('-')
# -C- ---------------
print('\n', "  *args - неограниченное количество аргументов.  ".center(70, '-'))
br('-')

""" my_list = [1, 2, 3, 4, 5]                 # Задание списка чисел с названием my_list
numpy_arr = np.array(my_list)             # Вызов np.array() превращает список в массив чисел
print(numpy_arr)                          # Проверка результата
print(f'my_list   - {type(my_list)}')
print(f'numpy_arr - {type(numpy_arr)}')   # Вызов type() сообщает тип данных значения переменной numpy_arr """

# [ ] -------------------------------------------------<-<-<-
# |--- -----------------------------------------------------