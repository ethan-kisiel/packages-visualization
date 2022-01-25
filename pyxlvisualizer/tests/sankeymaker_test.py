import pytest
from ..color import Color
from ..sankeymaker import Link, Node, Graph

source_color = Color([255, 0, 100, 1.0])
target_color = Color([255, 100, 0, 1.0])
link_color = Color([255, 50, 50, 0.5])
source_node = Node('Source', source_color)
target_node = Node('Target', target_color)
test_link = Link(source_node, target_node, link_color)

test_graph = Graph([test_link], [source_node, target_node])
#print(label for label in test_graph.get_labels)

def test_labels():
    print(test_graph.get_labels())
    assert test_graph.get_labels() == ['Source', 'Target']
    
def test_source_values():
    print(test_graph.get_sources())
          
def test_target_values():
    print(test_graph.get_targets())