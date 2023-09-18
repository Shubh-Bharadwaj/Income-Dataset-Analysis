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
data2=data.dropna(axis=0)

data2.columns

gender=pd.crosstab(index=data2["gender"],columns='count',normalize=True)
print(gender)

# Gender vs Salary Status
gender_salstat=pd.crosstab(index=data2["gender"], 
                           columns=data2["SalStat"],
                           margins=True,
                           normalize='index') #row proportion = 1)
print(gender_salstat)

# Frequency distribution of 'Salary Status'
salstat=sns.countplot(data=data2,x='SalStat')

sns.distplot(data2['age'],bins=10,kde=False)
sns.boxplot(x='SalStat',y='age',data=data2)


