from graph_builder import *

'''
static module for graph manipulations and
'''
def anding_two_graphs(graph_start, graph_end):
    '''anding two graphs '''
    graph_start.final_node.add_next_node(graph_end.start_node)
    return graph(graph_start.start_node)

def oring_two_graphs(graph1, graph2):
    '''
    perfoming an or operation on two graphs
    '''
    common_start = node()
    common_start.add_next_node(graph1.start_node)
    common_start.add_next_node(graph2.start_node)
    common_end = node()
    graph1.final_node.add_next_node(common_end)
    graph2.final_node.add_next_node(common_end)
    return graph(common_start)
