
class GraphInstance:
    def __init__(self, min_vertex, max_vertex, min_edge, max_edge):
        self.__min_vertex = min_vertex
        self.__max_vertex = max_vertex
        self.__min_edge = min_edge
        self.__max_edge = max_edge
        self.__vertex = []
        self.__edge = []
    
    @property
    def min_vertex(self):
        return self.__min_vertex

    @min_vertex.setter
    def min_vertex(self, value):
        self.__min_vertex = value
    
    @property
    def max_vertex(self):
        return self.__max_vertex

    @max_vertex.setter
    def max_vertex(self, value):
        self.__max_vertex = value

    @property
    def min_edge(self):
        return self.__min_edge
    
    @min_edge.setter
    def min_edge(self, value):
        self.__min_edge = value
    
    @property
    def max_edge(self):
        return self.__max_edge
    
    @max_edge.setter
    def max_edge(self, value):
        self.__max_edge = value    

    @property
    def vertex(self):
        return self.__vertex
    
    @vertex.setter
    def vertex(self, value):
        self.__vertex = value
    
    @property
    def edge(self):
        return self.__edge

    @edge.setter
    def edge(self, value):
        self.__edge = value
