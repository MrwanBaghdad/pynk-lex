import logging
from .graph_builder import *
logging.basicConfig(level=logging.INFO)
def replace_all(str_in,rep_dict):
    temp = str_in
    logging.info('replaceing string')
    for i in rep_dict.items():
        logging.debug(i)
        temp = temp.replace(i[0], i[1])
    logging.info('finished replaceing string')
    return temp

def change_to_graphs(inp1,inp2):
    '''
    if inputs are char make a simple NFA from them and pass them for
    the operation handling functions as tuples,
    can\'t pass by reference as maybe a char which is imutable
    '''
    if type(inp1) is graph:
        graph1 = inp1
    else:
        start_node = node()
        start_node.add_next_node(accepting_func_char(node(), inp1))
        graph1 = graph(start_node)

    if type(inp2) is graph:
        graph2 = inp2
    else:
        start_node = node()
        start_node.add_next_node(accepting_func_char(node, inp2))
        graph2 = inp2
    
    return (graph1, graph2)

def accepting_func_range(next_node, range_start, range_end):
    '''
        using closures a higher order function is returned that hide the next node
        this function represents the vertices between two node
    '''
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
        if char  == '-':
            op_stack.append(char)
        elif char in ['[',']']:
            pass
        elif char in ['+','*','|','.','(']:
            try:
                if op_stack.__len__()  == 0:
                    op_stack.append(char)
                elif precedence[op_stack[-1]] > precedence[char] :
                    while(precedence[op_stack[-1]] > precedence[char] or op_stack.__len__()>0):
                        temp = op_stack.pop()
                        postfix_stack.append(temp)
                    op_stack.append(char)
            except (IndexError, AttributeError, ValueError) as err:
                logging.error(err)
        elif char == ')':
            temp = op_stack.pop()
            while temp != '(' and op_stack.__len__()>0:
                postfix_stack.append(temp)
                temp = op_stack.pop()
        else:
            postfix_stack.append(char)
        
    while op_stack.__len__() > 0:
        postfix_stack.append(op_stack.pop())
    return ''.join(postfix_stack)

if __name__ =='__main__':
    #FIXME: this case
    print(to_postfix('(a-b).(0-9)'))