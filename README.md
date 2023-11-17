# 57042025_churning_customers
About
An AI model created to forecast customer churn for a subscription-based service is available in this repository. The model forecasts customers' chances to cancel subscriptions by analysing past customer data using machine learning algorithms.
Structure
Data: Contains the CSV file for model training and evaluation
Model: Uses keras to build models
Notebook: a COLAB file for exploratory data analysis and model development
Dependencies
Python 3.
NumPy
Pandas
Scikit-learn
Matplotlib
pickle
RandomForestClassifier
seaborn
TensorFlow
Keras
learn
Usage
Put the dataset in the directory called path
Open and run the model_training.py script there.

To predict:
Open the models/ directory and load the trained model.
To forecast churn for new customer data, use the model.
Model Training
Gender, senior citizen, tenure, Internet service, online security, online backup, TechSupport, contract, payment method, monthly charges, and total charges metrics are among the features of the historical customer data used to train the model. The dataset is preprocessed to handle missing values, encode categorical variables, and scale numerical features. To maximise model performance, I employ a variety of machine learning algorithms (such as Random Forest) and hyperparameter tuning.
Evaluation
Metrics like ROC AUC score, accuracy, precision, and recall are used to assess the model's performance. The generalisation abilities of the model are evaluated using a hold-out test set and cross-validation.
Outcomes
The trained model obtains an 83% AUC score and accuracy score , 
