import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split #To partition the data
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
data_income=pd.read_csv('C:\\D Drive\\Projects_Python\\NPTEL\\income.csv')
data=data_income.copy()
print(data.info())
print('Data columns with null values:\n',data.isnull().sum())
#Summary of numerical variables
summary_num=data.describe()
print(summary_num)
#Summary of categorical variables
summary_cate=data.describe(include ='O')
print(summary_cate)
data['JobType'].value_counts()
data['occupation'].value_counts()
print(np.unique(data['JobType']))
data=pd.read_csv('C:\\D Drive\\Projects_Python\\NPTEL\\income.csv',na_values=[" ?"])
data.isnull().sum()
missing=data[data.isnull().any(axis=1)]
#wherever job type is missing occupation is also missing
#also when job type is never worked
"""
Missing values in Jobtype = 1809
Missing values in Occupation = 1816
1816-1809= 7 never worked category
"""