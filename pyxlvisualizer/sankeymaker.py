from .color import Color

class Graph:
    '''
    '''
    
    def __init__(self, links, nodes):
        '''
        '''
        self.links = links
        self.nodes = nodes
        
    def add_node(self, node, index=None):
        '''
        Takes self, Node node, optional int index
        '''
        if index is None:
            self.nodes.append(node)
        else:
            self.nodes.insert(index, node)

    def set_nodes(self, nodes):
        '''
        '''
        self.nodes = nodes

    def add_link(self, link, index=None):
        '''
        Takes single Link type variable and optional index
        Appends link to self.links OR inserts link at index
        '''
        if index is None:
            self.links.append(link)
        else:
            self.links.insert(index, link)

    def set_links(self, links):
        '''
        Takes a list of Link type variables
        Sets self.links to links
        '''
        self.links = links
    
    def get_labels(self):
        '''
        '''
        return ([node.label for node in self.nodes])

    def get_sources(self):
        '''
        Returns self.nodes array location of self.links source nodes
        '''
        #return ([self.nodes.index(link.source_node) for link in self.links])
        return ([self.nodes.index(link.source_node) for link in self.links])
    def get_targets(self):
        '''
        Returns self.nodes array location of self.links target nodes
        '''
        return ([self.nodes.index(link.target_node) for link in self.links])
    
    def __repr__(self):
        print("Not yet implimented.")

class Node:
    '''
    Takes a list of Links and a Color
    '''
    
    def __init__(self, label, color: Color):      
        self.label = label
        self.color = color

    def set_color(self, color):
        '''
        Takes Color object
        (overwrites current self.color)
        '''
        self.color = color

    def __repr__(self):
        return f'Label: {self.label}, Color: {self.color.getrgba}, Number of Connections: {len(self.get_links())}'


# Link class (flow stream)
class Link:
    '''
    '''
    def __init__(self, source_node : Node, target_node: Node, color: Color):
        self.source_node = source_node
        self.target_node = target_node
        self.color = color
        self.size = 0

    def set_size(self, size):
        self.size = size

    def __repr__(self):
        '''
        '''
        return f'Source: {self.source_node.label}, Target: {self.target_node.label}, Size: {self.size}, Color: {self.color}'
    