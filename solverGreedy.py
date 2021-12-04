import random, time, pprint
from datParser import *
from collections import defaultdict


class Solver_Greedy():
    def __init__(self, datAttr):
        self.datAttr = datAttr
        self.pretty = pprint.PrettyPrinter()  # for pretty printing
        self._graphG = defaultdict(set)
        self._graphH = defaultdict(set)
        self._create_graph(datAttr.G, self._graphG)   
        self._create_graph(datAttr.H, self._graphH)      
        # Initialize the solution
        self.solution = []
        
    
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
    def _remove(node, graph):
        """ Remove all references to node """
        for n, cxns in graph.items():  # python3: items(); python2: iteritems()
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del graph[node]
        except KeyError:
            pass

    def _is_connected(self, node1, node2, graph):
        """ Is node1 directly connected to node2 """

        return node1 in graph and node2 in graph[node1]


    def _find_best_candidate(self):
        """ Find the best candidate to add to the solution """
        diff0 = 1
        if len(self.solution) == 0:
            min_val = min([len(self._graphH[vertex]) for vertex in self._graphH])
            res = []
            for vertex in self._graphH:
                if len(self._graphH[vertex]) == min_val:
                    res.append(vertex)
            vertexh1 = res[0]
            print(f'candidate: {vertexh1}')

            for vertexg1 in self._graphG:
                if len(self._graphH[vertexh1]) == len(self._graphG[vertexg1]):
                    for vertexh2 in self._graphH[vertexh1]:
                        for vertexg2 in self._graphG[vertexg1]:
                            if len(self._graphH[vertexh2]) == len(self._graphG[vertexg2]):
                                diff = abs(self.datAttr.H[vertexh1][vertexh2] - self.datAttr.G[vertexg1][vertexg2])
                                if diff <= diff0:
                                    edge = [vertexh1, vertexh2, vertexg1, vertexg2]
                                diff0 = diff
            return edge
        else:
            for vertexh1 in self._graphH:
                for vertexg1 in self._graphG:
                    if len(self._graphH[vertexh1]) == len(self._graphG[vertexg1]):
                        for vertexh2 in self._graphH[vertexh1]:
                            for vertexg2 in self._graphG[vertexg1]:
                                if len(self._graphH[vertexh2]) == len(self._graphG[vertexg2]):
                                    diff = abs(self.datAttr.H[vertexh1][vertexh2] - self.datAttr.G[vertexg1][vertexg2])
                                    if diff <= diff0:
                                        edge = [vertexh1, vertexh2, vertexg1, vertexg2]
                                    diff0 = diff
            return edge

    def solve(self):
        # While solution is not complete
        while len(self._graphH) > 0:
            # Find the best item to add
            best_item = self._find_best_candidate()
            print(f'best item: {best_item}')
            # Add the best item to the solution
            self.solution.append(best_item)    
            # Remove the item from the items list
            self._remove(best_item[0], self._graphH)
            self._remove(best_item[1], self._graphH)
            self._remove(best_item[2], self._graphG)
            self._remove(best_item[3], self._graphG)
            self.pretty.pprint(self._graphH)    
            self.pretty.pprint(self._graphG)   
        # Return the solution

if __name__ == "__main__":
    parser = DATParser()
    datAttr = parser.decode("project.1.dat")
    solver = Solver_Greedy(datAttr)
    solver.solve()
