# -F- ---divider-------------------------------------------
def divider(num):
  r = '- - -'
  print()
  for i in range(5): print(f'{r} {num}. ', end = '')
  print(f'{r}\n')
# -F- -----------------------------------------------------
print()
print('--- Работа с консолью: ---'.center(50))
# |--- -----------------------------------------------------
divider(1)
print('- Работа с цифрами: -\n'.center(50))
n = 5                                                                       # число
m = 1.2                                                                     # число
print(n + m)                                                                # сложение
print(n, '-', m, '=', n - m)                                                # вывод в консоль вар.1
print(f"{n} - {m} = {n - m}")                                               # вывод в консоль вар.2
print("{} - {} = {}".format(n, m, n - m))                                   # вывод в консоль вар.3
# |--- -----------------------------------------------------
divider(2)
print('- Работа с текстом: -\n'.center(50))
text = 'СъЕШЬ ещё этих МяГкИх французских булочек'
print(f'Исх.:   \"{text}\"\n')
    # -C- -----------------------------------------------------
# количество символов в строке.
print(len(text), ' - количество символов в строке.')      # 42
    # -C- -----------------------------------------------------
# наличие символов в строке.
print('ещё' in text)                                      # True
print('Ещё' in text)                                      # False
    # -C- -----------------------------------------------------
# делает все буквы строки маленькими.
print(text.lower())                                       # съешь ещё этих мягких французских булочек
    # -C- -----------------------------------------------------
# делает все буквы строки БОЛЬШИМИ.
print(text.upper())                                       # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОЧЕК
    # -C- -----------------------------------------------------
# Заменяет слово на другое.
print(text.replace('ещё', 'ЧЕЛОВЕЧЕ'))                    # СъЕШЬ ЧЕЛОВЕЧЕ этих МяГкИх французских булочек
# |--- -----------------------------------------------------
divider(3)
print('- Форматированный вывод в консоль: -\n'.center(50))
# https://all-python.ru/osnovy/vyvod-v-konsol.html
print("Программа номер: %4d, получила результат: %8.3f" % (4, n / m))       # Форматированный вывод в консоль.
print('Форматирование: {:04d} {:04d} {:04d}'.format(n - 1, n, n + 1))       # Форматированный вывод в консоль.
# https://pythonru.com/osnovy/formatirovanie-v-python-s-pomoshhju-format
print('Привет {0}, твой баланс:{1:9.2f}'.format("Саня", 230.056))
print('Привет {name}, твой баланс:{blc:9.2f}'.format(name="Саня", blc=230.2346))
divider(4)
print('- Расположение в консоль: -\n'.center(50))
text = " Этот текст расположен в центре - вар 1."
print(text.center(50))
print("Этот текст расположен слева. ".ljust(50, "-"))
print(" Этот текст расположен в центре - вар 2a.".center(50, "-"))
print("|- - -"," Этот текст расположен в центре - вар 2b.".center(50),"- - -|")
print(" Этот текст расположен справа.".rjust(50, "-"))
print(" Этот текст расположен в центре - вар 3.\n".center(50))


