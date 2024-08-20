import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt


#reads in data from student-mat.csv usings pandas, data is seperated by ';'
data = pd.read_csv("student-mat.csv", sep = ";")

#Get the specific atributes we want to  look at
data = data[["G1","G2", "G3", "studytime", "failures", "absences"]]

#the data we are trying to predict (like the y-axis)
predict = "G3"

#takes away the atribute and stores in X ( Data are trying to predict)
X = np.array(data.drop([predict], axis = 1))

#All of our labels (Data we are using to get our prediction)
Y = np.array(data[predict])

#splits data into 4 arrays, x_train and y_train are the data we are using to train
# x_test and y_test are the data we are using to test our model on
#We set the test_size to 0.1 for the 10-fold split size (industry standard)
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X,Y, test_size = 0.1)

linear = linear_model.LinearRegression()

#Fits the line to the data using OLS (ordinary least squares) method
#squaring each residules and adding them up, finding a line with the smallest value
linear.fit(x_train, y_train)

acc = linear.score(x_test,y_test)
coef = linear.coef_
predictions = linear.predict(x_test)
nameOfCoef = ["Grade 1", "Grade 2", "Hours Studied", "Failures", "Absences"]

print("Model Performance Summary:\n---------------------------")
print("R^2 Score: ",acc)
print("Intercept: " , linear.intercept_ )
print("Coefficients:\n")

for x in range(len(coef)):
    print(f"- {nameOfCoef[x]}:", linear.coef_[x])

print("Feature Explanation:\n---------------------\n- **Grade 1**: The first grade the student received.\n- **Grade 2**: The second grade the student received.\n- **Hours Studied**: Number of hours the student studied.\n- **Failures**: Number of previous failures.\n- **Absences**: Number of absences.")


plt.scatter(range(len(y_test)), y_test, color='blue', label='Actual')
plt.scatter(range(len(predictions)), predictions, color='red', label='Predicted')
plt.xlabel('Sample Index')
plt.ylabel('Grade')
plt.title('Actual vs Predicted Grades')
plt.legend()
plt.show()