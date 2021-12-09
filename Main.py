import sys, os, time, csv
from datParser import DATParser
from ValidateConfig import ValidateConfig
from InstanceGenerator import InstanceGenerator
from AMMMGlobals import AMMMException
from solverGreedy import Solver_Greedy
from localSearch import SolverLocalSearch
from solverGrasp import SolverGrasp

class AMMMproject:
    def __init__(self, configFile):
        try:
            print("Reading Config file %s" % configFile)
            self.parser = DATParser()
            self.config = self.parser.parse(configFile)
            print("Config file parsed")
            ValidateConfig.validate(self.config)
            print("Creating Instances")
            self.insGen = InstanceGenerator(self.config)
            status = self.insGen.generate()
            if status:
                raise AMMMException("Could not generate instances, not feasible instances found")
        except AMMMException as e:
            print("Exception: %s", e)
            sys.exit(1)
        self.K = []
        for i in range(self.config.max_sv):
            self.K.append(i)
        self.alpha = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        self.create_csv_header(["file", "algorithm", "solution", "time","Gsize", "Hsize"], "all_solvers_test")
        self.create_csv_header(["file", "algorithm", "solution", "time","Gsize", "Hsize"], "all_solvers_data")
        self.create_csv_header(["file", "alpha", "solution", "time","Gsize", "Hsize"], "alpha_test")
        self.create_csv_header(["file", "alpha", "solution", "time","Gsize", "Hsize"], "alpha_data")
        self.create_csv_header(["file", "K", "solution", "time","Gsize", "Hsize"], "K_test")
        self.create_csv_header(["file", "K", "solution", "time","Gsize", "Hsize"], "K_data")

    @staticmethod
    def create_csv_header(header, filename):
        try:
            os.remove("results/" + filename + ".csv")
        except OSError:
            pass
        with open("results/" + filename + ".csv", 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)

    @staticmethod
    def run_all_solvers(file, datAttr, K, alpha, testname):
        print("Running Solvers for file %s" % file)
        print(f"Graph G: {datAttr.G}")
        print(f"Graph H: {datAttr.H}")
        greedy = Solver_Greedy(datAttr)
        local = SolverLocalSearch(datAttr, K)
        grasp = SolverGrasp(datAttr, alpha)
        with open("results/" + testname + ".csv", 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            time0 = time.time()
            greedy_solution = greedy.solve()
            solve_time = time.time() - time0
            writer.writerow([file, "greedy", greedy_solution, solve_time, datAttr.n, datAttr.m])
            time0 = time.time()
            local_solution = local.solve()
            solve_time = time.time() - time0
            writer.writerow([file, "local", local_solution, solve_time, datAttr.n, datAttr.m])
            time0 = time.time()
            grasp_solution = grasp.solve()
            solve_time = time.time() - time0
            writer.writerow([file, "grasp", grasp_solution, solve_time, datAttr.n, datAttr.m])
    
    def run_tests(self):
        K = 4
        alpha = 0.5
        for file in os.listdir("testfiles"):
            if file.endswith(".dat"):
                datAttr = self.parser.decode("testfiles/" + file)
                self.run_all_solvers("testfiles/" + file, datAttr, K, alpha, "all_solvers_test")
        for file in os.listdir("datafiles"):
            if file.endswith(".dat"):
                datAttr = self.parser.decode("datafiles/" + file)
                self.run_all_solvers("datafiles/" + file, datAttr, K, alpha, "all_solvers_data")

    def run_K_tests(self):
        for k in self.K:
            for file in os.listdir("testfiles"):
                if file.endswith(".dat"):
                    datAttr = self.parser.decode("testfiles/" + file)
                    print("Running Solvers for file %s" % file)
                    print(f"Graph G: {datAttr.G}")
                    print(f"Graph H: {datAttr.H}")
                    local = SolverLocalSearch(datAttr, k)
                    with open("results/K_test.csv", 'a', encoding='UTF8', newline='') as f:
                        writer = csv.writer(f)
                        time0 = time.time()
                        local_solution = local.solve()
                        solve_time = time.time() - time0
                        writer.writerow([file, k, local_solution, solve_time, datAttr.n, datAttr.m])

            for file in os.listdir("datafiles"):
                if file.endswith(".dat"):
                    datAttr = self.parser.decode("datafiles/" + file)
                    print("Running Solvers for file %s" % file)
                    print(f"Graph G: {datAttr.G}")
                    print(f"Graph H: {datAttr.H}")
                    local = SolverLocalSearch(datAttr, k)
                    with open("results/K_data.csv", 'a', encoding='UTF8', newline='') as f:
                        writer = csv.writer(f)
                        time0 = time.time()
                        local_solution = local.solve()
                        solve_time = time.time() - time0
                        writer.writerow([file, k, local_solution, solve_time, datAttr.n, datAttr.m])
    
    def run_alpha_tests(self):
        for alpha in self.alpha:
            for file in os.listdir("testfiles"):
                if file.endswith(".dat"):
                    datAttr = self.parser.decode("testfiles/" + file)
                    print("Running Solvers for file %s" % file)
                    print(f"Graph G: {datAttr.G}")
                    print(f"Graph H: {datAttr.H}")
                    grasp = SolverGrasp(datAttr, alpha)
                    with open("results/alpha_test.csv", 'a', encoding='UTF8', newline='') as f:
                        writer = csv.writer(f)
                        time0 = time.time()
                        grasp_solution = grasp.solve()
                        solve_time = time.time() - time0
                        writer.writerow([file, alpha, grasp_solution, solve_time, datAttr.n, datAttr.m])
            for file in os.listdir("datafiles"):
                if file.endswith(".dat"):
                    datAttr = self.parser.decode("datafiles/" + file)
                    print("Running Solvers for file %s" % file)
                    print(f"Graph G: {datAttr.G}")
                    print(f"Graph H: {datAttr.H}")
                    grasp = SolverGrasp(datAttr, alpha)
                    with open("results/alpha_data.csv", 'a', encoding='UTF8', newline='') as f:
                        writer = csv.writer(f)
                        time0 = time.time()
                        grasp_solution = grasp.solve()
                        solve_time = time.time() - time0
                        writer.writerow([file, alpha, grasp_solution, solve_time, datAttr.n, datAttr.m])

    def run(self):
        self.run_K_tests()
        self.run_alpha_tests()
        self.run_tests()

if __name__ == '__main__':
    main = AMMMproject("configfiles/config.dat")
    sys.exit(main.run())
