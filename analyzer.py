import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from time import time
import os

if __name__ == '__main__':
    # Read data
    #for file in os.listdir("results"):
    file = "all_solvers_test"
    df = pd.read_csv('results/' + file + '.csv')
    greedy = df[df['algorithm'] == 'greedy']
    #greedy['load'] =  greedy['Gsize'] / greedy['Hsize']
    greedy = greedy.sort_values(by=['time'])
    local = df[df['algorithm'] == 'local']
    #local['load'] =  local['Gsize'] / local['Hsize']
    local = local.sort_values(by=['time'])
    # Plot
    ax = plt.subplot()
    ax.bar(greedy['Gsize'], greedy['time'], width=0.5, color='b', align='center')
    ax.bar(local['Gsize'], local['time'], width=0.5, color='g', align='center')

    plt.show()
