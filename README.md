# Asg-8-Matplotlib
# Data Visualization Project

## Purpose
This project aims to perform visual analysis on different datasets, including a loan dataset and the Iris dataset. The visualizations help in understanding the distribution and relationships between various attributes in these datasets.

## Project Structure
The project consists of the following files:
- `Matplotlib.py`: Contains the code for generating visualizations using Matplotlib and Seaborn libraries.
- `LoanDataset - LoansDatasest.csv`: The dataset file containing loan data.

## Datasets

### Loan Dataset
The loan dataset contains various attributes related to loans and customers, such as:
- `customer_id`
- `customer_age`
- `customer_income`
- `home_ownership`
- `employment_duration`
- `loan_intent`
- `loan_grade`
- `loan_amnt`
- `loan_int_rate`
- `term_years`
- `historical_default`
- `cred_hist_length`
- `current_loan_status`

### Iris Dataset
The Iris dataset is a classic dataset in machine learning and statistics. It contains 150 samples of iris flowers, each described by four features:
- `sepal length (cm)`
- `sepal width (cm)`
- `petal length (cm)`
- `petal width (cm)`

The dataset also includes the species of each flower, which can be one of three types:
- `setosa`
- `versicolor`
- `virginica`

## Visualizations

### Loan Dataset Visualizations
#### `plot_loan_grade_distribution(loan_data)`
- **Purpose**: Creates a bar plot showing the distribution of loan grades.
- **Parameters**: 
  - `loan_data` (DataFrame): A pandas DataFrame containing the loan data.
- **Returns**: None

### Iris Dataset Visualizations
#### Pair Plot
- **Purpose**: Creates a pair plot to visualize the relationships between features in the Iris dataset.
- **Code**:
  ```python
  sns.pairplot(iris_df, hue='species', markers=["o", "s", "D"])
  plt.suptitle('Pair Plot of Iris Dataset', y=1.02)
  plt.show()
