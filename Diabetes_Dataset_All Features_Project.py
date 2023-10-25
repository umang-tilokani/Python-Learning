# Linear Regression - Slicing - Training - Testing - on diabetes dataset for only 2 features
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

# Loading Datasets
diabetes = datasets.load_diabetes()

# Slicing
diabetes_X = diabetes.data
diabetes_X_train = diabetes_X[: -30]
diabetes_X_test = diabetes_X[-30:]
diabetes_y_train = diabetes.target[: -30]
diabetes_y_test = diabetes.target[-30:]

# Training
model = linear_model.LinearRegression()
model.fit(diabetes_X_train, diabetes_y_train)

# Testing
diabetes_y_predicted = model.predict(diabetes_X_test)
print("Mean Squared Error: ", mean_squared_error(diabetes_y_test, diabetes_y_predicted))
print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)
