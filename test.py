# ============================================
# DATA CLEANING & VISUALIZATION PROJECT
# Student Performance Analysis
# ============================================

# -----------------------------
# STEP 1: IMPORT LIBRARIES
# -----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Optional Settings
plt.rcParams['figure.figsize'] = (8,5)
sns.set_style("whitegrid")

print("Libraries Imported Successfully")


# -----------------------------
# STEP 2: CREATE SAMPLE DATASET
# -----------------------------
data = {
    "Name": ["Aman", "Rahul", "Priya", "Sneha", "Karan",
             "Aman", "Riya", "Vikas", "Neha", "Arjun"],

    "Age": [18, 19, 18, 20, np.nan,
            18, 19, 21, 20, 22],

    "Gender": ["Male", "Male", "Female", "Female", "Male",
               "Male", "Female", "Male", "Female", "Male"],

    "Math_Score": [85, 78, 92, 88, 150,
                   85, np.nan, 65, 72, 90],

    "Science_Score": [80, 75, 95, 89, 45,
                      80, 70, 60, np.nan, 91],

    "English_Score": [78, 74, 90, 85, 50,
                      78, 76, 58, 69, 88],

    "Attendance": [90, 85, 95, 92, 40,
                   90, 88, 70, 75, 96],

    "Study_Hours": [3, 2, 5, 4, 1,
                    3, 3, 2, 2, 5]
}

df = pd.DataFrame(data)

print("\nDataset Created Successfully")
print(df)


# -----------------------------
# STEP 3: SAVE DATASET AS CSV
# -----------------------------
df.to_csv("students.csv", index=False)

print("\nCSV File Saved Successfully")


# -----------------------------
# STEP 4: LOAD DATASET
# -----------------------------
df = pd.read_csv("students.csv")

print("\nFirst 5 Rows:")
print(df.head())


# -----------------------------
# STEP 5: BASIC INFORMATION
# -----------------------------
print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)


# -----------------------------
# STEP 6: CHECK MISSING VALUES
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())


# -----------------------------
# STEP 7: HANDLE MISSING VALUES
# -----------------------------
# Fill numerical missing values with mean

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Math_Score"].fillna(df["Math_Score"].mean(), inplace=True)
df["Science_Score"].fillna(df["Science_Score"].mean(), inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# -----------------------------
# STEP 8: CHECK DUPLICATES
# -----------------------------
print("\nDuplicate Rows:")
print(df.duplicated().sum())


# -----------------------------
# STEP 9: REMOVE DUPLICATES
# -----------------------------
df.drop_duplicates(inplace=True)

print("\nDuplicates Removed")
print("New Shape:", df.shape)


# -----------------------------
# STEP 10: DESCRIPTIVE STATISTICS
# -----------------------------
print("\nStatistical Summary:")
print(df.describe())


# -----------------------------
# STEP 11: DETECT OUTLIERS
# -----------------------------
print("\nDisplaying Boxplots for Outlier Detection")

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
sns.boxplot(y=df["Math_Score"])
plt.title("Math Score Outliers")

plt.subplot(1,2,2)
sns.boxplot(y=df["Science_Score"])
plt.title("Science Score Outliers")

plt.tight_layout()
plt.show()


# -----------------------------
# STEP 12: REMOVE OUTLIERS
# -----------------------------
# Removing rows where Math Score > 100

df = df[df["Math_Score"] <= 100]

print("\nOutliers Removed")
print(df)


# -----------------------------
# STEP 13: AVERAGE SCORES
# -----------------------------
avg_scores = df[["Math_Score",
                 "Science_Score",
                 "English_Score"]].mean()

print("\nAverage Scores:")
print(avg_scores)


# -----------------------------
# STEP 14: BAR CHART
# -----------------------------
avg_scores.plot(kind='bar')

plt.title("Average Subject Scores")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()

# -----------------------------
# STEP 15: ATTENDANCE VS MATH SCORE
# -----------------------------
sns.scatterplot(
    x="Attendance",
    y="Math_Score",
    data=df
)

plt.title("Attendance vs Math Score")

plt.show()


# -----------------------------
# STEP 16: STUDY HOURS VS MATH SCORE
# -----------------------------
sns.lineplot(
    x="Study_Hours",
    y="Math_Score",
    data=df
)

plt.title("Study Hours vs Math Score")

plt.show()


# -----------------------------
# STEP 17: CORRELATION HEATMAP
# -----------------------------
correlation = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()


# -----------------------------
# STEP 18: TOPPER STUDENT
# -----------------------------
df["Total"] = (
    df["Math_Score"] +
    df["Science_Score"] +
    df["English_Score"]
)

topper = df.sort_values(by="Total", ascending=False)

print("\nTopper Student:")
print(topper[["Name", "Total"]].head(1))


# -----------------------------
# STEP 19: SAVE CLEANED DATASET
# -----------------------------
df.to_csv("cleaned_students.csv", index=False)

print("\nCleaned Dataset Saved Successfully")


# -----------------------------
# STEP 20: FINAL CONCLUSION
# -----------------------------
print("\n========== PROJECT COMPLETED ==========")

print("""
Insights:
1. Missing values were handled
2. Duplicate rows were removed
3. Outliers were detected and removed
4. Visualizations were created
5. Correlation between features was analyzed
6. Top performing student was identified
""")



