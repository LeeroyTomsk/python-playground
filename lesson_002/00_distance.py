#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов


sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2



moscow = sites ['Moscow']
london = sites ['London']
paris = sites ['Paris']

moscow_to_london = london_to_moscow = (str((moscow [0] - london[0])**2 + (moscow[1] - london[1])**2))
moscow_to_paris = paris_to_moscow = (str((moscow [0] - paris [0]) **2 +(moscow [1] - paris[1])**2))
paris_to_london = london_to_paris = (str((paris [0] - london[0])**2 + (paris[1] - london[1])**2))

distances = {'From Moscow to London' : moscow_to_london, 'From London to Moscow' : london_to_moscow, 'From Moscow to Paris' : moscow_to_paris, 'From Paris to Moscow' : paris_to_moscow, 'From London to Paris' : london_to_paris, 'From Paris to London' : paris_to_london}


# TODO здесь заполнение словаря

print(distances)




