print()
print('--- Работа с консолью: ---')
# -------------------------------------------------------
print()
print('- - - - - - - - - - - - - - - - - - ')
n = 5
m = 1.2
print(n + m)
print(n, '-', m, '=', n - m)  # вывод в консоль вар.1
print(f"{n} - {m} = {n - m}")  # вывод в консоль вар.2
print("{} - {} = {}".format(n, m, n - m))  # вывод в консоль вар.3
# -------------------------------------------------------
print('- - - - - - - - - - - - - - - - - - ')
print()
text = 'СъЕШЬ ещё этих МяГкИх французских булочек'
print('- Работа с текстом: -')
print(f'\"{text}\"')
print()
print('- - - - - - - - - - - - - - - - - - ')
# количество символов в строке.
print(len(text))                            # 42
# наличие символов в строке.
print('ещё' in text)                        # True
# делает все буквы строки маленькими.
print(text.lower())                         # съешь ещё этих мягких французских булочек
# делает все буквы строки большими.
print(text.upper())                         # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОЧЕК
# Заменяет слово на другое.
print(text.replace('ещё','ЧЕЛОВЕЧЕ'))       # СъЕШЬ ЧЕЛОВЕЧЕ этих МяГкИх французских булочек
print('- - - - - - - - - - - - - - - - - - ')
print()
print('--- Работа с консолью: ---')
print()