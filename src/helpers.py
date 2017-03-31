import logging
from .graph_builder import *

logging.basicConfig(level=logging.INFO)

inputs_range = []

def replace_all(str_in,rep_dict):
    temp = str_in
    logging.info('replaceing string')
    for i in rep_dict.items():
        logging.debug(i)
        temp = temp.replace(i[0], i[1])
    logging.info('finished replaceing string')
    return temp

def change_to_graphs(inp1,inp2=None):
    '''
    if inputs are char make a simple NFA from them and pass them for
    the operation handling functions as tuples,
    can\'t pass by reference as maybe a char which is imutable
    '''
    logging.info("started changinng graphs")
    if type(inp1) is graph:
        graph1 = inp1
    else:
        start_node = node()
        start_node.add_next_node(accepting_func_char(node(), inp1))
        graph1 = graph(start_node)

    if inp2 is None:
        return graph1

    if type(inp2) is graph:
        graph2 = inp2
    else:
        start_node = node()
        start_node.add_next_node(accepting_func_char(node, inp2))
        graph2 = inp2

    logging.info('finished changing to graphs')
    return (graph1, graph2)

def accepting_func_range(next_node, range_start, range_end):
    '''
        using closures a higher order function is returned that hide the next node
        this function represents the vertices between two node
    '''
    global inputs_range
    inputs_range.extend([ chr(i) for i in range(ord(range_start), ord(range_end)+1)\
    if chr(i) not in inputs_range])
    def accepting_output(testing_char=None, master_key=False):
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
    global inputs_range
    if accept_char not in inputs_range:
        inputs_range.append(accept_char)
    def accepting_output(testing_char=None, master_key=False):
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
    '''accepting function for elipson char'''
    def accepting_output(testing_char=None, master_key=False):
        '''returned function accepts any char'''
        return next_node
    return accepting_output

def to_postfix(str_in):
    ''' convert infix to postfix string '''
    logging.info('start conversion to postfix')
    postfix_stack = []
    op_stack = []
    precedence = {}
    precedence['-'] = 3
    precedence['+'] = 2
    precedence['*'] = 2
    precedence['|'] = 1
    precedence['.'] = 1
    precedence['('] = 0
    for char in str_in:
        if char == '-':
            op_stack.append(char)
        elif char in ['[', ']']:
            pass
        elif char in ['+', '*', '|', '.', '(']:
            try:
                if op_stack.__len__() == 0:
                    op_stack.append(char)
                elif precedence[op_stack[-1]] >= precedence[char]:
                    while precedence[op_stack[-1]] >= precedence[char] or op_stack.__len__() > 0:
                        temp = op_stack.pop()
                        postfix_stack.append(temp)
                    op_stack.append(char)
            except (IndexError, AttributeError, ValueError) as err:
                logging.error(err)
        elif char == ')':
            temp = op_stack.pop()
            while temp != '(' and op_stack.__len__() > 0:
                postfix_stack.append(temp)
                temp = op_stack.pop()
        else:
            postfix_stack.append(char)

    while op_stack.__len__() > 0:
        postfix_stack.append(op_stack.pop())
    return ''.join(postfix_stack)

elipson_code = accpeting_func_elipson(node()).__code__.co_code

def dfs_elipson_edges(starting_node_list, standing_node):
    '''
    dfs recuservily; every traverse step we get  elipson edge
    adding the node reached by given edge to dict with key as the starting node.
    comparing edges using bytecode
    '''
    #use non locals
    for edge in standing_node.next_node:
        if edge.__code__.co_code == elipson_code:
            #Found an elipson edge
            dfs_next_node = edge(master_key=True)
            if dfs_next_node not in starting_node_list:
                starting_node_list.append(dfs_next_node)
                dfs_elipson_edges(starting_node_list, dfs_next_node)


if __name__ =='__main__':
    #FIXME: this case
    print(to_postfix('a-z.(0-9)'))
    print(to_postfix('((0-9)(a-z))*'))
    f1 =  accepting_func_char(node(), 'c')
    assert f1.__code__.co_code == accepting_func_char(node(),'d').__code__.co_code
    print(accpeting_func_elipson(node()).__code__.co_code)
