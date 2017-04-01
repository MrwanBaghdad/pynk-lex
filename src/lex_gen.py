

import logging
import os

from .graph_builder import *
from .graph_mani import *
from .helpers import *
from .preproc import preproc
import re
from .state_class import create_new_state

logging.basicConfig(level=logging.DEBUG)
def gen_great_NFA(in_lines):
    logging.debug('Content of inputs range at GEN NFA STAR')
    '''generate one NFA for whole lang'''
    input_lines = in_lines
    logging.info('Started generating NFA')

    literal_flag = False
    super_node = node()
    for all_line in input_lines:
        if re.search(r'=',all_line) is not None:
            logging.debug('found definition')
            continue
        line = all_line.split(':')[1].strip()
        line_pstfx = to_postfix(line)
        logging.info('working on postfix '+line_pstfx)
        stk = []
        for char in line_pstfx:
            logging.debug('cur char in postfix '+char)
            if literal_flag is True:
                logging.info('adding literal char in stack '+char)
                stk.append(char)
                literal_flag = False
            elif char in ['.', '+', '*', '|', '-']:
                if char == '.':
                    logging.info('preforming and on two graphs')
                    logging.debug(inputs_range)
                    c2 = stk.pop()
                    c1 = stk.pop()
                    stk.append(anding_two_graphs(c1, c2))
                    logging.debug(inputs_range)

                elif char in ['*','+']:
                    if(char == '*'):
                        logging.info('preforming closure')
                        stk.append(knlee(stk.pop()))
                    elif(char == '+'):
                        logging.info('preforming positive colsure')
                        stk.append(positive_knlee(stk.pop()))
                elif char == '|':
                    logging.info('preforming or')
                    c2 = stk.pop()
                    c1 = stk.pop()
                    stk.append(oring_two_graphs(c1,c2))

                elif char == '-':
                    logging.info('adding range edge')
                    c2 = stk.pop()
                    c1 = stk.pop()
                    start_node = node()
                    start_node.add_next_node(accepting_func_range(node(),c1,c2))
                    stk.append(graph(start_node))
            elif char == "\\":
                logging.debug("found literal"+char)
                literal_flag = True
                continue
            else:
                stk.append(char)
        '''one NFA Stack in stk push to NFA stack'''
        if stk.__len__() ==1  and type(stk[0]) != graph:
            logging.error('regex parsed more than one nfa ')
            raise RuntimeError
        logging.debug('all_line: '+all_line)
        logging.debug(stk)
        stk[0].end_node.final_state = all_line.split(':')[0].strip()
        super_node.add_next_node(accpeting_func_elipson(stk[0].start_node))
    
    return super_node

ALL_NODES = []

def gen_elipson_table(super_node):
    '''get an elipson nodes mapping for every node'''
    logging.info('Started building elipson table')
    ALL_NODES.append(super_node)

    def get_all_node(super_node):

        # temp_list = list(filter(lambda x: x not in all_nodes, super_node.get_next_node(master_key=True)))
        for nn in super_node.get_next_node(master_key=True):
            if nn not in ALL_NODES:
                ALL_NODES.append(nn)
                return get_all_node(nn)
            else:
                return
    logging.info('started getting all nodes')
    get_all_node(super_node)
    logging.info('finsihed getting all nodes')
    elipson_state_table = {}
    for cur_node in ALL_NODES:
        elipson_state_table[cur_node] = list()
        elipson_state_table[cur_node].append(cur_node)
        dfs_elipson_edges(elipson_state_table[cur_node], cur_node)
    return elipson_state_table

def gen_great_dfa(start_super_node, elipson_dict):
    '''make lexical DFAs great again'''
    #every node check for all inputs from inputs_range
    sym_table = {}

    for N in ALL_NODES:
        cur_table = sym_table[create_new_state(elipson_dict[N])] = dict()
        for i in inputs_range:
            cur_table[i] = list()
            logging.info('finding states for input '+i)
            for n in elipson_dict.get(N):
                #first we get list of nodes accepting current input i
                next_nodes = n.get_next_node(i)
                #we get elipson nodes for these nodes
                logging.debug("next_nodes")
                logging.debug(next_nodes)
                # elipson_next_nodes  = [ elipson_dict.get(j) for j in next_nodes]
                elipson_next_nodes = list()
                try:
                    for j in next_nodes:
                         cur_table[i].extend(elipson_dict.get(j)) 
                except TypeError as err:
                    pass

                #append them in the current symtable with row of node
            cur_table[i] = create_new_state(cur_table[i])
    return sym_table


    # get dict of all elipson moves
    #get all nodes:
    #DONE 


    
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
    
    #                 # oring_two_graphs()
    #         elif char == '*':
