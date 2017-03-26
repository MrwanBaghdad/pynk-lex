from .graph_builder import *
import logging
from .helpers import *
'''
static module for graph manipulations andq
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
    common_start.add_next_node(accpeting_func_elipson(graph1.start_node))
    common_start.add_next_node(accpeting_func_elipson(graph2.start_node))
    common_end = node()
    graph1.final_node.add_next_node(accpeting_func_elipson(common_end))
    graph2.final_node.add_next_node(accpeting_func_elipson(common_end))
    return graph(common_start)

def positive_knlee(graph):
    '''preformaing a posisitve knlee cloure on given graph'''
    new_start = node()
    new_end = node()

if(__name__ == "main"):
    anding_two_graphs(graph(node()), graph(node()))