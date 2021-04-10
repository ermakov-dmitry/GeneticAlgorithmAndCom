#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import csv
import re

import createRoute
import ploting


def create_data_model():
    """Stores the data for the problem."""
    data = {'distance_matrix': []}
    filename = 'ourRouteTopology.csv'
    with open(filename, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            line = []
            for y in row:
                line.append(int(y))
            data['distance_matrix'].append(line)

    depot = createRoute.idx_start_point_in_matrix
    data['num_vehicles'] = 1
    data['depot'] = depot
    return data


def print_solution(manager, routing, solution):
    """Prints solution on console."""
    # print('Objective: {} metres'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = ' Route for vehicle on point map:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += '{} -> '.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += '{}\n'.format(manager.IndexToNode(index))
    route_idx = re.findall('(\d+)', plan_output)
    plan_output += '\n Route distance:\n{} metres'.format(route_distance)
    print(plan_output)
    print('\n', 'Route for vehicle on global map:')
    end_value = -1
    plot_route = []
    for i in range(len(route_idx) - 1):
        idx = int(route_idx[i])
        next_idx = int(route_idx[i + 1])
        current_route = createRoute.matrix[idx][next_idx][0]
        for j in range(len(current_route)):
            if current_route[j] != end_value:
                end_value = current_route[j]
                plot_route.append(current_route[j])
                print(current_route[j], end=' ')
                if j != len(current_route) - 1 or i != len(route_idx) - 2:
                    print('->', end=' ')
    print()
    print(plot_route)
    ploting.plot_solution(plot_route)

def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(manager, routing, solution)


if __name__ == '__main__':
    main()
