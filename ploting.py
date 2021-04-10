#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def plot_rectangles():
    # first rectangle
    plt.gca().add_patch(Rectangle((1, 6), 5, 3, linewidth=1, edgecolor='k', facecolor='none'))
    plt.gca().add_patch(Rectangle((5, 5), 1, 1, linewidth=1, edgecolor='k', facecolor='none'))
    plt.text(3.25, 7, '1', fontsize=12)

    # second rectangle
    plt.gca().add_patch(Rectangle((1, 12), 5, 3, linewidth=1, edgecolor='k', facecolor='none'))
    plt.gca().add_patch(Rectangle((5, 11), 1, 1, linewidth=1, edgecolor='k', facecolor='none'))
    plt.text(3.25, 13, '2', fontsize=12)

    # third rectangle
    plt.gca().add_patch(Rectangle((1, 18), 5, 3, linewidth=1, edgecolor='k', facecolor='none'))
    plt.gca().add_patch(Rectangle((5, 17), 1, 1, linewidth=1, edgecolor='k', facecolor='none'))
    plt.text(3.25, 19, '3', fontsize=12)

    # 4th rectangle
    plt.gca().add_patch(Rectangle((9, 6), 5, 3, linewidth=1, edgecolor='k', facecolor='none'))
    plt.gca().add_patch(Rectangle((13, 5), 1, 1, linewidth=1, edgecolor='k', facecolor='none'))
    plt.text(11.25, 7, '4', fontsize=12)

    # 5th rectangle
    plt.gca().add_patch(Rectangle((9, 12), 5, 3, linewidth=1, edgecolor='k', facecolor='none'))
    plt.gca().add_patch(Rectangle((13, 11), 1, 1, linewidth=1, edgecolor='k', facecolor='none'))
    plt.text(11.25, 13, '5', fontsize=12)

    # 6th rectangle
    plt.gca().add_patch(Rectangle((9, 18), 5, 3, linewidth=1, edgecolor='k', facecolor='none'))
    plt.gca().add_patch(Rectangle((13, 17), 1, 1, linewidth=1, edgecolor='k', facecolor='none'))
    plt.text(11.25, 19, '6', fontsize=12)

    # 7th rectangle
    plt.gca().add_patch(Rectangle((17, 6), 5, 3, linewidth=1, edgecolor='k', facecolor='none'))
    plt.gca().add_patch(Rectangle((17, 5), 1, 1, linewidth=1, edgecolor='k', facecolor='none'))
    plt.text(19.25, 7, '7', fontsize=12)

    # 8th rectangle
    plt.gca().add_patch(Rectangle((17, 12), 5, 3, linewidth=1, edgecolor='k', facecolor='none'))
    plt.gca().add_patch(Rectangle((17, 11), 1, 1, linewidth=1, edgecolor='k', facecolor='none'))
    plt.text(19.25, 13, '8', fontsize=12)

    # 9th rectangle
    plt.gca().add_patch(Rectangle((17, 18), 5, 3, linewidth=1, edgecolor='k', facecolor='none'))
    plt.gca().add_patch(Rectangle((17, 17), 1, 1, linewidth=1, edgecolor='k', facecolor='none'))
    plt.text(19.25, 19, '9', fontsize=12)

    # zero rectangle
    plt.gca().add_patch(Rectangle((9, 0), 5, 2, linewidth=1, edgecolor='k', facecolor='none'))
    plt.text(11.25, 0.35, '0', fontsize=12)


def plot_solution(route):
    coordinats = [[14.5, 2.5],
                  [6.5, 5.5],
                  [6.5, 11.5],
                  [6.5, 17.5],
                  [14.5, 5.5],
                  [14.5, 11.5],
                  [14.5, 17.5],
                  [16.5, 5.5],
                  [16.5, 11.5],
                  [16.5, 17.5],
                  [6.5, 2.5],
                  [16.5, 2.5],
                  [8.5, 4.5],
                  [14.5, 4.5],
                  [8.5, 5.5],
                  [8.5, 10.5],
                  [14.5, 10.5],
                  [8.5, 11.5],
                  [8.5, 16.5],
                  [14.5, 16.5],
                  [8.5, 17.5]]
    x_route = []
    y_route = []
    # plt.figure(figsize=(10, 8), dpi=20)
    for idx in route:
        x_route.append(coordinats[idx][0])
        y_route.append(coordinats[idx][1])
    plt.plot(x_route, y_route, '--')
    for i in range(10):
        plt.plot(coordinats[i][0], coordinats[i][1], 'ok')
    for i in range(10, len(coordinats)):
        plt.plot(coordinats[i][0], coordinats[i][1], '.', color='k')
    plt.xlabel('$x$, m')
    plt.ylabel('$y$, m')
    plt.xlim([0, 25])
    plt.ylim([0, 25])

    plot_rectangles()
    plt.show()
