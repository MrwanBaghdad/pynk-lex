
from .context import src #pylint: disable=E
import src.graph_mani as graph_mani #pylint: disable=E
import src.graph_builder as graph_builder #pylint: disable=E
import src.helpers as helpers #pylint: disable=E
import unittest


class TestingGraph(unittest.TestCase):
    def test_create_node(self):
        n1 = graph_builder.node()
        n2 = graph_builder.node()
    def test_create_graph(self):
        n1 = graph_builder.node()
        n2 = graph_builder.node()
        n3 = graph_builder.node()
        n2.add_next_node(helpers.accpeting_func_elipson(n3))
        n1.add_next_node(helpers.accpeting_func_elipson(n2))
        g1 = graph_builder.graph(n1)
        unittest.TestCase.assertEqual(self, n3, g1.end_node)
        unittest.TestCase.assertTrue(self, n3 in n2.get_next_node(master_key=True))
    def test_graph_create_recursion(self):
        n1 = graph_builder.node()
        n2 = graph_builder.node()
        n3 = graph_builder.node()
        n4 = graph_builder.node()
        n1.add_next_node(helpers.accpeting_func_elipson(n2))
        n2.add_next_node(helpers.accpeting_func_elipson(n3))
        n3.add_next_node(helpers.accpeting_func_elipson(n4))
        n3
        n3.add_next_node(helpers.accpeting_func_elipson(n2)
        )
        g1 = graph_builder.graph(n1)
        n1.add_next_node(helpers.accpeting_func_elipson(n4))
        unittest.TestCase.assertTrue(self, g1.end_node, n4)
    def test_accepting_func(self):
        n1 = graph_builder.node()
        n2 = graph_builder.node()
        n11 = graph_builder.node()
        n12 = graph_builder.node()
        n13 = graph_builder.node()

        n22 = graph_builder.node()

        n1.add_next_node(helpers.accepting_func_range(n11,'a','e'))
        n1.add_next_node(helpers.accepting_func_char(n12,'d'))
        n1.add_next_node(helpers.accpeting_func_elipson(n13))

        unittest.TestCase.assertIn(self, n12, n1.get_next_node('d'))
        unittest.TestCase.assertIn(self, n11, n1.get_next_node('d'))

        withA = n1.get_next_node('a')

        unittest.TestCase.assertIn(self,n11, withA)
        unittest.TestCase.assertIn(self, n13, withA)
        unittest.TestCase.assertNotIn(self, n12, withA)


