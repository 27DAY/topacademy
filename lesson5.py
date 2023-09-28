# def S(a,b):
#     return a*b
#
# a = 10
# b = 5
# print(f'Площадь прямоугольника = {S(a, b)}')



# import math
#
# def S():
#     return math.pi*r**2
#
# r = int(input('Какой радиус круга?: '))
#
# print(f'Площадь круга = {math.pi*r**2}')



# import math
#
# def S(a, b, r):
#     result ={}
#     areaCircle = math.pi * r**2
#     areaSquare = a * b
#     result.update({'S квадрата': areaSquare})
#     result.update({'S круга': areaCircle})
#     return result
#
# a = 10
# b = 10
# r = 10
#
# for key,item in S(a, b, r).items():
#     print(f'{key}: {item}')
#
# print(S(a, b, r).items())




# import random as r
# def getHealth():
#     health = 100
#     while True:
#         a = r.randint(1, 99)
#         b = r.randint(1, 99)
#         if a > b:
#             health -= 20
#         if health <= 0:
#             print('Ваше здоровье закончилось ')
#             break
# getHealth()



# import random as r
#
# def getHealth(a, b):
#     if a > b:
#         return True
#     else:
#         return False
# hp = 100
# if True:
#     print(1)
# while hp > 0:
#     if getHealth(
#             r.randint(1, 99),
#             r.randint(1, 99)
#     ):
#         hp -= 20
# print('Ваше здоровье закончилось ')