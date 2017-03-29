from .graph_builder import *
import logging
from .helpers import *
'''
static module for graph manipulations andq
'''
def anding_two_graphs(graph_start, graph_end):
    '''anding two graphs '''
    logging.info('started anding operation')
    (graph1, graph2) = change_to_graphs(graph_start, graph_end)
    graph1.end_node.add_next_node(accpeting_func_elipson(graph2.start_node))
    logging.info('finished anding operation')
    return graph(graph1.start_node)

def oring_two_graphs(graph1, graph2):
    '''
    perfoming an OR operation on two graphs
    '''
    (graph1, graph2) = change_to_graphs(graph1, graph2)
    common_start = node()
    common_start.add_next_node(accpeting_func_elipson(graph1.start_node))
    common_start.add_next_node(accpeting_func_elipson(graph2.start_node))
    common_end = node()
    graph1.end_node.add_next_node(accpeting_func_elipson(common_end))
    graph2.end_node.add_next_node(accpeting_func_elipson(common_end))
    return graph(common_start)

def positive_knlee(graph_input):
    '''preformaing a posisitve knlee cloure on given graph'''
    graph_in = change_to_graphs(graph_input)
    new_start = node()
    new_end = node()
    new_start.add_next_node(accpeting_func_elipson(graph_in.start_node))
    graph_in.end_node.add_next_node(accpeting_func_elipson(new_end))
    graph_in.end_node.add_next_node(accpeting_func_elipson(graph_in.start_node))
    return graph(new_start)

def knlee(graph_inn):
    '''preforming a knlee closure on graph'''
    graph_in = change_to_graphs(graph_inn)
    new_start = node()
    new_end = node()
    new_start.add_next_node(accpeting_func_elipson(graph_in.start_node))
    graph_in.end_node.add_next_node(accpeting_func_elipson(new_end))
    graph_in.end_node.add_next_node(accpeting_func_elipson(graph_in.start_node))
    new_start.add_next_node(accpeting_func_elipson(new_end))
    return graph(new_start)

    
if(__name__ == "main"):
    anding_two_graphs(graph(node()), graph(node()))
