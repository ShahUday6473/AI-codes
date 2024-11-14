# Step 1: Import all required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from scipy import stats

# Step 2: Locate open source data from the web
# Dataset: Titanic: Machine Learning from Disaster
# Source: Kaggle Titanic Dataset (https://www.kaggle.com/c/titanic)

# Step 3: Load the dataset into a pandas DataFrame
df = pd.read_csv('titanic.csv')
print("First five rows of the DataFrame:")
print(df.head())

# Step 4: Display the initial statistics
print("\nSummary statistics for numeric variables:")
print(df.describe())

# Step 5: Scan for missing values and inconsistencies
missing_values = df.isnull().sum()
print("\nMissing Values in each column:\n", missing_values)

# Handling missing values:
# 1. Drop rows with missing values in 'Survived'
df.dropna(subset=['Survived'], inplace=True)

# 2. Fill missing 'Age' values with the median age
df['Age'].fillna(df['Age'].median(), inplace=True)

# 3. Fill missing 'Embarked' values with the most frequent value
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 4. Drop the 'Cabin' column due to a large number of missing values
df.drop(columns=['Cabin'], inplace=True)

# Verify missing values after handling
print("\nMissing Values after handling:\n", df.isnull().sum())

# Step 6: Scan for outliers in numeric variables
# Visualize outliers in 'Age' using a boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(df['Age'])
plt.title('Boxplot of Age')
plt.show()

# Handle outliers using the Z-score method
z_scores = np.abs(stats.zscore(df['Age']))
df = df[(z_scores < 3)]  # Keep rows where Z-scores are less than 3

# Step 7: Apply data transformation on 'Fare'
# Apply a log transformation to the 'Fare' column to reduce skewness
df['Fare_log'] = np.log1p(df['Fare'])

# Plot the transformed 'Fare_log' to visualize the effect
plt.figure(figsize=(10, 6))
sns.histplot(df['Fare_log'], bins=20, kde=True)
plt.title('Distribution of Fare After Log Transformation')
plt.show()

# Step 8: Convert categorical variables into quantitative variables
# Convert 'Sex' column from categorical to numeric using LabelEncoder
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])

# Convert 'Embarked' column using one-hot encoding
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)


# Display the updated DataFrame with converted categorical variables
print("\nFirst five rows of the updated DataFrame:")
print(df.head())
