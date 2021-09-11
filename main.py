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