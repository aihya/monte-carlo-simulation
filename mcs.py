# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mcs.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aihya <abdechahid.ihya@hotmail.c>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/05/06 19:24:37 by aihya             #+#    #+#              #
#    Updated: 2019/08/01 18:04:13 by aihya            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import math

def randGen(c):
    print("Generating coordinates...")
    table = []
    for i in range(c):
        table.append((random.random(), random.random()))
    print("Done.")
    return (table)

def get_pi(n):
    table = randGen(n)
    print("Calculating distances...")
    distances = [math.sqrt(p[0]*p[0] + p[1]*p[1]) for p in table]
    print("Done.\nSeparating circle_distances from square_distances...")
    circle_distances = [i for i in distances if i <= 1]
    square_distances = [i for i in distances if i > 1]
    print("Done.\nCalculating circle_count...")
    circle_count = len(circle_distances)
    print("Done.\nCalculating sc_count...")
    sc_count = len(square_distances) + circle_count
    print("Done.")
    return (4 * (circle_count / sc_count))

print(get_pi(7000000))
