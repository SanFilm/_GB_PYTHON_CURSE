
# ? -----------------------------------------------------
# Дополнительная информация:
# https://devpractice.ru/files/books/python/Matplotlib.book.pdf
# https://indico-hlit.jinr.ru/event/151/attachments/340/492/Project_school_Matplotlib_original.pdf
# ? -----------------------------------------------------

        # -I- ---------------
import numpy as np          # Подключение библиотеки.
# Если ошибка не пропадает.
# Установка 'NumPy'. В терминале ввести (Mac High Sierra):
#    pip3 install numpy
# Удаление:
#    pip uninstall numpy
# Проверка версии:
#    pip list
# Подключение библиотеки визуализации данных
import matplotlib.pyplot as plt
# Установка 'Matplotlib'. В терминале ввести (Mac High Sierra):
#    pip3 install matplotlib

        # -I- ---------------

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
com, t = 60, 70

br_('=')
# -C- ---------------
print('--- _AI-02.00...Библиотеки Matplotlib. ---'.center(com, '-'))
print('--- Библиотека для визуализации данных. ---'.center(com, '-'))
br('-')
# |--- ------------------------------------------------------
# -C- ---------------
print('\n', "---  Генерация точек графика.  ".ljust(t, '-'))
print('\n', "---  np.linspace() - значения по оси 'x' (равномерный массив чисел).  ".ljust(t, '-'), '\n')
# От 0 до (включая) 15, 101 - общее кол-во чисел.
x = np.linspace(0, 15, 101)
print(x)            # (значения по оси x)
# |--- ------------------------------------------------------
# -C- ---------------
print('\n', "---  np.sin(x) - значения по оси 'y'.  ".ljust(t, '-'), '\n')
y = np.sin(x)
print(y)            # (значения по оси y)
# |--- ------------------------------------------------------
# -C- ---------------
print('\n', "---  1. Отрисовка графика + доп. параметры (всплывающее окно).  ".ljust(t, '-'), '\n')
plt.figure(figsize=(10, 5))     # Размер полотна в дюймах 'x'= 10, 'y'= 5.
plt.plot(x, y)                  # Отрисовка графика по точкам массива 'x' и 'y'.
plt.title("y=sin(x)")           # .title() - название графика.
plt.xlabel('Переменная X')      # .xlabel() - подпись оси 'x'
plt.ylabel('Переменная Y')      # .ylabel() - подпись оси 'y'
plt.show()                      # .show() - вывод графика.
# |--- ------------------------------------------------------
# -C- ---------------
print('\n', "---  2. Отрисовка графика + доп. параметры (всплывающее окно).  ".ljust(t, '-'), '\n')
plt.figure(figsize=(10, 5))                   # Размера полотна в дюймах...
plt.plot(x, y, label='sin(x)')                # 'label' - подпись кривой.
plt.plot(x, np.cos(x)/2, label='cos(x)/2')    # Отрисовка еще одного графика.
plt.title("y = sin(x)")                       # Название графика
plt.xlabel('Переменная X')                    # Подпись оси 'x'
plt.ylabel('Переменная Y')                    # Подпись оси 'y'
plt.legend()                                  # Отрисовка подписей кривых ("легенды")
plt.grid()                                    # .grid() - сетка.
plt.show()                                    # Вывод графика
# |--- ------------------------------------------------------
# -C- ---------------
print('\n', "---  3. Отрисовка графика + доп. параметры (всплывающее окно).  ".ljust(t, '-'), '\n')
plt.figure(figsize=(14, 7))                   # Размера полотна в дюймах...

plt.plot(x,y , label='sin(x)', color='#4b0082', linewidth=4, marker='h', markerfacecolor='lightgreen', markeredgewidth=2, markersize=10, markevery=5)
plt.plot(x, np.cos(x)/2, label='cos(x)/2', linewidth=3, color='lightcoral', marker='D', markeredgecolor='black', markevery=5)

# label – подпись кривой графика;
# color – цвет линии;
# linewidth – ширина линии;
# linestyle – стиль линии;
# marker – маркер;
# mec – цвет маркера;
# markersize – размер маркера.

plt.title("y = sin(x)")                       # Название графика
plt.xlabel('Переменная X')                    # Подпись оси 'x'
plt.ylabel('Переменная Y')                    # Подпись оси 'y'
plt.legend()                                  # Отрисовка подписей кривых ("легенды")
plt.grid()                                    # .grid() - сетка.
plt.show()                                    # Вывод графика
