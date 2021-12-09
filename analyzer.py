import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from time import time
import os

if __name__ == '__main__':
    # Read data
    #for file in os.listdir("results"):
    file = "alpha_data"
    df = pd.read_csv('results/' + file + '.csv')
    #greedy = df[df['algorithm'] == 'greedy']
    ##greedy['load'] =  greedy['Gsize'] / greedy['Hsize']
    #greedy = greedy.sort_values(by=['time'])
    #local = df[df['algorithm'] == 'local']
    ##local['load'] =  local['Gsize'] / local['Hsize']
    #local = local.sort_values(by=['time'])
    ## Plot
    df['load'] =  df['Gsize'] / df['Hsize']
    df = df.sort_values(by=['solution'])
    df.plot(x='alpha', y='solution', kind='bar', title='Time vs. Gsize')

    plt.show()
