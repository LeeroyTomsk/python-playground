# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

sd.resolution = (1200, 600)
count_of_colors = rainbow_colors.__len__()
i = 0
for i in range(0, count_of_colors):
    rainbow_value = rainbow_colors[i]
    sd.line(sd.get_point(50 + i*5, 50), sd.get_point(350 + i*5, 450), color=rainbow_value, width=4)
    i += 1

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (см sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.resolution = (1200, 600)
count_of_colors = rainbow_colors.__len__()
i = 0
for i in range(0, count_of_colors):
    rainbow_value = rainbow_colors[i]
    sd.circle(sd.get_point(300, 0), radius=150 - 10*i, color=rainbow_value, width=10)
    i += 1

sd.pause()
