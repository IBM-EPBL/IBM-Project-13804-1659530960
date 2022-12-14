# -*- coding: utf-8 -*-
"""Assignment2_Premikkha.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zDUJEq7p7-opoM_CvqKVYnzjHLHYj3tY
"""

import pandas as pd

"""Load the dataset."""

from google.colab import files
uploaded = files.upload()
df = pd.read_csv('Churn_Modelling.csv')

df.head(5)

"""Univariate Analysis"""

import matplotlib.pyplot as plt

df.boxplot(column=['CreditScore'], grid=False, color='black')

import matplotlib.pyplot as plt

df.hist(column='CreditScore', grid=False, edgecolor='black')

import seaborn as sns

sns.kdeplot(df['EstimatedSalary'])

"""Multivariate Analysis"""

pd.plotting.scatter_matrix(df.loc[:, "CreditScore":"EstimatedSalary"], diagonal="kde",figsize=(20,15))
plt.show()

ax = df[["CreditScore","Age","Tenure","Balance","HasCrCard","IsActiveMember","EstimatedSalary"]].plot(figsize=(20,15))
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5));

"""Bivariate Analysis"""

plt.scatter(df.Tenure, df.Age)

""" Perform descriptive statistics on the dataset"""

average = df['CreditScore'].mean()
print(average)

average1 = df['Balance'].mean()
print(average1)

med = df['CreditScore'].median()
print(med)

med1 = df['Balance'].median()
print(med1)

standard_deviation = df['CreditScore'].std()
print(standard_deviation)

standard_deviation = df['Balance'].std()
print(standard_deviation)

"""Handle the Missing values.

"""

df.isnull()

df.notnull()

df.fillna(0)

""" Find the outliers and replace the outliers"""

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

df_out = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
print(df_out.shape)

df.head(5)

""" Check for Categorical columns and perform encoding"""

df_categorical = df[['Gender', 'HasCrCard', 'IsActiveMember', 'Exited']]

print(df['Gender'].unique())
print(df['HasCrCard'].unique())
print(df['IsActiveMember'].unique())
print(df['Exited'].unique())

from sklearn.preprocessing import LabelEncoder

gender_encoder = LabelEncoder()

gender_encoder.fit(df_categorical['Gender'])
LabelEncoder()

gender_values = gender_encoder.transform(df_categorical['Gender'])

print("After Encoding:", gender_values[-10:])

"""Split the data into dependent and independent variables."""

X = df.iloc[:, :-1].values
print(X)

Y = df.iloc[:, -1].values
print(Y)

"""Split the data into training and testing"""

import numpy as np
from sklearn.model_selection import train_test_split

#output
y= df.EstimatedSalary
 
#input
x=df.drop('EstimatedSalary',axis=1)
 
#splitting
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2)

print("shape of original dataset :", df.shape)
print("shape of input - training set", x_train.shape)
print("shape of output - training set", y_train.shape)
print("shape of input - testing set", x_test.shape)
print("shape of output - testing set", y_test.shape)