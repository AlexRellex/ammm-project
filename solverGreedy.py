import random, time
from datParser import *


class Solver_Greedy():
    def __init__(self, datAttr):
        self.datAttr = datAttr
        self.sonsG = {}
        self.sonsH = {}

    def matrix_to_dict(matrix):
        # Convert the matrix to a dictionary
        #   Keys are the items
        #   Values are the items' weights
        # Return the dictionary
        for m, i in matrix, len(matrix):
            if m[i] > 0:
                self.sonsH



    def _quality():
        pass
    
    def solve(self):
        # Initialize the solution
        solution = []
        # While solution is not complete
        while len(solution) < self.datAttr.M:
            # Find the best item to add
            best_item = self.datAttr.items[0]
            for item in self.datAttr.items:
                if item.weight < best_item.weight:
                    best_item = item
            # Add the best item to the solution
            solution.append(best_item)
            # Remove the item from the items list
            self.datAttr.items.remove(best_item)
        #   Find the best candidate
        #   Add it to the solution
        #   Remove it from the candidate list
        # Return the solution