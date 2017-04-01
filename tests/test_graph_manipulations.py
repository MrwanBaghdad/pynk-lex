import logging
from .context import src
import src.graph_builder as graph_builder
import src.graph_mani as graph_mani
from unittest import TestCase
import src.helpers as helpers

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(message)s')


class TestingGraphOperations(TestCase):
    def setUp(self):
        n11 = graph_builder.node()
        n12 = graph_builder.node()
        n13 = graph_builder.node()

        n21 = graph_builder.node()
        n22 = graph_builder.node()
        n23 = graph_builder.node()

        n11.add_next_node(helpers.accepting_func_char(n12, 'a'))
        n12.add_next_node(helpers.accpeting_func_elipson(n13))
        n12.add_next_node(helpers.accpeting_func_elipson(n11))

        n21.add_next_node(helpers.accpeting_func_elipson(n22))
        n22.add_next_node(helpers.accpeting_func_elipson(n23))
        self.g2 = graph_builder.graph(n21)
        self.g1 = graph_builder.graph(n11)

    def test_oring(self):
        g3 = graph_mani.oring_two_graphs(self.g1,self.g2)
        TestCase.assertEqual(self,self.g2.end_node.get_next_node(master_key=True),self.g1.end_node.get_next_node(master_key=True))

    
    def test_anding(self):
        g3 = graph_mani.anding_two_graphs(self.g1, self.g2)
        TestCase.assertEqual(self, self.g1.end_node.get_next_node(master_key=True)[0], self.g2.start_node)
        TestCase.assertEqual(self, g3.start_node, self.g1.start_node)
        # gerror = graph_mani.anding_two_graphs(g3,g3) #NOTE:

    
    def test_knleess(self):
        g3 = graph_mani.knlee(self.g1)
        TestCase.assertEqual(self, g3.start_node.get_next_node(master_key=True)[0], self.g1.start_node)
        TestCase.assertIn(self, g3.end_node, self.g1.end_node.get_next_node(master_key=True))
    
    def test_positive_knlees(self):
        g3 = graph_mani.positive_knlee(self.g1)
        TestCase.assertEqual(self, g3.start_node.get_next_node(master_key=True)[0], self.g1.start_node)
        TestCase.assertTrue(self, self.g1.end_node.get_next_node(master_key=True).__len__() == 2 \
        and  set(self.g1.end_node.get_next_node(master_key=True)) == set([g3.end_node, self.g1.start_node]) )
        logging.critical('Starting up')
    