# Asg-8-Matplotlib
# Loan Data Visualization Project

## Purpose
The purpose of this project is to perform visual analysis on a loan dataset. The dataset contains various attributes related to loans and customers, such as customer age, income, loan amount, interest rate, and loan grade. The visualizations help in understanding the distribution and relationships between these attributes.

## Project Structure
The project consists of the following files:
- `Matplotlib.py`: Contains the code for generating visualizations using Matplotlib and Seaborn libraries.
- `LoanDataset - LoansDatasest.csv`: The dataset file containing loan data.

## Class Design and Implementation
This project does not use a class-based design. Instead, it uses functions to load data and generate visualizations. Below is an explanation of the main functions and their attributes:

### Functions

#### `load_data(file_path)`
- **Purpose**: Loads the loan data from a CSV file.
- **Parameters**: 
  - `file_path` (str): The path to the CSV file.
- **Returns**: 
  - `loan_data` (DataFrame): A pandas DataFrame containing the loan data.

#### `plot_loan_grade_distribution(loan_data)`
- **Purpose**: Creates a bar plot showing the distribution of loan grades.
- **Parameters**: 
  - `loan_data` (DataFrame): A pandas DataFrame containing the loan data.
- **Returns**: None

### Attributes
- `loan_data`: A pandas DataFrame containing the loan data loaded from the CSV file.

### Methods
- `load_data`: Loads the loan data from the specified CSV file.
- `plot_loan_grade_distribution`: Generates a bar plot for the distribution of loan grades.

## Usage
1. Ensure you have the required libraries installed:
   ```bash
   pip install pandas matplotlib seaborn
