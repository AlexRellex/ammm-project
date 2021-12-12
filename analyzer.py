import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from time import time
import os

def plot_bias(df, bias): # bias = K or alpha
    df['load'] =  df['Gsize'] / df['Hsize']  
    files = df['file'].unique()
    for f in files:
        df2 = df.loc[df['file'] == f]
        df2 = df2.sort_values(by=[bias])
        df2.plot(x=bias, y='solution', kind='bar', title= bias + ' vs. solution')
        plt.savefig('graphics/' + bias + '_'+ f + '.png')

def plot_algorithms(df): # bias = K or alpha
    df['load'] =  df['Gsize'] / df['Hsize']  
    files = df['file'].unique()
    for f in files:
        df2 = df.loc[df['file'] == f]
        df2 = df2.sort_values(by=["algorithm"])
        df2.plot(x='algorithm', y='solution', kind='bar', title= 'algorithm vs. solution')
        plt.savefig('graphics/alforithms_' + f + 'solution.png')
    for f in files:
        df2 = df.loc[df['file'] == f]
        df2 = df2.sort_values(by=["algorithm"])
        df2.plot(x='algorithm', y='time', kind='bar', title= 'algorithm vs. time')
        plt.savefig('graphics/alforithms_' + f + 'time.png')

if __name__ == '__main__':
    # Read data
    #for file in os.listdir("results"):
    file = "k_test"
    df = pd.read_csv('results/' + file + '.csv')
    plot_bias(df, "K")
    file = "alpha_test"
    df = pd.read_csv('results/' + file + '.csv')
    plot_bias(df, "alpha")
    file = "all_solvers_test"
    df = pd.read_csv('results/' + file + '.csv')
    plot_algorithms(df)
