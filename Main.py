from re import A
import sys, os
from datParser import DATParser
from ValidateConfig import ValidateConfig
from InstanceGenerator import InstanceGenerator
from AMMMGlobals import AMMMException
from solverGreedy import Solver_Greedy
from localSearch import SolverLocalSearch
from solverGrasp import SolverGrasp


def run():
    try:
        configFile = "configfiles/config.dat"
        print("Reading Config file %s" % configFile)
        parser = DATParser()
        config = parser.parse(configFile)
        print("Config file parsed")
        ValidateConfig.validate(config)
        print("Creating Instances")
        insGen = InstanceGenerator(config)
        status = insGen.generate()
        if status:
            raise AMMMException("Could not generate instances, not feasible instances found")

        K = 4
        alpha = 0.5
        for file in os.listdir("datafiles"):
            if file.endswith(".dat"):
                datAttr = parser.decode("datafiles/" + file)
                print("Running Solvers for file %s" % file)
                print(f"Graph G: {datAttr.G}")
                print(f"Graph H: {datAttr.H}")
                greedy = Solver_Greedy(datAttr)
                local = SolverLocalSearch(datAttr, K)
                grasp = SolverGrasp(datAttr, alpha)
                greedy.solve()
                local.solve()
                grasp.solve()

    except AMMMException as e:
        print("Exception: %s", e)
        return 1

if __name__ == '__main__':
    sys.exit(run())
