import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

import matplotlib.pyplot as plt

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Pair plot
sns.pairplot(iris_df, hue='species', markers=["o", "s", "D"])
plt.suptitle('Pair Plot of Iris Dataset', y=1.02)
plt.show()

# Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='species', y='sepal length (cm)', data=iris_df)
plt.title('Box Plot of Sepal Length by Species')
plt.show()

# Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='species', y='petal length (cm)', data=iris_df)
plt.title('Violin Plot of Petal Length by Species')
plt.show()



# Load the loan data
loan_data = pd.read_csv("C:/Users/danie/Downloads/Pythonclasstwo/LoanDataset - LoansDatasest.csv")

# Plot the distribution of customer ages
plt.figure(figsize=(10, 6))
plt.hist(loan_data['customer_age'], bins=20, edgecolor='black', alpha=0.7)
plt.title('Distribution of Customer Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# Plot interest rate distribution by loan grade
plt.figure(figsize=(12, 6))
sns.boxplot(x='loan_grade', y='loan_int_rate', data=loan_data)
plt.title('Interest Rate Distribution by Loan Grade')
plt.xlabel('Loan Grade')
plt.ylabel('Interest Rate (%)')
plt.show()

# Create a bar plot for the distribution of loan grades
plt.figure(figsize=(10, 6))
sns.countplot(x='loan_grade', data=loan_data, palette='viridis')
plt.title('Distribution of Loan Grades')
plt.xlabel('Loan Grade')
plt.ylabel('Count')
plt.grid(True)
plt.show()
