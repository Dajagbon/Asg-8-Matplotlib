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
By running these code snippets, you will get three informative visualizations:

**A histogram showing the distribution of customer ages.**

Distribution of Customer Ages: The histogram shows the age distribution of customers. Most customers are within a certain age range, with fewer customers at the extreme young and old ends of the spectrum. The peak indicates the most common age group among the customers.

**A box plot displaying loan amounts grouped by loan intents.**

Interest Rate Distribution by Loan Grade: The boxplot illustrates how interest rates vary across different loan grades. Higher loan grades tend to have lower interest rates, while lower loan grades are associated with higher interest rates. This relationship highlights the impact of loan grades on the cost of borrowing.

**A bar plot showing the count of each loan grade.**

Distribution of Loan Grades: The bar plot reveals the frequency of each loan grade within the dataset. It shows which loan grades are more common among the customers, with some grades being more prevalent than others. This distribution helps understand the overall quality of the loan portfolio.

### Iris Dataset Visualizations
#### Pair Plot
- **Purpose**: Creates a pair plot to visualize the relationships between features in the Iris dataset.

#### Box Plot
- **Purpose**: Creates a box plot to visualize the distribution of sepal length by species.


#### Violin Plot
- **Purpose**: Creates a violin plot to visualize the distribution of petal length by species.

**Usage**: 
1. Ensure you have the required libraries installed:
   
pip install pandas matplotlib seaborn sci-kit-learn

3. Load the data and generate visualizations by running the Matplotlib.py script:
   
python Matplotlib.py

## Limitations
The project currently includes visualizations for the distribution of loan grades and various visualizations for the Iris dataset. Additional visualizations can be added to provide more insights into the data.
The loan dataset file path is hardcoded. However, it can be modified to accept user input or configuration files for better flexibility.

## Conclusion
This project provides a basic framework for visualizing loan data and the Iris dataset. It can be extended to include more complex analyses and visualizations to gain deeper insights into the datasets.
