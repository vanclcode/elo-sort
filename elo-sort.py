#!/usr/bin/env python3
DEF_SCORE = 1500
FACTOR = 400
K = 48
DEV = 1

from random import randint
from save import items


itemsLen = len(items)
totalTests = 0

while True:
    i_1 = randint(0, itemsLen - 1)
    i_2 = randint(0, itemsLen - 1)

    treshold = (totalTests/itemsLen) + DEV
    if i_1 == i_2 or items[i_1][2] > treshold or items[i_2][2] > treshold:
        continue
    inp = input(f"a: {items[i_1][0]:<9} VS b: {items[i_2][0]:<9} ? ")
    if inp == '':
        items = sorted(items, key=lambda x: -x[1])
        i_1 = None
        i_2 = None

        i = 1
        for item in items:
            print(f"{i:>3}. {item[0]:<12} {item[1]:4.1f} ({item[2]:})")
            i += 1

        continue
    elif inp == 'a' or inp == 'b':
        was_1 = items[i_1][1]
        was_2 = items[i_2][1]

        items[i_1][2] += 1
        items[i_2][2] += 1
        totalTests += 2
        
        delta = 1/(1 + 10**((items[i_1][1] - items[i_2][1]) / FACTOR))
        
        if inp == 'a':
            items[i_1][1] += K * delta
            items[i_2][1] -= K * delta
        elif inp == 'b':
            items[i_1][1] -= K * (1 - delta)
            items[i_2][1] += K * (1 - delta)
                
        # print(f"{items[i_1][0]}: {was_1} -> {items[i_1][1]}")
        # print(f"{items[i_2][0]}: {was_2} -> {[i_2][1]}")

        
