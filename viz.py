# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:22:59 2019

@author: Amin Saqi
"""

import matplotlib.pyplot as plt
import matplotlib.dates as dates
from scipy.stats import norm, percentileofscore
import seaborn as sns
import pandas as pd
import numpy as np

# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

plt.style.use('bmh')

# %% Helper method for rendering histograms.

def plot_histogram (data, nBins=10, xLabel='', yLabel='', title='', test_mean=None):
    """Renders a histogram plot."""
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.05,0.05,0.9,0.9])
    
    #doc for hist:
    #   https://matplotlib.org/3.2.2/api/_as_gen/matplotlib.pyplot.hist.html
    
    n, bins, patches = axes.hist(data, nBins, density=True, facecolor='C0', alpha=0.70)
    
    mean = np.mean(data)
    std = np.std(data)         
    txt = 'Mean: {mean}\nSTD: {std}'.format(mean=round(mean,4), std=round(std,4))   
    if test_mean is not None:
        pth = round(percentileofscore(data, test_mean, kind='mean'))
        txt += '\n\nTest Mean: {}\nPercentile: {}'.format(test_mean, pth)

    axes.text(0.05, 0.9, txt, transform=axes.transAxes)
    
    # doc for clolrs:
    #   https://matplotlib.org/api/_as_gen/matplotlib.pyplot.colors.html
    
    axes.axvline(mean, color='k', linestyle='dashed', linewidth=1)
    axes.axvline(mean + std, color='b', linestyle='dashed', linewidth=1)   
    axes.axvline(mean - std, color='b', linestyle='dashed', linewidth=1)
    axes.axvline(mean + (2 * std), color='g', linestyle='dashed', linewidth=1)
    axes.axvline(mean - (2 * std), color='g', linestyle='dashed', linewidth=1)
    axes.axvline(mean + (3 * std), color='r', linestyle='dashed', linewidth=1)
    axes.axvline(mean - (3 * std), color='r', linestyle='dashed', linewidth=1)
    
    if test_mean is not None:
        axes.axvline(test_mean, color='k', linestyle='solid', linewidth=2)
    
    axes.set_xlabel(xLabel)
    axes.set_ylabel(yLabel)
    axes.set_title(title)
    
    xmin, xmax = plt.xlim()
    sample_x = np.linspace(xmin, xmax, len(data))
    norm_data = norm.pdf(sample_x, mean, std)
    axes.plot(sample_x, norm_data, color='#777777', linewidth=1)    
    
    plt.show()

