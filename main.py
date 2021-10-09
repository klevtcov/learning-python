# python on Stepik.org

# print (15 * 20);
#
# a = 3
# name = input('Whats your name?')
# print ('hello, ' , name)

# a = int(input('Enter number'))
# b = int(input('Enter number'))
# print (a * b)


# Boolean
# a = int(input())
# print(a > 0)

# a = int(input())
# print(10 <= a < 100)

# x1, x2, x3 = False, True, False
# print(not x1 or x2 and x3) -> True
# # not -> and -> or
# True or x2 and x3
# True or False
# True 

# ((a and b) or ((not a) and (not b)))

# x = 5
# y = 10
# y > x * x or y >= 2 * x and x < y

# a = True
# b = False
# a and b or not a and not b
# False

# x = int(input())
# if x % 2 == 0:
#     print('Четное')
# else: 
#     print('Нечетное')

# a = int(input())
# b = int(input())
# if b != 0:
#     print (a / b)
# else:
#     print('Деление не возможно')
#     b = int(input('Введите ненулевое значение'))
#     if b == 0:
#         print('Вы не справились')
#     else:
#         print (a / b)

# A = int(input())
# B = int(input())
# H = int(input())
# if H < A:
#     print('Недосып')
# elif H > B:
#     print('Пересып')
# else:
#     print('Это нормально')

# lower, upper, x = (int(input()) for _ in range(3))
# print("Недосып" if x < lower else "Пересып" if x > upper else "Это нормально")

# year = int(input())
# if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
#     print('Високосный')
# else:
#     print('Обычный')

# comment
# x = 5 #comment

# strings

# a = 'string'
# b = 'another string'
# print(a, b)
# print(a + b)

# print(a)
# '''
# multiline
# comment
# '''
# print(b)
# print(a + '\n' + b) # print in two different lines

# # площадь треугольника по формуле Герона
# a, b, c = int(input()), int(input()), int(input())
# p = (a + b + c) / 2
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5 
# print(S)

# a = int(input())
# print((-15 < a <= 12) or (14 < a < 17) or (a >= 19))

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# a, b, oper = float(input()), float(input()), input()

# if oper == '+':
#     print(a + b)
# elif oper == '-':
#     print(a - b)
# elif oper == '/':
#     if b == 0:
#         print('Деление на 0!')
#     else:
#         print(a / b)
# elif oper == '*':
#     print(a * b)
# elif oper == 'mod':
#     if b == 0:
#         print('Деление на 0!')
#     else:
#         print(a % b)
# elif oper == 'pow':
#     print(a ** b)
# elif oper == 'div':
#     if b == 0:
#         print('Деление на 0!')
#     else:
#         print(a // b)

# a, b, oper = float(input()), float(input()), input()

# if oper == '+':
#     print(a + b)
# elif oper == '-':
#     print(a - b)
# elif oper == '*':
#     print(a * b)
# elif oper == 'pow':
#     print(a ** b)
# elif b == 0:
#     print('Деление на 0!')
# elif oper == '/':
#     print(a / b)
# elif oper == 'div':
#     print(a // b)
# elif oper == 'mod':
#     print(a % b)

# t = input()
# if t == 'треугольник':
#     a, b, c = int(input()), int(input()), int(input())
#     p = (a + b + c) / 2
#     print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
# elif t == 'прямоугольник':
#     a, b = int(input()), int(input())
#     print(a * b)
# elif t == 'круг':
#     r = int(input())
#     print(3.14 * r ** 2)

# a, b, c = int(input()), int(input()), int(input())
# max = 0
# min = 0
# another = 0
# if a >= b and a >= c:
#     max = a
#     if b > c:
#         min = c
#         another = b
#     else:
#         min = b
#         another = c
# elif b >= a and b >= c:
#     max = b
#     if a > c:
#         min = c
#         another = a
#     else:
#         min = a
#         another = c
# elif c >= a and c >= b:
#     max = c
#     if a > b:
#         min = b
#         another = a
#     else:
#         min = a
#         another = b
# print (max, '\n', min, '\n', another)

