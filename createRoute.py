#!/usr/bin/env python
# -*- coding: utf-8 -*-

import geneticAlgo
import csv

iteration = 50
childs = 100
mut = 100
filename = 'smallTopology.csv'

# small: 0 - 7
# medium: 0 - 11

number_of_points = input('Please enter number of points of route: ')
number_of_points = int(number_of_points)
points = []
for i in range(number_of_points):
    points.append(int(input('Enter number of {0} point: '.format(i + 1))))

matrix = []

for i in range(number_of_points):
    matrix.append([None] * number_of_points)

for i in range(number_of_points):
    for j in range(i, number_of_points):
        if i == j:
            matrix[i][j] = [0], 0
        else:
            matrix[i][j] = geneticAlgo.findShortestPath(filename, iteration, childs, mut, points[i], points[j])
            matrix[j][i] = geneticAlgo.findShortestPath(filename, iteration, childs, mut, points[j], points[i])

with open("ourRouteTopology.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    for i in range(len(matrix[0])):
        row_csv = []
        for j in range(len(matrix[0])):
            row_csv.append(matrix[i][j][1])
        file_writer.writerow(row_csv)

print('Choose start point from route point -', end='')
for x in points:
    print(' ', end='')
    print(x, end='')
print(':', end=' ')
start_point = input()
start_point = int(start_point)
idx_start_point_in_matrix = 0
for i in range(number_of_points):
    if points[i] == start_point:
        idx_start_point_in_matrix = i
        break

if points.count(start_point) == 0:
    raise Exception('Not found start point')

filename = 'ourRouteTopology.csv'
for x in matrix:
    print(x)
