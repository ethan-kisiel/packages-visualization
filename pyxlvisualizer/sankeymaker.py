from .color import Color

class Graph:
    '''
    '''
    
    def __init__(self):
        pass
    
    def __repr__(self):
        print("Not yet implimented.")
        

class Node:
    '''
    Takes a list of Links and a Color
    '''
    
    def __init__(self, label, color: Color, links=None):
        if links is not None:
            self.links = links
        
        self.label = label
        self.color = color

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

    def get_links(self):
        '''
        Takes self, returns self.links
        '''
        return self.links

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
    def __init__(self,):
        pass
    
    def __repr__(self):
        '''
        '''
    