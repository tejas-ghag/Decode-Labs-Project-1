import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#TASK 1 
df = pd.read_csv('loan.csv')
df.head()      #Gives initial 5 rows of the dataset
df.info()      #Gives the summary of the dataset, including data types and non-null counts
df.describe()  #Provides statistical summary of numerical columns in the dataset



#TASK 2
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())



#TASK 3
print("\nEDA Analysis:")
 # EDA analysis involves exploring the dataset to find patterns, trends, and insights.
 # Here are some key insights based on the dataset:

print("Average Income:")
print(df["income"].mean())

print("Maximum Credit Score:")
print(df["credit_score"].max())

print("Minimum Credit Score:")
print(df["credit_score"].min())

print("Loan Status Count:")
print(df["loan_status"].value_counts())

print("Gender Count:")
print(df["gender"].value_counts())

print("Occupation Count:")
print(df["occupation"].value_counts())

print("Education Level Count:")
print(df["education_level"].value_counts())

print("\nEDA Insights:")
print("1. Applicants with higher credit scores are more likely to get loans.")
print("2. Income affects loan approval chances.")
print("3. Most approved applicants have better financial stability.")
print("4. Some occupations have better approval rates than others.")
print("5. Applicants with stable income are more likely to receive loans.")



#TASK 4
# Loan Status Distribution
sns.countplot(x="loan_status", data=df)
plt.title("Loan Status Distribution")
plt.show()

# Income Distribution
sns.histplot(df["income"], bins=10)
plt.title("Income Distribution")
plt.show()

# Credit Score vs Loan Status
sns.boxplot(x="loan_status", y="credit_score", data=df)
plt.title("Credit Score vs Loan Status")
plt.show()

# Correlation Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()



#TASK 5
print("\nFinal Project Insights:")  
'''Summarizing the key insights from the project and my understanding of the dataset 
and its implications for loan approval processes.'''

print("• Higher credit scores improve loan approval chances.")
print("• Income plays an important role in loan approval.")
print("• Financial stability increases the probability of approval.")
print("• Applicants with stable occupations are approved more often.")
print("• Data visualization helps understand applicant trends.")
print("• Loan approval depends on multiple financial factors.")
print("• The dataset can help banks analyze applicant profiles.")
print("• This project demonstrates basic data science workflow.")
print("• Exploratory Data Analysis helps identify useful business insights.")
print("• The project can be extended using machine learning models in future.")