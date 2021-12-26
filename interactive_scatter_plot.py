import numpy as np
import scipy.stats
import pandas as pd

import matplotlib
import matplotlib.pyplot as pp
import matplotlib.patches as mpatches

from IPython import display
from ipywidgets import interact, widgets

%matplotlib inline

import re
import mailbox
import csv

#read a csv file with the data
df = pd.read_csv('data.csv')

def plotyear(year):
    data = df[df.year == year]
    
    #determine how big will be the dots of the scatter plot and the colour legend
    area = 5e-6 * data.population
    colors = data.region.map({'Africa':'skyblue', 'America':'palegreen','Europe':'gold','Asia':'coral'})
    
    data.plot.scatter('babies_per_woman','age5_surviving',
                     s=area, c=colors,
                     linewidth=1.5, edgecolors='k',
                     figsize=(16,10))
    
    #add a title for the graph
    pp.title(label='Evolution of child mortality rate and number of children per woman over time',
            fontsize=18, pad=20)

    #customise a bit the graph
    pp.grid(linestyle=':', linewidth='0.5')
    pp.axis(ymin=50,ymax=105,xmax=8,xmin=0)
    pp.xlabel('babies per woman')
    pp.ylabel('% childern alive at age of 5')
    
    # build the legend
    Africa = mpatches.Patch(color='skyblue', label='Africa')
    America = mpatches.Patch(color='palegreen', label='America')
    Europe = mpatches.Patch(color='gold', label='Europe')
    Asia = mpatches.Patch(color='coral', label='Asia')

    # set up for handles of the legend declaration
    patches = [Africa,America,Europe,Asia]

    # define and place the legend
    legend = pp.legend(handles=patches,loc='best')
    
#customize the slider fof the year
interact(plotyear, year=widgets.IntSlider(min=1950,max=2015,step=5,value=1965))
