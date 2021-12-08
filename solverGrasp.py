from graphManager import *
import random

class SolverGrasp(GraphManager):
    def __init__(self, datAttr, alpha):
        super().__init__(datAttr)       
        self.alpha = alpha

    def _find_best_candidate(self):
        """ Find the best candidate to add to the solution """
        diffs = []
        edges = []

        if len(self.solution) == 0:
            min_val = min([len(self._graphH[vertex]) for vertex in self._graphH])
            res = []
            for vertex in list(self._graphH):
                if len(self._graphH[vertex]) == min_val:
                    res.append(vertex)
            vertexh1 = res[0]
            #print(f'vertexh1: {vertexh1}')
            for vertexg1 in list(self._graphG):
                #print(f'vertexg1: {vertexg1}')
                if len(self._graphH[vertexh1]) <= len(self._graphG[vertexg1]):
                    for vertexh2 in list(self._graphH[vertexh1]):
                        #print(f'vertexh2: {vertexh2}')
                        for vertexg2 in list(self._graphG[vertexg1]):
                            #print(f'vertexg2: {vertexg2}')
                            if len(self._graphH[vertexh2]) <= len(self._graphG[vertexg2]):
                                diffs.append(abs(self.datAttr.H[vertexh1][vertexh2] - self.datAttr.G[vertexg1][vertexg2]))
                                edges.append([vertexh1, vertexh2, vertexg1, vertexg2])
                                print(f'added option edge: {edges[-1]} with diff: {diffs[-1]}')
                            else:
                                print(f'Vertex {vertexh2} and {vertexg2} have different #edges')
                else:
                    print(f'Vertex {vertexh1} and {vertexg1} have different #edges')
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
                                            diffs.append(abs(self.datAttr.H[vertexh1][vertexh2] - self.datAttr.G[vertexg1][vertexg2]))
                                            edges.append([vertexh1, vertexh2, vertexg1, vertexg2])
                                            print(f'added option edge: {edges[-1]} with diff: {diffs[-1]}')
                                        else:
                                            print(f'Vertex {vertexh2} is already assigned to {self.solution[vertexh2]}')
                                    else:
                                        print(f'Vertex {vertexh2} and {vertexg2} have DIFFERENT #edges')
                        else:
                            print(f'Vertex {vertexh1} is already assigned to {self.solution[vertexh1]}')
                    else:
                        print(f'Vertex {vertexh1} and {vertexg1} have DIFFERENT #edges')

        if len(edges) == 0:
            return None, None
        elif len(edges) == 1:
            return edges[0], diffs[0]
        RCL = min(diffs) + self.alpha * (max(diffs) - min(diffs))
        for diff, edge in zip(diffs, edges):
            if diff >= RCL:
                edges.remove(edge)
                diffs.remove(diff)
        if len(edges) == 0:
            return None, None
        edge = random.choice(edges)
        diff = diffs[edges.index(edge)]
        return edge, diff

    def _find_different_candidate(self):
        """ Find the best candidate to add to the solution """
        diffs = []
        edges = []

        if len(self.solution) == 0:
            min_val = min([len(self._graphH[vertex]) for vertex in self._graphH])
            res = []
            for vertex in list(self._graphH):
                if len(self._graphH[vertex]) == min_val:
                    res.append(vertex)
            vertexh1 = res[0]
            #print(f'vertexh1: {vertexh1}')
            for vertexg1 in list(self._graphG):
                #print(f'vertexg1: {vertexg1}')
                if len(self._graphH[vertexh1]) <= len(self._graphG[vertexg1]):
                    for vertexh2 in list(self._graphH[vertexh1]):
                        #print(f'vertexh2: {vertexh2}')
                        for vertexg2 in list(self._graphG[vertexg1]):
                            #print(f'vertexg2: {vertexg2}')
                            if len(self._graphH[vertexh2]) <= len(self._graphG[vertexg2]):
                                diffs.append(abs(self.datAttr.H[vertexh1][vertexh2] - self.datAttr.G[vertexg1][vertexg2]))
                                if [vertexh1, vertexh2, vertexg1, vertexg2] not in self.used_edges:
                                    edges.append([vertexh1, vertexh2, vertexg1, vertexg2])
                                    print(f'added option edge: {edges[-1]} with diff: {diffs[-1]}')
                            else:
                                print(f'Vertex {vertexh2} and {vertexg2} have different #edges')
                else:
                    print(f'Vertex {vertexh1} and {vertexg1} have different #edges')
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
                                            diffs.append(abs(self.datAttr.H[vertexh1][vertexh2] - self.datAttr.G[vertexg1][vertexg2]))
                                            if [vertexh1, vertexh2, vertexg1, vertexg2] not in self.used_edges:
                                                edges.append([vertexh1, vertexh2, vertexg1, vertexg2])
                                                print(f'added option edge: {edges[-1]} with diff: {diffs[-1]}')
                                        else:
                                            print(f'Vertex {vertexh2} is already assigned to {self.solution[vertexh2]}')
                                    else:
                                        print(f'Vertex {vertexh2} and {vertexg2} have DIFFERENT #edges')
                        else:
                            print(f'Vertex {vertexh1} is already assigned to {self.solution[vertexh1]}')
                    else:
                        print(f'Vertex {vertexh1} and {vertexg1} have DIFFERENT #edges')

        if len(edges) == 0:
            return None, None
        elif len(edges) == 1:
            return edges[0], diffs[0]
        RCL = min(diffs) + self.alpha * (max(diffs) - min(diffs))
        for diff, edge in zip(diffs, edges):
            if diff >= RCL:
                edges.remove(edge)
                diffs.remove(diff)
        if len(edges) == 0:
            return None, None
        edge = random.choice(edges)
        diff = diffs[edges.index(edge)]
        return edge, diff

    def solve(self):
        # While solution is not complete
        residual = 0
        best_item = None
        backtrack = 0
        while len(self._graphH) > 0:
            # Find the best item to add
            if best_item is None and backtrack > 0:
                print('Looking for a different solution')
                best_item, diff = self._find_different_candidate()
                if best_item is not None:
                    backtrack -= 1
            else:
                best_item, diff = self._find_best_candidate()
            if best_item is None:
                backtrack += 1
                try:
                    for track in range(backtrack):
                        self._add(self.edges[-1][0], self.edges[-1][1], self._graphH)
                        self._add(self.edges[-1][2], self.edges[-1][3], self._graphG)
                        self.used_edges.append(self.edges.pop())
                        self.solution.popitem()          
                    for track in range(backtrack - 1):
                        print(f'used diffs {self.used_diffs}')
                        residual -= self.used_diffs.pop()
                except:
                    return None
            else:
            # Add the best item to the solution
                self.edges.append(best_item)
                self.used_diffs.append(diff)
                self.solution[best_item[0]].add(best_item[2])   
                self.solution[best_item[1]].add(best_item[3])
                # Remove the item from the items list
                self._remove_edge(best_item[0], best_item[1], self._graphH)
                self._remove_edge(best_item[2], best_item[3], self._graphG)
                residual += diff
                print(f'edges: {self.edges}')
                print(f'solution: {self.solution}')
                print(f'graphH: {self._graphH}')
                print(f'graphG: {self._graphG}')
                
        return residual
        # Return the solution

if __name__ == "__main__":
    parser = DATParser()
    datAttr = parser.decode("project.9.dat")
    solver = SolverGrasp(datAttr, alpha=0.5)
    residual = solver.solve()
    if residual is None:
        print("\n\nSolution is not possible")
        print('INFEASIBLE SOLUTION')
    else:
        print(f'\n\nSolution found: {list(solver.solution.items())}\n')
        print(f'Residual for the solution: {residual}')
