print()
print('--- Условия - if elif else ---')
# -------------------------------------------------------
print()
print('->->-> v.01 ->->->')
print('- Найти максимальное число. -')
print('Введите:')
a = int(input('a = '))
b = int(input("b = "))
if a > b:
    print(f'максимальное число \'a\' = {a}')
else:
    print(f'максимальное число \'b\' = {b}')
print('<-<-<- v.01 <-<-<-')
# -------------------------------------------------------
print()
print('->->-> v.02 ->->->')
print('- Условие проверки имени. -')
username = input('Введите ваше имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)
print('<-<-<- v.02 <-<-<-')
# -------------------------------------------------------
print()
print('->->-> v.03 ->->->')
print('- Проверка на кратность. -')
n = int(input('Введите число: '))
if n % 2 == 0 and n % 3 == 0:
    print('Число кратно 6')
if n % 5 == 0 and n % 3 == 0:
    print('Число кратно 15')
print('<-<-<- v.03 <-<-<-')
# -------------------------------------------------------
print()
print('--- Условия - if elif else ---')
print()
