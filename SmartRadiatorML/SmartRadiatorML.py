import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('ML.csv')
#clean our data little bit
dataset.isnull().any()
dataset = dataset.fillna(method='ffill')

#the factors (independent variable)
X = dataset[['Outside temp before start', 'Target tempreture']].values

#the dependet variable (what we would like to predict\explain)
y = dataset['Average Time (in hours)'].values


#training the model
X_train, X_test , y_train , y_test = train_test_split(X,y,test_size=0.25,random_state=0) #75/25 split


model = LinearRegression()
model.fit(X_train, y_train)
X_new = [[-10, 23]]
predictions=model.predict(X_new)




#df = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})


#df1 = df.head(25)
#print(df1)
print("Input=%s, Predicted=%s" % (X_new[0], predictions))