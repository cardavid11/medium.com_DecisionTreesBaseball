# Necessary imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, mean_squared_error
import matplotlib.pyplot as plt

# Load the baseball dataset
data = pd.read_csv('../data/generated_baseball_data.csv')

# Quick overview of the dataset
print(data.head())

# Data preprocessing (assuming there are some categorical variables and missing values)
data = pd.get_dummies(data, drop_first=True)
data.dropna(inplace=True)

# Splitting data into features and target (Let's assume we're predicting if a player will get MVP based on their stats)
X = data.drop('MVP', axis=1)
y = data['MVP']

# Splitting the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the Decision Tree model
clf = DecisionTreeClassifier(max_depth=5)  # Limiting to depth 5 for visualization purposes
clf.fit(X_train, y_train)

# Visualizing the Decision Tree
plt.figure(figsize=(20,10))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=['Not MVP', 'MVP'], rounded=True)
plt.show()

# Making predictions and evaluating the model
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Further, if you want to showcase regularization/pruning, play with the parameters:
# clf = DecisionTreeClassifier(max_depth=5, min_samples_leaf=10, min_samples_split=20)

