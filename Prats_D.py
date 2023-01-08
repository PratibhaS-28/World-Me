from turtle import pd
import numpy as np
import pandas as pd
from statistics import *

df = pd.read_csv('Diabetes.csv')
print(df.head().to_string())
print(df.tail().to_string())
print(df.info())
print(df['Glucose'].mean())
print(df['Glucose'].max())
print(df['Glucose'].min())
print(df.filter("Outcome"))
print(df['Outcome'].head(50)) 
print(df['Outcome']) 