# a,b,c = int(input()), int(input()), int(input())

# if a < b:
# 	a, b = b, a
# if a < c:
# 	a, c = c, a
# if b > c:
# 	b, c = c, b
# print(a, '\n', b, '\n', c)

# n = int(input())
# programmers = 'программистов'
# if ((n == 1) or (n % 10 == 1)) and (n % 100 != 11):
#     programmers = 'программист'
# elif (1 < n < 5) or (1 < n % 10 < 5) and not (11 < n % 100 < 15):
#     programmers = 'программиста'   
# print(n, programmers)
# print(11 % 100)

# n=int(input())
# print(n,'программист'+('ов' if n%10==0 or 4<n%10<10 or 10<n%100<15 else 'а' if 1<n%10<5 else ''))

# a = str(input())
# first = int(a[0]) + int(a[1]) + int(a[2])
# second = int(a[3]) + int(a[4]) + int(a[5])
# if first == second:
#     print('Счастливый')
# else:
#     print('Обычный')

# a, b, c, d, e, f = input()
# n = int(a) + int(b) + int(c)
# m = int(d) + int(e) + int(f)
# if n == m:
#     print ('Счастливый')
# else:
#     print ('Обычный')

# n = int(input())
# c = 1
# while c <= n:
#     print('*' * c)
#     c += 1

# stars = '*'
# n = int(input())
# while len(stars) <= n:
#     print(stars)
#     stars += '*'

# print(0 % 2) # остаток от деления на 2 == 0!

# a = int(input())
# sum = a
# while a != 0:
#     a = int(input())
#     sum += a
# print(sum)

# a = True
# sum = 0
# while a:
#     a = int(input())
#     sum += a
# print(sum)

# a, b, d = int(input()), int(input()), 1
# while ((d % a != 0) or (d % b != 0)):
#     d += 1
# print(d)

# a, b = int(input()), int(input())
# d = a
# while d % b:
#     d += a
# print(d)

# i = 0
# while i < 5:
#     a, b = input().split()
#     a = int(a)
#     b = int(b)
#     if (a == 0) and (b == 0):
#         break # досрочное ззавершение цикла
#     if (a == 0) or (b == 0):
#         continue # переходим к следующей итерации
#     print(a * b)
#     i += 1

# while True:
#     a = int(input())
#     if a < 10:
#         continue
#     elif a > 100:
#         break
#     print(a)

# for i in 2, 3, 5:
#     print(i * i)

# range (start=0, to, step=1)
# range(1, 10, 3) -> 1, 4, 7 (10 не входит)

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("*", end='')
#     print()

# Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными 
# блоками. Для тренировок ему бы очень пригодилась программа, которая 
# показывала бы блок таблицы умножения.

# Напишите программу, на вход которой даются четыре числа a, b, c и d, 
# каждое в своей строке. Программа должна вывести фрагмент таблицы умножения 
# для всех чисел отрезка [a; b] на все числа отрезка [c;d].

# Числа a, b, c и d являются натуральными и не превосходят 10, 
# a <= b, c <= d.

# Следуйте формату вывода из примера, для разделения элементов внутри строки 
# используйте '\t' — символ табуляции. Заметьте, что левым столбцом и верхней 
# cтрокой выводятся сами числа из заданных отрезков — заголовочные столбец 
# и строка таблицы.

# a, b, c, d = (int(input()) for x in range(4))
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# print('', '\t', end='')
# for i in range(c, d + 1):
#     print(i, end='\t')
# print()
# for j in range(a, b + 1):
#     print(j, '\t', end='')
#     for k in range(c, d + 1):
#         print(j * k, end='\t')
#     print()

#a, b = (int(i) for i in input().split()) # если данные подаются одной строкой через пробел
#a, b, c, d = (int(input()) for x in range(4)) # если данные вводятся по одному числу

