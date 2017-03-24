class node():
    def __init__(self, final_state=False):
        '''
        create a node with a ref to other nodes and final state with false
        '''
        self.next_node = []
        self.final_state = final_state

    def add_next_node(self, accepting_func):
        '''
            init next nodes ref as a list of nodes if not init,
            append otherwise
        '''
        self.next_node.append(accepting_func)

    def get_next_node(self, testing_char, master_key=None):
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
        if self.end_node is not None:
            return
        for i in self.start_node.next_node:
            temp = i(master_key=True)
            if temp not in hist_stack:
                hist_stack.append(temp)
                self.run_graph(temp, hist_stack)
            if temp.final_state:
                self.end_node = temp
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
    n1 = node()
    n2 = node()
    g1 = graph(n1)
    print(n2, n1, n1.next_node)

