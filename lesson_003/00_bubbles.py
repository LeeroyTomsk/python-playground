# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код

point = sd.get_point(100, 100)
radius = 5
for i in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код


def bubble(point, step):
    radius = 50
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, width=2)
        radius += step


point = sd.get_point(300, 300)
bubble(point=point, step=10)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

radius = 20
for i in range(10):
    point = sd.get_point(50 + i * radius * 3, 50)
    sd.circle(center_position=point, radius=radius)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

radius = 20
for i in range(10):
    for j in range(3):
        point = sd.get_point(50 + i * radius * 3, 50 + j * radius * 3)
        sd.circle(center_position=point, radius=radius)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код


for i in range(100):
    point = sd.random_point()
    radius = 10
    color = sd.random_color()
    sd.circle(center_position=point, radius=radius, color=color, width=2)


sd.pause()