# Напишите программу, которая считывает с клавиатуры два числа a и b, 
# считает и выводит на консоль среднее арифметическое всех чисел из 
# отрезка [a; b], которые кратны числу 3.

# В приведенном ниже примере среднее арифметическое считается для чисел на 
# отрезке [-5; 12]. Всего чисел, делящихся на 3, на этом отрезке
#  6: -3, 0, 3, 6, 9, 12. Их среднее арифметическое равно
#   4.5

# На вход программе подаются интервалы, внутри которых всегда есть хотя бы 
# одно число, которое делится на 3

# a, b = int(input()), int(input())
# i = 0
# sum = 0
# for j in range(a, b + 1):
#     if j % 3 == 0:
#         i += 1
#         sum += j
# print(sum / i)

# Символы строки
# Примеры: var="Hello!"
# var[0] -> 'H' - только первый символ
# var[1:] -> 'ello!' - все символы начиная со второго
# var[:3] -> 'Hell' - все символы до четвертого
# var[1:4] -> 'ello' - символы со второго по пятый
# var[::] -> 'Hello!' - выведутся все символы
# var[::2] -> 'Hlo' - здесь выбирается каджый второй символ строки, т.е. 0й 2й и 4й
# var[::-1] -> '!olleH'- выведутся все символы, но с шагом -1 - каждый символ, но в обратном порядке.

# genome = input()
# print(genome.count('C'))

# Напишите программу, которая вычисляет процентное содержание символов 
# G (гуанин) и C (цитозин) в введенной строке (программа не должна 
# зависеть от регистра вводимых символов).

# Например, в строке "acggtgttat" процентное содержание символов G и C 
# равно 4 / 10 * 100 = 40​, где 4 - это количество символов G и C,  а 10 - 
# длина строки.

# genome = input()
# cnt = genome.upper().count('G') + genome.upper().count('C')
# print((cnt / len(genome)) * 100)
# genome = input().upper()

# s = 'abcdefghijk'
# print(s[-1:-10:-2])

# Узнав, что ДНК не является случайной строкой, только что поступившие в Институт 
# биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, 
# который сжимает повторяющиеся символы в строке.

# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной 
# строки заменяются на этот символ и количество его повторений в этой позиции строки.

# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и 
# выводит закодированную последовательность на стандартный вывод. Кодирование должно 
# учитывать регистр символов.

# s = input()
# short = ''
# i = 1
# cnt = 1
# while i < (len(s)):
#     if i == len(s) - 1:
#         short += s[i] + str(cnt)
#         break
#     if s[i-1] == s[i]: 
#         cnt += 1
#         i += 1
#         continue
#     short += s[i-1] + str(cnt)
#     i += 1
#     cnt = 1
# print(short)

# s = input()
# short = ''
# i = 0
# cnt = 1
# while i < len(s):
#     if len(s) == 1:
#         short += s[i] + str(1)
#         break
#     if i == len(s) - 2:
#         if s[i] == s[i + 1]:
#             short += s[i] + str(cnt + 1)
#             break
#         else:
#             short += s[i] + str(cnt)
#             short += s[i+1] + str(1)
#             break
#     if s[i] == s[i + 1]: 
#         cnt += 1
#         i += 1
#         continue
#     short += s[i] + str(cnt)
#     i += 1
#     cnt = 1
# print(short)

# genome = input()+' '
# s = 0
# n=genome[0]
# short = ''
# for i in genome:       
#     if n!=i:
#         short += n + str(s)
#         s=0
#         n=i
#     s+=1
# print(short)

# Списки

