
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def add_group_size_to_boxplot(ax, df, groupby_col, value_col):
    # Calculate number of obs per group & maxs to position labels
    nobs = "n:" + df[groupby_col].value_counts().astype(str)
    maxs = df.groupby([groupby_col])[value_col].max()
    xticklabels = [t.get_text()  for t in ax.get_xticklabels()]
    
    # Add it to the plot
    for i,label in enumerate(xticklabels):
        ax.text(i, #x
                maxs.loc[label] + 0.5, #y
                nobs.loc[label], #value (txt)
                horizontalalignment='center',
                size='x-small',
                color='black',
                weight='semibold')

    return ax