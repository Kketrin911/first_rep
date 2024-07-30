# import random


# name = input ('введите имя: ')
# print ('Привет,', name)
# a = 2
# b = 20
# print (a+b)
# name = input ('Введите имя: ')
# lastname = input ('Введите фамилию: ')
# print ('Привет', name, 'твоя фамилия', lastname)
# x= -5 #абсолютное значение
# y = abs(x)
# print (y)
# x = [2,8,9,4,7]
# y = max (x)
# z = min (x)
# print (y)
# print (z)
# def get_sum(a, b) -> int:
#     return a + b


# print(get_sum(5, 7))
# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print(last_digit)
# print(first_digit)
# print('Искомое число =', last_digit * 10 + first_digit)

# num = 7825
# d = num % 10 #последняя цифра
# c = (num // 10) % 10
# b = (num // 100) % 10
# a = (num // 1000) #первая цифра
# print('Цифра в позиции тысяч равна', a)
# print('Цифра в позиции сотен равна', b)
# print('Цифра в позиции десятков равна', c)
# print('Цифра в позиции единиц равна', d)
# n = int(input())
# n%2 == 0 #четное число
# n%2 !=0 #нечетное число

# n = 1245
# n4 = n % 10 #последнее число
# n3 = n // 10 % 10
# n2 = n // 100 % 10
# n1 = n // 1000 #первое число
# print (n1, n2, n3, n4)

# a = 67
# b = 8
# c = 8
# d = 89
# ab = 0
# cd = 0
# if a<=b:
#     ab = a
# else:
#     ab = b
# if c<=d:
#     cd = c
# else:
#     cd = d
# if ab <= cd:
#     print (ab)
# else:
#     print (cd)

# age = 60
# if age<=13:
#     print ('детство')
# elif 14<=age<=24:
#     print ('молодость')
# elif 25<=age<=59:
#     print ('зрелость')
# else:
#     print ('старость')
# a = 4
# b = -22
# c = 1
# summa = 0
# if a >= 0:
#     summa = a
# if b >= 0:
#     summa = summa + b
# if c >= 0:
#     summa = summa + c
# print(summa)
# line1 = input()
# line2 = input()

# if (line1 != "красный" and line1 != "синий" and line1 != "желтый") or (line2 != "красный" and line2 != "синий"  and line2 != "желтый"):
#     print ('ошибка цвета')

# if line1 == "красный":
#     if line2 == 'синий':
#         print ('фиолетовый')
#     elif line2 == 'желтый':
#         print ('оранжевый')
#     elif line2 == 'красный':
#         print ('красный')

# if line1 == "синий":
#     if line2 == 'красный':
#         print ('фиолетовый')
#     elif line2 == 'желтый':
#         print ('зеленый')
#     elif line2 == 'синий':
#         print ('синий')

# if line1 == "желтый":
#     if line2 == 'синий':
#         print ('зеленый')
#     elif line2 == 'желтый':
#         print ('желтый')
#     elif line2 == 'красный':
#         print ('оранжевый')
# import math
# a = float(input())
# b = float(input())
# c = float(input())
# d = b**2 - 4*a*c
# if d < 0:
#     print('Нет корней')
# elif d == 0:
#     print (-b/(2*a))
# elif d > 0:
#     x1 = (-b+math.sqrt(d))/(2*a)
#     x2 = (-b + d**0.5)/(2*a)
#     print(max(x1, x2))
#     print(min(x1, x2))
    
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# n4 = int(input())
# n5 = int(input())
# n6 = int(input())
# n7 = int(input())
# n8 = int(input())
# n9 = int(input())
# n10 = int(input())
# m = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
# count = 0
# for i in m:
#     if i%2==0 and m.index(9): print ('YES')
#     if i%2!=0: print ('NO')
#     break
        

    
# total = 0 
# for a in range (1, 151):
#     for b in range (a,151):
#         for c in range (b, 151):
#             for d in range (c, 151):
#                 for e in range (d, 151):
#                     if a**5 + b**5 + c**5 + d**5 == e**5:
#                         total +=1
#                         print ('a=', a, 'b=', b, 'c=', c, 'd=', d, 'e=', e)
# print ('количество решений ', total)                
# n = int (input())
# if 102<=n<=10**9:
#     sum_in_1_to_99 = 99*(99+1)//2
#     sum_in_1_to_n = n*(n+1)//2
#     itog = sum_in_1_to_n - sum_in_1_to_99
#     print (itog)
# n = int(input())
# stroka =  str(input())
# if (1<=n<=500000) and (len(stroka)==n):

#     count_a = 0
#     for i in stroka:
#         if i == 'a':
#             count_a +=1
#     print (count_a)

# import re
# text = ""
# while True:
#     try:
#         line = str(input())
#         if not line:
#             break
#         text = text + line
#     except EOFError:
#         break
# lower_text = (text.lower())
# without_punctuation = re.sub(r'[^\w\s]', '', lower_text)
# print(without_punctuation.count(' a ') + without_punctuation.count('a '))

# n = int(input())
# if 1<=n<=1000:
#     matrix = [list(map(int, input().split())) for _ in range(n)]
#     for i in 
    
# n = int(input())
# if 1<=n<=10**8:
#     if n == 1:
#         zarazn_person = 1
#     else:
#         zarazn_person = (n-1) * 4
#     print (zarazn_person)   

    