# Для работы со списками определен ряд операторов и функций:
# len(s) Длина последовательности s
# x in s Проверка принадлежности элемента последовательности. В новых версиях Python можно проверять принадлежность подстроки строке. Возвращает True или False
# x not in s = not x in s
# s + s1 Конкатенация последовательностей
# s*n или n*s Последовательность из n раз повторенной s. Если n < 0, возвращается пустая последовательность.
# s[i] Возвращает i-й элемент s или len(s)+i-й, если i < 0
# s[i:j:d] Срез из последовательности s от i до j с шагом d будет рассматриваться ниже
# min(s) Наименьший элемент s
# max(s) Наибольший элемент s
# s[i] = x i-й элемент списка s заменяется на x
# s[i:j:d] = t Срез от i до j (с шагом d) заменяется на (список) t
# del s[i:j:d] Удаление элементов среза из последовательности

# Кроме того, для списков определен ряд методов.
# append(x) Добавляет элемент в конец последовательности
# count(x) Считает количество элементов, равных x
# extend(s) Добавляет к концу последовательности последовательность s
# index(x) Возвращает наименьшее i, такое, что s[i] == x. Возбуждает исключение ValueError, если x не найден в s
# insert(i, x) Вставляет элемент x в i-й промежуток
# pop(i) Возвращает i-й элемент, удаляя его из последовательности
# reverse() Меняет порядок элементов s на обратный
# sort([cmpfunc]) Сортирует элементы s. Может быть указана своя функция сравнения cmpfunc

# a = [0 for i in range(5)]
# print(a)
# [0, 0, 0, 0, 0]

# a = [i * i for i in range(5)]
# print(a)
# [0, 1, 4, 9, 16]

# a = [int(i) for i in input().split()]
# print(a)
# 2 5 3 7
# [2, 5, 3, 7]

# можно генерить списки с выбором элементов по условию 
# [ i for i in range(x) if condition] например:
# [i * 3 for i in range(5) if i % 3 == 0] -> выведет кубы всех цифр кратным трём,
# входящим в этот список

# Напишите программу, на вход которой подается одна строка с целыми числами.
# Программа должна вывести сумму этих чисел.

# Используйте метод split строки. 

# a = [int(i) for i in input().split()]
# sum = 0
# for n in a:
#     sum += n
# print(sum)


# Напишите программу, на вход которой подаётся список чисел одной строкой. 
# Программа должна для каждого элемента этого списка вывести сумму двух его 
# соседей. Для элементов списка, являющихся крайними, одним из соседей 
# считается элемент, находящий на противоположном конце этого списка. 
# Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается 
# список "13 6 9 15 7" (без кавычек).

# Если на вход пришло только одно число, надо вывести его же.

# Вывод должен содержать одну строку с числами нового списка, разделёнными 
# пробелом.
# 1 3 5 6 10

# a = [int(i) for i in input().split()]
# if len(a) == 1: 
#     print(a[0])
# else:
#     i = 0
#     while i < len(a) - 1:
#         print(a[i-1] + a[i+1], end=' ')
#         i += 1
#     print(a[-2] + a[0])
    
# a=[int(i) for i in input().split()]
# if len(a)>1:
#     for i in range(len(a)):
#         print(a[i-1]+a[i+1-len(a)])
# else:
#     print(a[0])


# Напишите программу, которая принимает на вход список чисел в одной 
# строке и выводит на экран в одну строку значения, которые встречаются 
# в нём более одного раза.

# Для решения задачи может пригодиться метод sort списка.

# Выводимые числа не должны повторяться, порядок их вывода может быть
# произвольным.

# Sample Input 1:
# 4 8 0 3 4 2 0 3
# [0, 0, 2, 3, 3, 4, 4, 8]
# Sample Output 1:
# 0 3 4

# a = [int(i) for i in input().split()]
# a.sort()
# i = 1
# n = 0
# while i < len(a):
#     if a[i-1] == a[i]:
#         n += 1
#     elif a[i-1] != a[i] and n > 0:
#         print(a[i-1], end=' ')
#         n = 0
#     i += 1
#     if i == len(a) and n > 0:
#         print(a[i-1], end=' ')

# a, b = [int(i) for i in input().split()], []
# for i in a:
#     if a.count(i) > 1 and b.count(i) == 0:
#         b.append(i)
# for i in b:
#     print(i, end=" ")

