import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff

def grf (arg):
    list = np.array(arg)
    df = pd.DataFrame(list)
    #print(df)
    fig1 = px.scatter(df,x = 0,y = 1)
    fig2 = px.density_heatmap(df,0,1)
    fig1.show()
    fig2.show()
    #fig2 = px.scatter(x:arg1,y:arg2) #df = DataFrame
    #fig1.show()
   # fig2.show()
    return()
