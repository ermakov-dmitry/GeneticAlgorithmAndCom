#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

import randPaths
import genes

def findShortestPath(filename, iter, childs, mutation, start, finish):

	#Set here: number of iteration, childs(in one iteration), and possibility of mutation in percent:
	ITERATION = iter
	CHILDS = childs
	MUT = mutation

	GRAPH = [[]]
	NODES=0
	with open(filename, "rt") as f:
		reader = csv.reader(f)
		for line in reader:
			for x in range(len(line)):
				GRAPH[NODES].append(int(line[x]))
			if(NODES>0):
				GRAPH[NODES].remove(NODES)
			NODES += 1
			GRAPH.append([NODES])
	GRAPH.pop()


	# startCity = input('Please choose first Node(from 0 to ' + str(NODES-1) + '): ')
	# stopCity = input('Please choose last Node(from 0 to ' + str(NODES-1) + '): ')

	startCity = start
	stopCity = finish

	startCity = int(startCity)
	stopCity = int(stopCity)

	paths = randPaths.randPaths(GRAPH, NODES, startCity, stopCity)
	firstParent = paths.makeRoute()
	secondParent = paths.makeRoute()

	gen = genes.Genes(GRAPH, ITERATION, NODES, CHILDS, MUT, startCity, stopCity, firstParent, secondParent)
	gen.makeRoute()

	firstPath = gen.returnBestRoute()
	return firstPath