# ls = [int(i) for i in input().split()]
# for i in set(ls):
#     if ls.count(i) > 1:
#         print(i, end=' ')

# s = [int(i) for i in input().split()]
# s.sort()
# i = 0
# while i < len(s):
#     if s.count(s[i]) > 1:      # думаю, тут всё понятно
#         print (s[i], end=' ')  
#         i += s.count(s[i])     # прибавляем к индексу количество повторений текущего элемента,
#                                # чтобы перескочить на первый отличающийся от текущего
#     else:                      
#         i += 1

# n = 3
# a = [[0] * n] * n
# print(a)
# a[0][0] = 5
# print(a)

# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# [[5, 0, 0], [5, 0, 0], [5, 0, 0]]

# a = [[0] * n for i in range(n)]
# a = [[0 for j in range(n)] for i in range(n)]
# a[0][0] = 7
# print(a)

# [[7, 0, 0], [0, 0, 0], [0, 0, 0]]


# Рисуем поле Сапёра, если есть бюомба выводим *, если нет - выводим количество 
# бомб рядом. если 0 - выводим точку

# n, m, k = (int(i) for i in input().split())   # строки, столбцы, кол-во мин
# a = [[0 for j in range(m)] for i in range(n)]    # пустая таблица из 0
# for i in range(k):    # перебираем кол-во мин
#     rw, cl = (int(i) - 1 for i in input().split())   # записываем строку и столбец одной мины при каждом проходе
#     a[rw][cl] = -1   # записываем мину по координатам столбца и колонны
# #дальше нам нужно заглянуть в каждую пустую ячейку, и находясь в ячейке пробежаться еще вокруг и поискать мины

# for i in range(n):    # перебираем строки
#     for j in range(m):   # перебираем столбцы 
#         if a[i][j] == 0:   # ячейка без мины
#             for di in range(-1, 2):   # перебираем соседние строки (просто цифры -1 0 1)
#                 for dj in range(-1, 2):   # перебираем соседние столбцы (просто цифры -1 0 1)
#                     ai = i + di     # координата по строке
#                     aj = j + dj     # координата по столбцу
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:   # проверка вхождения в диапазон и мины по соседству
#                         a[i][j] += 1

# # в поле 5х4 цикл пройдется 5 * 4 = 20 раз по ячейкам и, находясь в ячейке еще по 9(3*3) проходов вокруг. Всего будет 20*9=180 раз (или n*m*9 раз)
# # так же можно искать не пустые ячейки, а ячейки с миной (if a[i][j] == -1) и вокруг прибавлять единицу
# # код почти такой же, меняется последнее условие:
# '''
#                     if 0 <= ai < n and 0 <= aj < m:
#                         if a[ai][aj] != -1: # проверка, чтобы не увеличивать на 1 мину
#                             a[ai][aj] += 1
# '''
# # дальше просто заменяем -1 на "*" и 0 на "."

# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()

#  Правильный codestyle
# for row in range(rows):
#     for column in range(columns):
#         matrix[row][column] == -1:

# Напишите программу, которая считывает с консоли числа (по одному в строке) до тех 
# пор, пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму 
# квадратов всех считанных чисел.

# Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после 
# этого считывание продолжать не нужно.

# В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что 
# сумма этих чисел равна нулю и выводим сумму их квадратов, не обращая внимания на то,
# что остались ещё не прочитанные значения.
# int(i) for i in input().split()

# Моё решение:
# a = [int(input())]
# while sum(a) != 0:
#     a.append(int(input()))
# for i in range(len(a)):
#     a[i] = a[i] * a[i]
# print(sum(a))

# Оптимизированный:
# a = [int(input())]
# while sum(a) != 0: # while sum(s)!=0: s.append(int(input())) -> запись в одну строку
#     a.append(int(input()))
# print(sum(i**2 for i in a))

# Без использования списков (требует меньше памяти):
# m = int(input())
# t2 = m**2
# while m != 0:
#     t = (int(input()))
#     m += t
#     t2 += t**2
# print(t2)

