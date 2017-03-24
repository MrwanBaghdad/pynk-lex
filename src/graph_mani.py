from graph_builder import *
import logging
'''
static module for graph manipulations and
'''
def anding_two_graphs(graph_start, graph_end):
    '''anding two graphs '''
    graph_start.final_node.add_next_node(graph_end.start_node)
    return graph(graph_start.start_node)

def oring_two_graphs(graph1, graph2):
    '''
    perfoming an OR operation on two graphs
    '''
    common_start = node()
    common_start.add_next_node(graph1.start_node)
    common_start.add_next_node(graph2.start_node)
    common_end = node()
    graph1.final_node.add_next_node(common_end)
    graph2.final_node.add_next_node(common_end)
    return graph(common_start)

def accepting_func_range(next_node, range_start, range_end):
    '''
        using closures a higher order function is returned that hide the next node
        this function represents the vertices between two node
    '''
    def accepting_output(testing_char, master_key=False):
        '''the higer order function with a master key flag
        to allow accesing final node for graph class
        accepting a range'''
        if master_key:
            return next_node
        if testing_char >= range_start and testing_char <= range_end:
            return next_node
        else:
            return None
    return accepting_output

def accepting_func_char(next_node, accept_char):
    '''
        using closures a higher order function is returned that hide the next node
        this function represents the vertices between two node
    '''
    def accepting_output(testing_char, master_key=False):
        '''the higer order function with a master key flag
        to allow accesing final node for graph class
        accepting a specfic char '''
        if master_key:
            return next_node
        if testing_char == accept_char:
            return next_node
        else:
            return None
    return accepting_output

def accpeting_func_elipson(next_node):
    def accepting_output(testing_char, master_key=False):
        return next_node
