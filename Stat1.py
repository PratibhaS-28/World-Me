from fileinput import filename
import numpy as np
import pickle as pc
import pandas as pd

filename = "load.csv"   # to open file
cols=None
data=[]
with open (filename) as f:
    for line in f.readlines():
        vals= line.replace("\n","").split(",")
        print(vals)
        if cols is None:
            cols=vals
        else:
            data.append([float(x) for x in vals])
    d0=pd.DataFrame(data,columns=cols)
    print(d0.dtypes)
    d0.head()
    print(d0)




    d1= np.loadtxt(filename,skiprows=1,delimiter=",")
    print(d1.dtype)
    print(d1[:5,:])
    d3=pd.read_csv(filename)
    print(d3.dtypes)
    print(d3)


        

