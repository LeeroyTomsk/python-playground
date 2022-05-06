#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# TODO здесь ваш код

halo_value = violator_songs_list[3][1]
enjoy_value = violator_songs_list[6][1]
clean_value = violator_songs_list[-1][1]
total_value = halo_value + enjoy_value + clean_value

print ('Три песни звучат ' + str(total_value) + ' минут')

# Есть словарь песен группы Depeche Mode

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# TODO здесь ваш код

sweet = violator_songs_dict ['Sweetest Perfection']
policy = violator_songs_dict ['Policy of Truth']
bluedress = violator_songs_dict ['Blue Dress']

nextvalue = round ( sweet + policy + bluedress, 2) #тут пришлось юзать round, т.к. без него выдавало 9 в периоде

print ('А другие 3 песни звучат ' + str(nextvalue) + ' минут')