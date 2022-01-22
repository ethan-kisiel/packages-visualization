import pytest
from ..color import Color
from ..sankeymaker import Node


node_color = Color([255, 0, 100, 1])
test_node = Node('E', node_color)

def test_node_inf():
    assert test_node.label == 'E'
