# Multiple Linear Regression
import os
os.chdir('/Users/rajatpa/Documents/DS/ML_A-Z/Part2_Regression/Section5_Multiple_Linear_Regression')

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# as we know the formula for multiple linear regression y = b0 + b1 x1 + b2 x2 + .. + bn xn
# but if we see properly then we can write this as y = b0 x0 + b1 x1 + b2 x2 + .. + bn xn considering x0 =1
# But for introducing the x0 as 1 we have to tweak our model a little bit as by default it is not supported
# ideally we should write this : X = np.append(arr = X,values = np.ones((50,1)).astype(int),axis = 1)
# but if we write this then then coulmns with all one will insert at the end of X Matrix.
# so we are interchanging the arr and values 
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50,1)).astype(int), values = X ,axis = 1)
X
# let's apply the backward elimination
# we have to create a new matrix of X called X_opt which contains all the features
# ideally the X_opt should contain only the optimal independent. At the time of initialization it will contain all
# Then we have to remove one by one using the backward elimination algorithms that are not statistically significant
# we have to write all the index's of columns in the X, as we have to eliminate the columns one by one if required.
X_opt = X[:,[0,1,2,3,4,5]]
# We have to create a new regressor object because here the regressor object will create from class statsmodels
regressor_OLS = sm.OLS(endog = y,exog = X_opt ).fit()
regressor_OLS.summary()
# From the summary we saw that the index 2 that is X2 has the highest p-value that is 0.99 . so we have to remove this
X_opt = X[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y,exog = X_opt ).fit()
regressor_OLS.summary()
# From the summary we saw that the index 2 that is X1 has the highest p-value that is 0.94 . so we have to remove this
X_opt = X[:,[0,3,4,5]]
regressor_OLS = sm.OLS(endog = y,exog = X_opt ).fit()
regressor_OLS.summary()
# From the summary we saw that the index 2 that is X2 has the highest p-value that is 0.602 . so we have to remove this
X_opt = X[:,[0,3,5]]
regressor_OLS = sm.OLS(endog = y,exog = X_opt ).fit()
regressor_OLS.summary()
# From the summary we saw that the index 2 that is X2 has the highest p-value that is 0.60 . so we have to remove this
X_opt = X[:,[0,3]]
regressor_OLS = sm.OLS(endog = y,exog = X_opt ).fit()
regressor_OLS.summary()