# Multiple Linear Regression
setwd('/Users/rajatpa/Documents/DS/ML_A-Z/Part2_Regression/Section5_Multiple_Linear_Regression')
# Importing the dataset
dataset = read.csv('50_Startups.csv')

# Encoding categorical data
dataset$State = factor(dataset$State,
                       levels = c('New York', 'California', 'Florida'),
                       labels = c(1, 2, 3))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

# Fitting Multiple Linear Regression to the Training set
regressor = lm(formula = Profit ~ .,
               data = training_set)

summary(regressor)

# Predicting the Test set results
y_pred = predict(regressor, newdata = test_set)


# Fitting Multiple Linear Regression using backward elemination process 
regressor_ols = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data = dataset)

summary(regressor_ols)

# As we saw both the Sate2 and State3 having higher P-value and greater than 0.0.5 we will remove State feature
regressor_ols = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
                   data = dataset)

summary(regressor_ols)

# As we saw Administration feature has high P-value that is 0.602, need to remove that
regressor_ols = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
                   data = dataset)

summary(regressor_ols)

# As we saw Marketing.Spend feature has high P-value that is 0.6, need to remove that
regressor_ols = lm(formula = Profit ~ R.D.Spend,
                   data = dataset)

summary(regressor_ols)


