import itertools
import pprint
import random
import sys
from graphInstance import GraphInstance

class InstanceGenerator(object):
    # Generate instances based on read configuration.

    def __init__(self, config):
        self.image = GraphInstance(config.min_iv, config.max_iv, config.min_ie, config.max_ie)
        self.shape = GraphInstance(config.min_sv, config.max_sv, config.min_se, config.max_se)

    def generate(self): 
        # generate all combinations of values from all for ranges
        combinations = list(
            itertools.product(*[
                [i for i in range(self.image.min_vertex, self.image.max_vertex + 1)], 
                [i for i in range(self.image.min_edge, self.image.max_edge + 1)], 
                [i for i in range(self.shape.min_vertex, self.shape.max_vertex + 1)], 
                [i for i in range(self.shape.min_edge, self.shape.max_edge + 1)],
                ]))
        # generate image-shape pairs that satisfy graph and image-shape conditions
        pairs = []
        for i in combinations:
            IV = i[0]
            IE = i[1]
            SV = i[2]
            SE = i[3]
            # shape must have as many or less vertices as image
            if IV < SV:
                pass

            # you can't have more edges than n*(n-1)/2 such that n corresponds to the
            # number of vertices of an acyclic, undirected graph
            elif (
                IE > (IV * (IV - 1)) / 2
                or SE > (SV * (SV - 1)) / 2
            ):
                pass

            # you can't have less edges than n-1 such that n corresponds to number of
            # vertices of an acyclic, undirected graph
            elif (
                IE < IV - 1
                or SE < SV - 1
            ):
                pass

            # all good with combination, one last thing though...
            else:
                # if shape and image have same number of vertices, shape can't have more 
                # edges than image
                if IV == SV:
                    if SE <= IE:
                        pairs.append(i)
                    else:
                        pass
                else:
                    pairs.append(i)

        if pairs == []:
            print(
                "no feasible combinations found"
            )
            return 1
        else:
            for pair in pairs:
                self._generate_pair(pair[0], pair[1], pair[2], pair[3])

    def _generate_pair(self, IV, IE, SV, SE):
        image_str = self._generate_matrix(IV, IE)
        shape_str = self._generate_matrix(SV, SE)
        image_dims = f"{IV}_{IE}"
        shape_dims = f"{SV}_{SE}"
        print(
            f'writing into file "datafiles/config-{image_dims}-{shape_dims}.dat"'
        )
        with open(f"datafiles/config-{image_dims}-{shape_dims}.dat", "w") as file:
            file.write(
                f"n = {IV};\n"
                f"m = {SV};\n\n"
                "G = \n"
                f"{image_str};\n\n"
                "H = \n"
                f"{shape_str};\n"
            )

    def _generate_matrix(self, vertex, edges):

        size_matrix_triangle = int((vertex * (vertex - 1)) / 2)
        matrix_triangle = [0.0 for _ in range(size_matrix_triangle)]

        # populate upper/lower-triangle elements with values 0.0-1.0 for as many edges as
        # specified and remove that choice from index values to select from
        index_values = [i for i in range(size_matrix_triangle)]
        for i in range(edges):
            random_index_value = random.choice(index_values)
            matrix_triangle[random_index_value] = random.randint(1, 10) / 10
            index_values.remove(random_index_value)
        # generate (i, j) index pairs for upper triangle of matrix
        triangle_index = []
        head = 1
        for i in range(vertex):
            for j in range(head, vertex):
                triangle_index.append((i, j))
            head += 1

        matrix = [[0.0 for _ in range(vertex)] for _ in range(vertex)]

        # populate matrix's upper/lower triangles
        for element_indices in zip(matrix_triangle, triangle_index):
            # (i, j) of upper triangle
            i = element_indices[1][0]
            j = element_indices[1][1]
            matrix[i][j] = element_indices[0]
            # switch places of i and j
            matrix[j][i] = element_indices[0]

        matrix_str = pprint.pformat(
            matrix,
            width=len(str(matrix[0])) + 2
        ).replace(",", " ")

        return matrix_str

