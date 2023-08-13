# 4
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data from CSV
data = pd.read_csv('handlandmarks_data.csv')

# Extract labels (first column) and features (rest of the columns)
X = data.iloc[:, 1:]
y = data.iloc[:, 0]

# List of unique label names
label_names = y.unique()

# Create an empty DataFrame to store accuracy values
accuracy_table = pd.DataFrame(columns=['Dataset', 'Model', 'Accuracy'])

# Loop through label names and models
for label_name in label_names:
    # Filter data for the current label
    X_subset = X[y == label_name]
    y_subset = y[y == label_name]

    # Check if there are enough samples for splitting
    if len(X_subset) < 2:
        print(f"Skipping label '{label_name}' due to insufficient samples for splitting.")
        continue

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_subset, y_subset, test_size=0.2, random_state=42)

    # Train Random Forest model
    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    y_rf_pred = rf_model.predict(X_test)
    accuracy_rf = accuracy_score(y_test, y_rf_pred) * 100

    # Append accuracy to the accuracy table
    accuracy_table = accuracy_table.append({'Dataset': label_name, 'Model': 'Random Forest', 'Accuracy': accuracy_rf}, ignore_index=True)

# Print the accuracy comparison table
print(accuracy_table)
