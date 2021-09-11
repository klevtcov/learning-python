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

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print('', '\t', end='')
for i in range(c, d + 1):
    print(i, end='\t')
print()
for j in range(a, b + 1):
    print(j, '\t', end='')
    for k in range(c, d + 1):
        print(j * k, end='\t')
    print()
