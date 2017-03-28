#TODO: read from lexical rule and make NFA
#TODO: add logging
import logging
import os

from .graph_builder import *
from .graph_mani import *
from .helpers import *
from .preproc import preproc
import re

logging.basicConfig(level=logging.DEBUG)
def gen_great_NFA(input_lines):
    '''generate one NFA for whole lang'''
    input_lines = preproc.transfrom(input_lines)
    literal_flag = False
    final_NFA_stack = []
    for all_line in input_lines:
        if re.search(r'=',all_line) is not None:
            continue
        line = all_line.split('=')[1].strip()
        line_pstfx = to_postfix(line)
        stk = []
        for char in line_pstfx:
            if literal_flag is True:
                stk.append(char)
                literal_flag = False
            elif char in ['.', '+', '*', '|', '-']:
                if char == '.':
                    c2 = stk.pop()
                    c1 = stk.pop()
                    stk.append(anding_two_graphs(c1, c2))

                elif char in ['*','+']:
                    #FIXME: make knlee and positive knlee
                    # knlee_graph(stk.pop())
                    if(char == '*'):
                        stk.append(knlee(stk.pop()))
                    elif(char == '+'):
                        stk.append(positive_knlee(stk.pop()))
                elif char == '|':
                    c2 = stk.pop()
                    c1 = stk.pop()
                    stk.append(oring_two_graphs(c1,c2))

                elif char == '-':
                    c2 = stk.pop()
                    c1 = stk.pop()
                    start_node = node()
                    start_node.add_next_node(accepting_func_range(node(),c1,c2))
                    stk.append(graph(start_node))
                elif char == '\\':
                    continue
        '''one NFA Stack in stk push to NFA stack'''
        if stk.__len__ ==1  and type(stk[0]) != graph:
            logging.error('regex parsed more than one nfa ')
            return RuntimeError
        stk[0].end_node.final_state = all_line.split('=')[0]
    
    '''oring all graphs in NFA'''
    super_node = node()
    for nfa in final_NFA_stack:
        super_node.add_next_node(accpeting_func_elipson(nfa.start_node))
    
    return super_node

def gen_elipson_table(super_node):
    '''ONE DFA TO RULE THEM ALL'''
    all_nodes = []
    all_nodes.append(super_node)
    def get_all_node(super_node):
        for node in super_node.get_next_node(master_key=True):
            if node not in all_nodes:
                all_nodes.append(node)
                return get_all_node(node)
            else:
                return
    get_all_node(super_node)
    elipson_dict = []
    node_temp = node()
    elipson_dict[0] = accepting_func_char(node_temp,'c').__code__.co_code
    elipson_dict[1] = accepting_func_range(node_temp, 0, 10).__code__.co_code
    elipson_dict[2] = accpeting_func_elipson(node_temp).__code__.co_code

    elipson_state_table = {}
    def dfs_elipson_edges(starting_node_list, standing_node):
        #use non locals
        for edge in standing_node.next_node:
            if edge.__code__.co_code == elipson_dict[2]:
                if edge(master_key=True) not in starting_node_list:
                    dfs_next_node= edge(master_key=True)
                    starting_node_list.append(dfs_next_node)
                    return dfs_elipson_edges(starting_node_list, dfs_next_node)
            else: 
                return

    for node in all_nodes:
        elipson_state_table[node] = list()
        dfs_elipson_edges(elipson_state_table, node)
    return elipson_state_table

def gen_great_dfa(start_super_node, elipson_dict):
    '''make lexical DFAs great again'''
    
    # get dict of all elipson moves
    #get all nodes:
    #TODO:


    # TODO: make postfix algo
    # lex_lines = helpers.to_postfix(lex_lines) 
    # nfa_stack = []
    # op_stack = []
    # char_stack = []
    # curr_nfa = graph(node())
    # for line in lex_lines:
    #     for char in line:
    #         if char == '-':
    #             c2 = char_stack.pop()
    #             c1 = char_stack.pop()
    #             curr_nfa.end_node.add_next_node(
    #                 accepting_func_range(node(), c1, c2)
    #             )
    #         elif char.isspace():
    #             nfa_stack.append(curr_nfa)
    #             curr_nfa = None

    #         elif char.alnum():
    #             char_stack.append(char)

    #         elif char == '|':
    #             if curr_nfa is None:
    #                 n1 = nfa_stack.pop()
    #                 n2 = nfa_stack.pop()
    #                 #FIXME: 
    #                 # oring_two_graphs()
    #         elif char == '*':