# Напишите программу, которая выводит часть последовательности 
# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). 
# На вход программе передаётся неотрицательное целое число n — столько элементов 
# последовательности должна отобразить программа. На выходе ожидается последовательность
# чисел, записанных через пробел в одну строку.

# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

# Моё решение:
# n = int(input())
# i = 0
# a = []
# while len(a) < n:
#     for j in range(i):
#         a.append(i)
#     i += 1
# a = a[:n]
# for k in a:
#     print(k, end=' ')

# Оптимизированное:
# n = int(input())
# a = []
# i = 0
# while len(a) < n:
#     a += [i] * i
#     i += 1
# print(*a[:n]) -> * позволяет выводить через любой символ, по умолчанию - пробел.
# # строка выводит распакованный список a (* - unpucking) от начала до n-ного элемента не включительно.

# Без саммива:
# n = int(input())
# count = 0
# curr = 1
# for i in range(n):
#     print(curr, end=' ')
#     count += 1
#     if count == curr:
#         curr += 1
#         count = 0

# Загуглил последовательность, у нее оказалась готовая форма для любого элемента и 
# соответственно печатаем его:
# a(n)=floor(1/2+sqrt(2n))

# import math
# x = int(input())
# print(*[int( 1/2 + math.sqrt(2 * n) ) for n in range(1, x + 1)])

# Напишите программу, которая считывает список чисел lst из первой строки и число 
# x из второй строки, которая выводит все позиции, на которых встречается число x 
# в переданном списке lst.

# Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку
# "Отсутствует" (без кавычек, с большой буквы).

# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
# 5 8 2 7 8 8 2 4
# 8
# вывод: 1 4 5

# Моё решение:
# lst = [int(i) for i in input().split()]
# x = int(input())
# if lst.count(x) == 0:
#     print('Отсутствует')
# else:
#     i = 0
#     while i < len(lst):
#         if lst[i] == x:
#             print(i, end = ' ')
#         i += 1

# Оптимизированное:
# lst = [int(i) for i in input().split()]
# x = int(input())
# if x not in lst:
#     print('Отсутствует')
# else:
#     for i in range(len(lst)):
#         if lst[i] == x: 
#             print(i, end = ' ')

# for i, a in enumerate(lst): 
#     if a == x:
#         print(i)

# Напишите программу, на вход которой подаётся прямоугольная матрица в виде 
# последовательности строк. После последней строки матрицы идёт строка, содержащая 
# только строку "end" (без кавычек, см. Sample Input).

# Программа должна вывести матрицу того же размера, у которой каждый элемент в 
# позиции i, j равен сумме элементов первой матрицы на позициях 
# (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент 
# находится с противоположной стороны матрицы.

# В случае одной строки/столбца элемент сам себе является соседом по соответствующему 
# направлению.
# Sample Input 1:
# 9 5 3
# 0 7 -1
# -5 2 9
# end
# Sample Output 1:
# 3 21 22
# 10 6 19
# 20 16 -1

# Моё решение:
# matrix = []
# while True:
#     row = [i for i in input().split()]
#     if row[0] == 'end':
#         break
#     else:
#         for i in range(len(row)):
#             row[i] = int(row[i])
#     matrix += [row]    
#         # matrix.append(row)

# for i in range(len(matrix)): 
#     for j in range(len(matrix[i])): 
#         print((matrix[i-1][j] + matrix[i+1-len(matrix)][j] + matrix[i][j-1] + matrix[i][j+1-len(matrix[i])]), end=' ')
#     print()

# matrix.append([int(i) for i in row.split()])

# a = [0, 1, 2, 3, 4]
# b = a
# a = a[0:3]
# print('a - ', a)
# print('b - ', b)


# Выведите таблицу размером n×n, заполненную числами от 1 до n^2 

# по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
# Sample Input:
# 5
# Sample Output:

