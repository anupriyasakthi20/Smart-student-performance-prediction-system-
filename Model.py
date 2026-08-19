from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import pickle
data = pd.read_csv("student_dataset.csv")
print("Dataset:")
print(data)
print("\nMissing values:")
print(data.isnull().sum())
data = data.dropna()
print("\nData types:")
print(data.dtypes)
print("\nDuplicate Records:", data.duplicated().sum())
data = data.drop_duplicates()
def calculate_performance(row):
    score = (
        row["Attendance_Percentage"] * 0.20
        + min(row["Study_Hours"] * 10, 100) * 0.15
        + (row["IA_Marks"] / 30 * 100) * 0.25
        + row["Assignment_score"] * 0.15
        + row["Previous_score"] * 0.25
    )
    if score >= 75:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"
data["Performance"] = data.apply(
    calculate_performance,
    axis=1
)
print("\nPerformance Distribution:")
print(data["Performance"].value_counts())
features = [
    "Attendance_Percentage",
    "Study_Hours",
    "IA_Marks",
    "Assignment_score",
    "Previous_score"
]
X = data[features]
y = data["Performance"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
model = LogisticRegression(
    max_iter=1000
)
model.fit(X_train, y_train)
print("\nModel trained successfully!")
y_pred = model.predict(X_test)
accuracy = accuracy_score(
    y_test,
    y_pred
)
print("\nModel Accuracy:",round(accuracy * 100, 2),"%")
print("\nClassification Report:")
print(classification_report( y_test, y_pred))
with open(
    "student_performance_model.pkl","wb") as file:
    pickle.dump(model, file)
print(
    "\nModel saved successfully!")
print(
    "File: student_performance_model.pkl")
