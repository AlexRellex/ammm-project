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
        self.edges = []
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

    def _is_connected(self, node1, node2, graph):
        """ Is node1 directly connected to node2 """

        return node1 in graph and node2 in graph[node1]

    def _find_best_candidate(self):
        """ Find the best candidate to add to the solution """
        diff0 = 1
        edge = None
        if len(self.solution) == 0:
            min_val = min([len(self._graphH[vertex]) for vertex in self._graphH])
            res = []
            for vertex in list(self._graphH):
                if len(self._graphH[vertex]) == min_val:
                    res.append(vertex)
            vertexh1 = res[0]
            print(f'vertexh1: {vertexh1}')
            for vertexg1 in list(self._graphG):
                print(f'vertexg1: {vertexg1}')
                if len(self._graphH[vertexh1]) <= len(self._graphG[vertexg1]):
                    for vertexh2 in list(self._graphH[vertexh1]):
                        print(f'vertexh2: {vertexh2}')
                        for vertexg2 in list(self._graphG[vertexg1]):
                            print(f'vertexg2: {vertexg2}')
                            if len(self._graphH[vertexh2]) <= len(self._graphG[vertexg2]):
                                diff = abs(self.datAttr.H[vertexh1][vertexh2] - self.datAttr.G[vertexg1][vertexg2])
                                if diff <= diff0:
                                    edge = [vertexh1, vertexh2, vertexg1, vertexg2]
                                    print(f'considered option edge: {edge} with diff: {diff}')
                                    diff0 = diff
                            else:
                                print(f'Vertex {vertexh2} and {vertexg2} have different #edges')
                else:
                    print(f'Vertex {vertexh1} and {vertexg1} have different #edges')
            if edge is not None:
                return edge, diff0
            else:
                return None, None
        else:
            for vertexh1 in list(self.solution):
                #print(f'vertexh1: {vertexh1}')
                for vertexg1 in list(self.solution[vertexh1]):
                    #print(f'vertexg1: {vertexg1}')
                    if (len(self._graphH[vertexh1]) <= len(self._graphG[vertexg1])) and len(self._graphH[vertexh1]) > 0:
                        #print(f'Vertex {vertexh1} and {vertexg1} have the SAME #edges')
                        if ((len(self.solution[vertexh1]) > 0 and vertexg1 in self.solution[vertexh1])) or len(self.solution[vertexh1]) == 0:
                            for vertexh2 in list(self._graphH[vertexh1]):
                                #print(f'vertexh2: {vertexh2}')
                                for vertexg2 in list(self._graphG[vertexg1]):
                                    #print(f'vertexg2: {vertexg2}')
                                    if ((len(self._graphH[vertexh2]) <= len(self._graphG[vertexg2])) and len(self._graphH[vertexh2]) > 0):
                                        #print(f'Vertex {vertexh2} and {vertexg2} have the SAME #edges')
                                        if (len(self.solution[vertexh2]) > 0 and vertexg2 in self.solution[vertexh2]) or len(self.solution[vertexh2]) == 0:
                                            diff = abs(self.datAttr.H[vertexh1][vertexh2] - self.datAttr.G[vertexg1][vertexg2])
                                            if diff <= diff0:
                                                edge = [vertexh1, vertexh2, vertexg1, vertexg2]
                                                print(f'considered option edge: {edge} with diff: {diff}')
                                                diff0 = diff
                                        else:
                                            print(f'Vertex {vertexh2} is already assigned to {self.solution[vertexh2]}')
                                    else:
                                        print(f'Vertex {vertexh2} and {vertexg2} have DIFFERENT #edges')
                        else:
                            print(f'Vertex {vertexh1} is already assigned to {self.solution[vertexh1]}')
                    else:
                        print(f'Vertex {vertexh1} and {vertexg1} have DIFFERENT #edges')
            return edge, diff0

    def solve(self):
        # While solution is not complete
        residual = 0
        while len(self._graphH) > 0:
            # Find the best item to add
            best_item, diff = self._find_best_candidate()
            if best_item is None:
                return None
            # Add the best item to the solution
            self.edges.append(best_item)
            self.solution[best_item[0]].add(best_item[2])   
            self.solution[best_item[1]].add(best_item[3])
            # Remove the item from the items list
            self._remove_edge(best_item[0], best_item[1], self._graphH)
            self._remove_edge(best_item[2], best_item[3], self._graphG)
            print(f'edges: {self.edges}')
            print(f'solution: {self.solution}')
            print(f'graphH: {self._graphH}')
            print(f'graphG: {self._graphG}')
            residual += diff
        return residual
        # Return the solution

if __name__ == "__main__":
    parser = DATParser()
    datAttr = parser.decode("project.9.dat")
    solver = Solver_Greedy(datAttr)
    residual = solver.solve()
    if residual is None:
        print("\n\nSolution is not possible")
        print('INFEASIBLE SOLUTION')
    else:
        print(f'\n\nSolution found: {list(solver.solution.items())}\n')
        print(f'Residual for the solution: {residual}')
