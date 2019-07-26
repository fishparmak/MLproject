import numpy as np 
import pandas as pd
import random

df = pd.read_csv('input/beauty.csv')
# df.loc[df.loc[:, 'wage']==0,'wage'] = 0.01
df.loc[:, 'exper'] = df.loc[:, 'exper']/3
# df.loc[df.loc[:, 'exper']==0,'exper'] = 0.001
df.loc[df.iloc[:,-1]<3,'looks'] = 0
# df.loc[df.iloc[:,-1]==3,'looks'] = 0
df.loc[(df.iloc[:,-1]==3) & (df.loc[:,'wage']>=7),'looks'] = 1
df.loc[(df.iloc[:,-1]==3) & (df.loc[:,'wage']< 7),'looks'] = 0
df.loc[df.iloc[:,-1]>3,'looks'] = 1
df.to_csv('input/beauty.csv') 
