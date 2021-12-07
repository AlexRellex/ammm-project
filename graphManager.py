import random, time, pprint
from datParser import *
from collections import defaultdict

class GraphManager:
    def __init__(self, datAttr):
        self.datAttr = datAttr
        self.pretty = pprint.PrettyPrinter()  # for pretty printing
        self._graphG = defaultdict(set)
        self._graphH = defaultdict(set)
        self._create_graph(datAttr.G, self._graphG)   
        self._create_graph(datAttr.H, self._graphH)      
        # Initialize the solution
        self.edges = []
        self.used_edges = []
        self.used_diffs = []
        self.solution = defaultdict(set)
    def _create_graph(self, connections, graph):
        """ Add connections (adjacence matrix) to graph """
        for i in range(len(connections)):
            for j in range(len(connections[i])):
                if connections[i][j] > 0:
                    self._add(i, j, graph)
        print("Graph created: ")
        self.pretty.pprint(graph)
        #print(f'graph created: {graph}')

    @staticmethod
    def _add(node1, node2, graph):
        """ Add connection between node1 and node2 """
        graph[node1].add(node2)
        graph[node2].add(node1)

    @staticmethod
    def _remove_edge(node1, node2, graph):
        """ Remove all references to node """
        graph[node1].remove(node2)
        graph[node2].remove(node1)
        for node in list(graph):
            if len(graph[node]) == 0:
                del graph[node] 