# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 04:57:41 2021

@author: abc
"""

import pandas as pd

df = pd.read_csv('grain_measurements.csv')

df['Area'].plot(kind ='hist',title='Area',bins=50)     #df = dataframe

#####################################################################################

import pandas as pd

data = [[10,200,60],
        [12,155,45],
        [9,50,-45],
        [16,240,90]]

df = pd.DataFrame(data, columns=['Area','Intensity','Orientation'])

print(df)

#######################################################################################

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

print(df.info())
print(df)
print(df.head())
print(df.tail())


df1 = df.set_index('Image')
print(df1.head())
print(df1.columns)



####################################################################################


import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df1 = df.set_index('Image')

print(df['unnamed : 0'].unique())



######################################################################




import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df1 = df.rename(columns = {'unnamed: 0':'Image_set'})
print(df1.columns)
print(df.columns)



########################################################################


import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df1 = (df['Manual'])
print(df1)


#####################################################################

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')
print(df.dtypes)


########################################################################


import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')
print(df.describe())

######################################################################


                  #THANK YOU 
                  #STAY HOME STAY SAFE
                  












