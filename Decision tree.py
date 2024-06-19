import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.tree import export_text

# Sample data
data = {
    'Age': [22, 25, 47, 52, 46, 56, 23, 24, 35, 33],
    'Income': ['High', 'High', 'Low', 'Medium', 'Low', 'Medium', 'High', 'Medium', 'Low', 'Medium'],
    'Education_Level': ['Bachelor', 'Master', 'PhD', 'PhD', 'Bachelor', 'Master', 'Bachelor', 'Master', 'PhD', 'Bachelor'],
    'Has_Job': [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    'Buy_Laptop': ['Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert categorical data to numerical data
df['Income'] = df['Income'].map({'Low': 0, 'Medium': 1, 'High': 2})
df['Education_Level'] = df['Education_Level'].map({'Bachelor': 0, 'Master': 1, 'PhD': 2})
df['Buy_Laptop'] = df['Buy_Laptop'].map({'No': 0, 'Yes': 1})

# Features and target variable
X = df[['Age', 'Income', 'Education_Level', 'Has_Job']]  # Features
y = df['Buy_Laptop']                                     # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Create Decision Tree classifier object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifier
clf = clf.fit(X_train, y_train)# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Display the decision tree
tree_rules = export_text(clf, feature_names=['Age', 'Income', 'Education_Level', 'Has_Job'])
print(tree_rules)

# Function to interpret the prediction
def interpret_prediction(prediction):
    return 'Buy Laptop' if prediction == 1 else "Don't Buy Laptop"

# Function to map input to numerical values
def map_input(age, income, education_level, has_job):
    income_map = {'Low': 0, 'Medium': 1, 'High': 2}
    education_level_map = {'Bachelor': 0, 'Master': 1, 'PhD': 2}
    has_job_map = {'No': 0, 'Yes': 1}

    return {'Age': age, 'Income': income_map[income], 'Education_Level': education_level_map[education_level], 'Has_Job': has_job_map[has_job]}

# Get input from the user
age = int(input("Enter Age: "))
income = input("Enter Income (Low/Medium/High): ")
education_level = input("Enter Education Level (Bachelor/Master/PhD): ")
has_job = input("Do you have a job? (Yes/No): ")

# Map input to numerical values and create DataFrame
new_data = pd.DataFrame([map_input(age, income, education_level, has_job)])

# Predict the response for new data point
new_prediction = clf.predict(new_data)

# Interpret the prediction
decision = interpret_prediction(new_prediction[0])
print(f"The decision is: {decision}")
