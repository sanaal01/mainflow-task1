
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("heart.csv")


sns.set(style="whitegrid", palette="muted")

# Define a color palette
palette = sns.color_palette("Set2")
#Questions
#What is the distribution of age among patients?
#How does the distribution of cholesterol levels vary by sex?
#What is the correlation between different features in the dataset?
#What is the average maximum heart rate achieved (thalach) by patients grouped by target (heart disease presence)?
#How many patients have fasting blood sugar levels greater than 120 mg/dl (fbs = 1) and how many do not (fbs = 0)?
#What is the distribution of chest pain types (cp) in the dataset?
#What is the relationship between age and maximum heart rate achieved (thalach)?
#How many patients have heart disease (target = 1) versus those who do not (target = 0)?
# Q1: Distribution of age among patients
plt.figure(figsize=(12, 6))
sns.histplot(df['age'], bins=30, kde=True, color=palette[0])
plt.title('Distribution of Age', fontsize=18, fontweight='bold')
plt.xlabel('Age', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
sns.despine()
plt.show()

# Q2: Distribution of cholesterol levels by sex
plt.figure(figsize=(12, 6))
sns.boxplot(x='sex', y='chol', data=df, palette="Set2")
plt.title('Cholesterol Levels by Sex', fontsize=18, fontweight='bold')
plt.xlabel('Sex (0 = Female, 1 = Male)', fontsize=14)
plt.ylabel('Cholesterol', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
sns.despine()
plt.show()

# Q3: Correlation between different features
plt.figure(figsize=(14, 10))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix', fontsize=18, fontweight='bold')
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
sns.despine()
plt.show()

# Q4: Average maximum heart rate achieved by patients grouped by target
plt.figure(figsize=(12, 6))
thalach_mean = df.groupby('target')['thalach'].mean().reset_index()
sns.barplot(x='target', y='thalach', data=thalach_mean, palette="Set2")
plt.title('Average Maximum Heart Rate by Heart Disease Presence', fontsize=18, fontweight='bold')
plt.xlabel('Heart Disease (0 = No, 1 = Yes)', fontsize=14)
plt.ylabel('Average Maximum Heart Rate', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
sns.despine()
plt.show()

# Q5: Fasting blood sugar levels
plt.figure(figsize=(12, 6))
fbs_counts = df['fbs'].value_counts().reset_index()
sns.barplot(x='index', y='fbs', data=fbs_counts, palette="Set2")
plt.title('Fasting Blood Sugar Levels', fontsize=18, fontweight='bold')
plt.xlabel('Fasting Blood Sugar (0 = <= 120 mg/dl, 1 = > 120 mg/dl)', fontsize=14)
plt.ylabel('Number of Patients', fontsize=14)
plt.xticks(fontsize=12, rotation=0)
plt.yticks(fontsize=12)
sns.despine()
plt.show()

# Q6: Distribution of chest pain types
plt.figure(figsize=(12, 6))
cp_counts = df['cp'].value_counts().reset_index()
sns.barplot(x='index', y='cp', data=cp_counts, palette="Set2")
plt.title('Chest Pain Types', fontsize=18, fontweight='bold')
plt.xlabel('Chest Pain Type', fontsize=14)
plt.ylabel('Number of Patients', fontsize=14)
plt.xticks(fontsize=12, rotation=0)
plt.yticks(fontsize=12)
sns.despine()
plt.show()

# Q7: Relationship between age and maximum heart rate achieved
plt.figure(figsize=(12, 6))
sns.scatterplot(x='age', y='thalach', data=df, hue='target', palette="Set2", s=100)
plt.title('Age vs. Maximum Heart Rate Achieved', fontsize=18, fontweight='bold')
plt.xlabel('Age', fontsize=14)
plt.ylabel('Maximum Heart Rate Achieved', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Heart Disease', fontsize=12, title_fontsize=14)
sns.despine()
plt.show()

# Q8: Heart disease presence
plt.figure(figsize=(12, 6))
target_counts = df['target'].value_counts().reset_index()
sns.barplot(x='index', y='target', data=target_counts, palette="Set2")
plt.title('Heart Disease Presence', fontsize=18, fontweight='bold')
plt.xlabel('Heart Disease (0 = No, 1 = Yes)', fontsize=14)
plt.ylabel('Number of Patients', fontsize=14)
plt.xticks(fontsize=12, rotation=0)
plt.yticks(fontsize=12)
sns.despine()
plt.show()
