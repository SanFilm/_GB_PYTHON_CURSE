print()
print('--- Диапазон ---')
# -------------------------------------------------------
print()
print('- - - Объявление диапазона и работа с ним - - - ')
print()
print('- - - 1. - - - 1. - - - 1. - - - 1. - - - 1. - - - ')
r = range(5)                        # [0 - 4)
for i in r: print(i)                # 0 1 2 3 4 - вывод в столбик.
print()
for i in r: print(i, end = ' ')     # 0 1 2 3 4 - вывод в строку.
print()
print('- - - 2. - - - 2. - - - 2. - - - 2. - - - 2. - - - ')
r = range(2, 5)                     # [2 - 4)
for i in r: print(i, end = ' ')     # 2 3 4
print()
print('- - - 3. - - - 3. - - - 3. - - - 3. - - - 3. - - - ')
r = range(-5, 0)                    # [-5 – -1)
for i in r: print(i, end = ' ')     # -5 -4 -3 -2 -1
print()
print('- - - 4. - - - 4. - - - 4. - - - 4. - - - 4. - - - ')
r = range(1, 10, 2)                 # [1 - 9) шаг = 2
for i in r: print(i, end = ' ')     # 1 3 5 7 9
print()
print('- - - 5. - - - 5. - - - 5. - - - 5. - - - 5. - - - ')
r = range(100, 0, -20)              # [100 - 1) шаг = -20
for i in r: print(i, end = ' ')     # 100 80 60 40 20
print()
# print('- - - - - - - - - - - - - - - - - - ')
print('- - - 6. - - - 6. - - - 6. - - - 6. - - - 6. - - - ')
for i in 'qwe ty 123': print(i, end = ' ')
print()
# print('- - - - - - - - - - - - - - - - - - ')
print('- - - 7. - - - 7. - - - 7. - - - 7. - - - 7. - - - ')
a='qwerty'
print(a[0], a[3], a[4])
print('- - - 8. - - - 8. - - - 8. - - - 8. - - - 8. - - - ')
for i in a: print(i, end = ' ')
print()
# print('- - - - - - - - - - - - - - - - - - ')
# -------------------------------------------------------
print('- - - 9. - - - 9. - - - 9. - - - 9. - - - 9. - - - ')
print()
text = 'СъЕШЬ ещё этих МяГкИх французских булочек'
print('- Работа с регионами текста: -')
print(f'\"{text}\"')
print()
print('- - - - - - - - - - - - - - - - - - ')
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
print('- - - - - - - - - - - - - - - - - - ')
txt = text[2:9] + text[-5] + text[:2]           # ЕШЬ ещелСъ
print(txt)
print('- - - - - - - - - - - - - - - - - - ')
print()
print('--- Диапазон ---')
print()
