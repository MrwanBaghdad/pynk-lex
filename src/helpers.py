import logging
logging.basicConfig(level=logging.INFO)
def replace_all(str_in,rep_dict):
    temp = str_in
    logging.info('replaceing string')
    for i in rep_dict.items():
        logging.debug(i)
        temp = temp.replace(i[0], i[1])
    logging.info('finished replaceing string')
    return temp

def accepting_func_range(next_node, range_start, range_end):
    '''
        using closures a higher order function is returned that hide the next node
        this function represents the vertices between two node
    '''
    def accepting_output(testing_char, master_key=False):
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
    def accepting_output(testing_char, master_key=False):
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
    def accepting_output(testing_char, master_key=False):
        '''returned function accepts any char'''
        return next_node
    return accepting_output