# 1  2  3  4  5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# Моё решение:
# n = int(input())
# if n > 1:
#     matrix = [[0] * n for i in range(n)]
#     i = 1
#     start = 0
#     count = int((n)//2)
#     lenght = int(n)
#     n -= 1
#     while count:
#         for j in range(n):
#             matrix[start][start+j] = i
#             i += 1

#         for j in range(n):
#             matrix[start+j][-1-start] = i
#             i += 1

#         for j in range(n):
#             matrix[-1-start][-1-j-start] = i
#             i += 1

#         for j in range(n):
#             matrix[-1-start-j][start] = i
#             i += 1

#         n -= 2
#         start += 1
#         count -= 1
#     center = lenght//2
#     if lenght%2 == 1:
#         matrix[center][center] = lenght**2
    
#     for j in range(lenght):
#         for k in range(lenght):
#             print(matrix[j][k], end="  ")
#         print()
# else:
#     print(n)

# Функции

# def f(n):
#     return n * 10 + 5

# print(f(f(f(10))))


# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей 
# числовой прямой:
# 1−(x+2)**2 при x≤−2
# -x/2 при −2<x≤2
# (x−2)**2 +1 при 2 < x
# ​
# def f(x):
#     if x <= -2:
#         return(1 - ( x+2 )**2)
#     elif -2 < x <= 2:
#         return(-x/2)
#     else:
#         return((x - 2)**2 + 1)

# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него 
# все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется 
# только изменение переданного списка, например:

# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]

# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]

# Мой вариант:

# def modify_list(l):
#     i = 0
#     while i < len(l):
#         if l[i] % 2 == 1:
#             l.pop(i)
#         else:
#             l[i] = int(l[i] / 2)
#             i += 1

# Подсмотренный:
# def modify_list(l):
#     l[:] = [i//2 for i in l if not i % 2]

# from typing_extensions import ParamSpecArgs


# Множдества:

# s = set()
# basket = {'apple', 'orange', 'banana', 'orange', 'pear'}

# 'orange' in basket # True
# 'python' in basket # False

# s.add(element)
# s.remove(element) #ошибка, если элемента нет в множестве
# s.discard(element) # удалит без ошибки
# s.clear()

# basket = {'apple', 'orange', 'banana', 'orange', 'pear'}
# for x in basket:
#     print(x)
# banana
# orange
# pear
# apple

# Словари

# dict, {}
# d = {'a':100, 10:150}
# print(d['a']) # 100
# print(d[10]) # 150

# dictionary = {}

# key in dictionary # True/False
# key not in dictionary # True/False
# dictionary[key] = value # добавить ключ + значение
# dictionary[key] # если нет - будет ошиька
# dictionary.get(key) # ошибки не будет, вернут None
# del dictionary[key]

# d = {'C':14, 'A':12, 'T':9, 'G':18}
# for key in d:
#     print(key, end='') # G C A T
# for key in d.keys():
#     print(key, end='') # G C A T
# for value in d.values:
#     print(value, end='') # 9 18 12 14
# for key, values in d.items():
#     print(key, values, end=';') # G 18; C 14; A 12; T 9

# Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: 
# key и value.

# Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по 
# этому ключу.
# Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2 * key2. Если и 
# ключа 2 * key2 нет, то нужно добавить ключ 2 * key2 в словарь и сопоставить ему список из 
# переданного элемента [value].

# Требуется реализовать только эту функцию, кода вне её не должно быть.
# Функция не должна вызывать внутри себя функции input и print.

# Пример работы функции:

# d = {}

# # print(update_dictionary(d, 1, -1))  # None
# # print(d)                            # {2: [-1]}
# # update_dictionary(d, 2, -2)
# # print(d)                            # {2: [-1, -2]}
# # update_dictionary(d, 1, -3)
# # print(d)                            # {2: [-1, -2, -3]}

# Моё решение:
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#     elif key not in d and key*2 not in d:
#         d[key*2] = [value]
#     else:
#         d[key*2].append(value)
