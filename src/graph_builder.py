import logging

logging.basicConfig(level=logging.DEBUG)
class node():
    def __init__(self, final_state=False):
        '''
        create a node with a ref to other nodes and final state with false
        '''
        self.next_node = []
        if final_state is False:
            self.final_state = None
        else:
            self.final_state = final_state

    def add_next_node(self, accepting_func):
        '''
            init next nodes ref as a list of nodes if not init,
            append otherwise
        '''
        self.next_node.append(accepting_func)

    def get_next_node(self, testing_char=None, master_key=None):
        '''
            refractor for getting next node
        '''
        nodes_returned = []
        if master_key is True:
            # return self.next_node.values()
            for i in self.next_node:
                nodes_returned.append(i(master_key=True))
            return nodes_returned
        else:
            for i in self.next_node:
                nodes_returned.append(i(testing_char=testing_char))
            return nodes_returned

class graph:
    def __init__(self, start_node):
        '''get the start and final nodes of a graph '''
        self.start_node = start_node
        self.end_node = None
        temp_history = []
        self.run_graph(self.start_node, temp_history)

    def run_graph(self, start_node, hist_stack):
        '''
        DFS to get end node
        '''
        logging.debug(start_node)
        hist_stack.append(start_node)
        self.end_node = start_node
        if self.end_node.final_state:
            return
        # if self.end_node is not None:
        #     return
        for next_node in self.end_node.get_next_node(master_key=True):
            if next_node not in hist_stack:
                self.run_graph(next_node, hist_stack)
                # go to next node
            # if temp not in hist_stack:
            #     hist_stack.append(temp)
            #     self.run_graph(temp, hist_stack)
            # if temp.final_state:
            #     self.end_node = temp
#depreceated
        # for i in start_node.next_nodes.values():
        #     if i.final_state is True:
        #         self.final_nodes.append(i)
        #     if i in hist_stack:
        #         continue
        #     else:
        #         hist_stack.append(i)
        #         self.run_graph(i, hist_stack)



if __name__ == '__main__':
    from helpers import *
    n1 = node(final_state=True)
    n2 = node()
    n1.add_next_node(accepting_func_range(n2,0,10))
    n2.add_next_node(accepting_func_char(n1,'a'))
    g1 = graph(n1)
    print(g1.end_node is n1)

