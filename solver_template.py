import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils_sp18 import *

"""
======================================================================
  Complete the following function.
======================================================================
"""
# All kingdoms that have yet to be visited.
unvisited = set()

# Conquered kingdoms. Conquered kingdoms are free pieces. They have fallen and there is no 
# need to put extra time into taking these places. 
conquered = set()

# Surrendered kingdoms. Surrendered kingdoms can be conquered. However they do not need to be finished. 
surrendered = set()



def solve(list_of_kingdom_names, starting_kingdom, adjacency_matrix, params=[]):
    """
    Write your algorithm here.
    Input:
        list_of_kingdom_names: An list of kingdom names such that node i of the graph corresponds to name index i in the list
        starting_kingdom: The name of the starting kingdom for the walk
        adjacency_matrix: The adjacency matrix from the input file

    Output:
        Return 2 things. The first is a list of kingdoms representing the walk, and the second is the set of kingdoms that are conquered
    """
    raise Exception('"solve" function not defined')
    # return closed_walk, conquered_kingdoms


#############################################
#############################################
#############################################
######### MAIN HELPERS ######################
#############################################
#############################################
#############################################


def get_neighbors(kingdom, adjacency_matrix):
    # Todo 
    # Return a list of neighbors
    return adjacency_matrix[kingdom]



#############################################
#############################################



# Returns a dictionary that contains the cost and node associated with 
# that traversal cost. Has helper functions to pull data from it. look below
def traverse_cheapest(starting_point, adjacency_matrix):
    # We want to start at our starting point 

    # From our starting point we want to go the cheapest child node to get to 
    # This should be a one liner 

    neighbors = get_neighbors(starting_point, adjacency_matrix)
    try:
        assert len(neighbors) != 0
        curr_cheapest_cost = sys.maxint 
        curr_node = neighbors[0]
        curr_cost = adjacency_matrix[starting_point][curr_node]
        cost_dictionary = {"node" : curr_node, "cost" : curr_cost}
        for node in neighbors:
            if curr_cost < curr_cheapest_cost:
                curr_cheapest_cost = curr_cost
                cost_dictionary["node"] = curr_node
                cost_dictionary["cost"] = curr_cost
        return cost_dictionary
    except:
        print("No neighbors")
        return None



#############################################
#############################################
#############################################
########## UTILITY FUNCTIONS ################
#############################################
#############################################
#############################################

# Retrieve the node from a cost dictionary
def get_cost(cost_dict):
    assert cost_dict is not None 
    return cost_dict["cost"]


def get_node(cost_dict):
    assert cost_dict is not None
    return cost_dict["node"]

#############################################
#############################################
#############################################
#############################################


"""
======================================================================
   No need to change any code below this line
======================================================================
"""


def solve_from_file(input_file, output_directory, params=[]):
    print('Processing', input_file)
    
    input_data = utils.read_file(input_file)
    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
    closed_walk, conquered_kingdoms = solve(list_of_kingdom_names, starting_kingdom, adjacency_matrix, params=params)

    basename, filename = os.path.split(input_file)
    output_filename = utils.input_to_output(filename)
    output_file = f'{output_directory}/{output_filename}'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    utils.write_data_to_file(output_file, closed_walk, ' ')
    utils.write_to_file(output_file, '\n', append=True)
    utils.write_data_to_file(output_file, conquered_kingdoms, ' ', append=True)


def solve_all(input_directory, output_directory, params=[]):
    input_files = utils.get_files_with_extension(input_directory, 'in')

    for input_file in input_files:
        solve_from_file(input_file, output_directory, params=params)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('--all', action='store_true', help='If specified, the solver is run on all files in the input directory. Else, it is run on just the given input file')
    parser.add_argument('input', type=str, help='The path to the input file or directory')
    parser.add_argument('output_directory', type=str, nargs='?', default='.', help='The path to the directory where the output should be written')
    parser.add_argument('params', nargs=argparse.REMAINDER, help='Extra arguments passed in')
    args = parser.parse_args()
    output_directory = args.output_directory
    if args.all:
        input_directory = args.input
        solve_all(input_directory, output_directory, params=args.params)
    else:
        input_file = args.input
        solve_from_file(input_file, output_directory, params=args.params)
