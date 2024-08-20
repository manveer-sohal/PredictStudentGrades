# Student Grade Prediction
This project involves predicting student grades using a linear regression model. The model is trained on data from the student-mat.csv dataset and aims to predict final grades based on various student attributes.
## Project Overview
### Data Preparation
- Reads and processes data from student-mat.csv.
- Selects relevant attributes: G1, G2, G3, studytime, failures, absences.
### Model Training
- Utilizes a linear regression model to predict the final grade (G3).
- Uses OLS (ordinary least squares) method to get the line fit
- Includes a loop (currently commented out) to train the model until an accuracy of 97% is achieved.
### Model Persistence
- Saves the trained model and its accuracy using the pickle module.
- Loads the best-performing model and accuracy from saved files for evaluation.
### Model Evaluation
- Prints model performance summary including R^2 score, intercept, and coefficients.
- Provides explanations for each feature's contribution to the model.
### Visualization
- Creates scatter plots to visualize:
  - Actual vs. Predicted Grades
  - Feature (G1) vs. Final Grade (G3)
  
## Findings
**Model Performance**: 
  - The trained model achieved an R^2 score of `0.971338` on the test data, indicating how well the model's predictions align with the actual values.
**Coefficients**:
  - The coefficients of the model provide insights into the influence of each feature on the final grade. For example, the coefficient for `Grade 1` is `0.14146219552038186`, indicating the stregth of the relationship to be weak while the coefficient for `Grade 2` is `0.9915719156327819`, indicating a strong relationship for  the prediction.
**Visualization Insights**:
  - The scatter plot of actual vs. predicted grades shows the model's prediction accuracy. Ideally, the points should closely align along the line of equality.
<img width="754" alt="Screenshot 2024-08-20 at 5 56 37 PM" src="https://github.com/user-attachments/assets/feadff08-9193-4072-b4bb-dc5518ca3c3b">

  - The feature vs. final grade plot helps visualize the relationship between a specific feature and the final grade, showing trends and potential correlations. In the instance below being the 1st grade vs the predicted grade
<img width="764" alt="Screenshot 2024-08-20 at 5 58 03 PM" src="https://github.com/user-attachments/assets/5127a3a2-9ca1-4efb-b5f4-c5089f2aa33b">

## Getting Started
### Prerequisites
Python 3.7
Required libraries: pandas, numpy, scikit-learn, matplotlib, pickle
### Running the Project
1. Ensure student-mat.csv is available in the project directory.
2. Uncomment the training loop to train the model and save it:
3. The script automatically loads the best model and its accuracy, prints the performance summary, and displays scatter plots.
4. The scatter plots will be displayed showing actual vs. predicted grades and a specific feature vs. final grade.
## File Descriptions
'student-mat.csv': Dataset containing student attributes and grades.
'student_grade_prediction.py': Python script containing code for data preparation, model training, evaluation, and visualization.
