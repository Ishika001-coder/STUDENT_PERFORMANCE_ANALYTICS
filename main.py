import pandas as pd
import numpy as np

from functions import (
    calculate_summary,
    calculate_grade,
    check_result
)

# Load dataset
df = pd.read_csv("students.csv")

subjects = ["Python", "Maths", "English"]

print("=" * 60)
print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 60)

# Display dataset information
print("\nTotal Students:", len(df))
print("Dataset Columns:", df.columns.tolist())

# Calculate total and average
df = calculate_summary(df, subjects)

# Assign grades and results
df["Grade"] = df["Average"].apply(calculate_grade)

df["Result"] = df.apply(
    lambda row: check_result(row, subjects),
    axis=1
)

# Student marks summary
print("\n1. STUDENT MARKS SUMMARY")
print(
    df[["Name", "Total", "Average"]]
    .round({"Average": 2})
    .to_string(index=False))
print("\n3. CLASS PERFORMANCE")
print("Highest Average:", round(df["Average"].max(), 2))
print("Lowest Average:", round(df["Average"].min(), 2))
print("Overall Class Average:", round(df["Average"].mean(), 2))

# Subject-wise performance
print("\n4. SUBJECT-WISE PERFORMANCE")

for subject in subjects:
    average_marks = np.mean(df[subject].to_numpy())
    print(subject, "Average:", round(average_marks, 2))

# Top five students
print("\n5. TOP FIVE STUDENTS")
top_students = df.nlargest(5, "Average")

print(
    top_students[["Name", "Average", "Grade"]]
    .round({"Average": 2})
    .to_string(index=False)
)

# Pass and fail statistics
print("\n6. PASS/FAIL STATISTICS")
print(df["Result"].value_counts())

# Final report
print("\n7. COMPLETE STUDENT REPORT")
print(
    df[
        [
            "Student_ID",
            "Name",
            "Department",
            "Total",
            "Average",
            "Grade",
            "Result"
        ]
    ]
    .round({"Average": 2})
    .to_string(index=False)
)

print("\nPROJECT EXECUTION COMPLETED")
