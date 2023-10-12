# from test import Animal

# TODO: 1 урок

# wolf = Animal('волк', 'лес', 12)
# pig = Animal('свинья', 'город', 4)
#
# animals = [wolf, pig]
# for animal in animals:
#     print(animal.getInfo())
#     # animal.setLocation()
# car = Car()
# car.setMotor(wolf)
# print(car.forward())



# TODO: 2 урок

from random import randint

# animal1 = Animal('Заяц', randint(100, 200))
# animal1 = Animal('Волк', randint(100, 200))
# animal1 = Animal('Утка', randint(100, 200))
# animals = [animal1, animal2, animal3]


# animals = []
# animalName = ['Заяц', 'Черепаха', 'Утка', 'Гусь', 'Собака']
# for name in animalName:
#     animals.append(Animal(name,randint(100,200)))
#
#
# road = int(input('Введите длину дороги: '))
# for animal in animals:
#     if animal.getSpeed() >= road:
#         print(f'{animal.getType()} пробежал')
#     else:
#         print(f'{animal.getType()} сошел с дистанции')



# TODO: 3 с/р

from test2 import Auto

sedan = Auto('седан', '1.6', 'красный')
jeep = Auto('джип', '2.0', 'синий')
coupe = Auto('купе', '1.8', 'желтый')

auto = [sedan, jeep, coupe]
for a in auto:
    print(a.getInfo())
