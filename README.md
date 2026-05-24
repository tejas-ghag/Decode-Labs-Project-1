# Loan Approval Analysis Project

## Project Overview

This is a beginner-level Data Science project based on loan applicant data.

In this project:

* The dataset was analyzed
* Missing values and duplicates were checked
* Different graphs were created
* Insights were generated from the data

This project was created for the Decode Labs Internship Task.

---

## Dataset Used

* `loan.csv`

The dataset contains:

* Age
* Gender
* Occupation
* Education Level
* Marital Status
* Income
* Credit Score
* Loan Status

---

## Libraries Used

* Pandas
* Matplotlib
* Seaborn

---

## Tasks Completed

### Task 1: Dataset Understanding

* Loaded dataset
* Viewed rows and columns
* Checked dataset information

### Task 2: Data Cleaning

* Checked missing values
* Checked duplicate rows

### Task 3: Exploratory Data Analysis

* Analyzed income
* Analyzed credit score
* Generated insights

### Task 4: Data Visualization

Created:

* Loan Status Distribution
* Income Distribution
* Credit Score vs Loan Status
* Correlation Heatmap

### Task 5: Insight Project

Generated insights from the dataset.

---

## Project Insights

* Higher credit scores improve loan approval chances.
* Income affects loan approval.
* Financial stability increases approval probability.

---

## Output Graphs

### Loan Status Distribution
<img src="Plots/Loan status distribution.png">

### Income Distribution
<img src="Plots/Income Distribution.png">

### Credit Score vs Loan Status
<img src="Plots/Credit Score vs Loan Status.png">

### Correlation Heatmap
<img src="Plots/Correlation Heatmap.png">

---

## How to Run

Install required libraries:

```bash
pip install pandas matplotlib seaborn
```

Run the Python file:

```bash
python loan_analysis.py
```

---

## Project Folder Structure

```text
Decode-Labs-Project-1/
│
├── loan.csv
├── loan_analysis.py
├── README.md
│
└── Plots/
    ├── Correlation Heatmap.png
    ├── Credit Score vs Loan Status.png
    ├── Income Distribution.png
    └── Loan status distribution.png
```
