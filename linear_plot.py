#!/usr/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sys

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        df = pd.read_csv(sys.argv[1])
        df.plot(x=0, grid=True)
        plt.style.use('seaborn-whitegrid')
        plt.show()
