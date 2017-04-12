from .context import src
import src.lex_gen as lex
from unittest import TestCase
from pprint import pprint
import logging
class test_lexical_analyzer(TestCase):
    def test_gen_great_NFA(self):
        # nod = lex.gen_great_NFA(['y:id.'])
        su_nod = lex.gen_great_NFA(['y:A.D'])
        logging.debug(lex.inputs_range)
        el_table = lex.gen_elipson_table(su_nod)
        for i in su_nod.get_next_node(master_key=True):
            self.assertIn(i,el_table)
        r = lex.gen_great_dfa(su_nod, el_table)
        pprint(el_table)
        pprint(r)
        

class test_elipson_table_gen(TestCase):
    def test_elipson_table(self):
        n1 = lex.node()
        n2 = lex.node()
        n3 = lex.node()
        n4 = lex.node()
        n5 = lex.node()

        n1.add_next_node(lex.accpeting_func_elipson(n2))
        n1.add_next_node(lex.accpeting_func_elipson(n3))
        n2.add_next_node(lex.accpeting_func_elipson(n4))
        n4.add_next_node(lex.accepting_func_char(n5, 'c'))

        e_table = lex.gen_elipson_table(n1)
        
        self.assertTrue(type(e_table) ==dict)
        self.assertTrue(type(e_table[n1] == list))
        self.assertTrue(e_table[n1] is not False)
        self.assertIn(n2, e_table[n1])
        self.assertIn(n3, e_table[n1])
        self.assertIn(n4, e_table[n1])

        self.assertFalse( n5 in e_table[n1])
        self.assertIn(n4, e_table[n2])
        self.assertNotIn(n5, e_table[n4])

        self.tearDown()
