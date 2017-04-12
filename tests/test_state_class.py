from .context import src
import src.state_class as state_class
from src.graph_builder import node
from unittest import TestCase
import logging

class test_state(TestCase):
    def test_gen_state(self):
        n1 = node()
        n2 = node()
        self.assertEqual(state_class.create_new_state([n1,n2]), state_class.create_new_state([n1,n2]))
        self.assertNotEqual(state_class.create_new_state([n1]), state_class.create_new_state([n2]))
        self.assertIn(state_class.create_new_state([n1]), state_class.all_states)
