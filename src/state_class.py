from .graph_builder import node
import logging
logging.basicConfig(level=logging.DEBUG)
all_states = []
class State():
    ''' representation of state in DFA '''
    cur_ord = ord('a')
    def __init__(self, list_of_nodes):
        self.list_of_nodes = list_of_nodes
        self.cur_ord = State.cur_ord
        State.cur_ord+=1
        all_states.append(self)
    
    def get_nodes(self):
        return self.list_of_nodes
    def __str__(self):
        return chr(self.cur_ord)


def create_new_state(list_of_nodes):
    logging.info('Start trying creating new state')
    logging.debug(list_of_nodes)
    pre_state = list(filter(lambda s: set(s.list_of_nodes) == set(list_of_nodes), all_states))
    if pre_state.__len__() == 1:
        logging.info('found state with same nodes')
        return pre_state[0]
    elif pre_state.__len__() > 1:
        raise RuntimeError
    else:
        logging.info('Creating new state')
        return State(list_of_nodes)

if __name__ == '__main__':
    s1 = State(node())
    s2 = State(node()) 
    n1 = node()
    n2 = node()
    n3 = node()
    n4 = node()
    set([n1,n2])
    create_new_state([n1,n2])
    # assert create_new_state([n1,n2]) == create_new_state([n1,n2])
    print(s1, s2)
