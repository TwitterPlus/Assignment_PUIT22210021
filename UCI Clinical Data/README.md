# Heart Failure Clinical Records — Notebook

Overview
--------

This repository contains a Jupyter Notebook, `Heart Failure.ipynb`, that performs data cleaning, exploratory
data analysis, outlier removal, model training (Logistic Regression and Random Forest), evaluation and a simple
patient report generator for the Heart Failure Clinical Records dataset.

Files of interest
- `Heart Failure.ipynb` — main analysis notebook (EDA, modeling, reporting).
- `heart_failure_clinical_records_dataset.csv` — expected dataset (place in project root).
- `requirements.txt` — Python packages needed to run the notebook.

Quick setup (Windows PowerShell)
-------------------------------

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv venv
; .\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Start the Jupyter Notebook server and open the notebook:

```powershell
jupyter notebook
```

How to use the notebook
-----------------------

- Run the cells in order. The notebook loads the CSV `heart_failure_clinical_records_dataset.csv` from the
  repository root — make sure that file exists in the same folder as the notebook.
- Sections included:
  - Dependencies and imports
  - Data loading and summary statistics
  - Exploratory Data Analysis (countplots, boxplots, correlation)
  - Outlier removal helper and cleaning
  - Model training (Logistic Regression and Random Forest)
  - Model evaluation (classification report, confusion matrix, ROC)
  - Patient report generator and helper `get_report_by_index`

Notes & tips
-----------

- The notebook trains models on a cleaned subset (outliers removed). If you re-run cells that re-train models,
  the `generate_patient_report` and `get_report_by_index` functions will use the most recently trained `log_reg` and `scaler` variables.
- If your dataset is large or you want repeatable results, seed is already set in `train_test_split` and model constructors.
- If you prefer a reproducible environment, consider exporting a pinned `pip freeze` after setting up your environment.

Troubleshooting
---------------

- If `pip install mediapipe` or other package installs fail, check your Python version and consult the package
  installation instructions. The `requirements.txt` included here lists conservative minimum versions known to work.
- On Windows, ensure PowerShell has permission to run the venv activation script. You may need `Set-ExecutionPolicy` to allow running local scripts.

Contact
-------

If you'd like further help (pinning exact versions, creating a conda environment, or converting the notebook into a script),
tell me what you want next and I can update files or run install commands in your environment.
# Diabetes Prediction from Clinical Data

This Jupyter Notebook, `Sowutwom_Clinic.ipynb`, details the process of building and evaluating machine learning models to predict diabetes status based on a clinical dataset. The project covers data preprocessing, exploratory data analysis, model training, and performance comparison.

## Overview

The primary objective of this notebook is to develop a predictive model that can accurately classify patients as diabetic or non-diabetic using their health metrics. It demonstrates a complete machine learning workflow, from initial data inspection to comparing the performance of different classification algorithms.

## Features

-   **Data Loading and Inspection**: Loads the `sowutuom_clinic_dataset.csv` and performs an initial inspection to understand its structure and check for issues like class imbalance.
-   **Data Preprocessing**:
    -   Uses `LabelEncoder` to convert categorical features (e.g., `blood_group`, `genotype`) into a numerical format suitable for modeling.
    -   Applies `StandardScaler` to normalize numerical features, which is crucial for models like Logistic Regression.
-   **Exploratory Data Analysis (EDA)**:
    -   Generates a **correlation matrix** to visualize the relationships between different health metrics.
    -   Creates a **scatter plot** of Glucose vs. BMI to visually inspect the separation between diabetic and non-diabetic patients.
-   **Model Training and Evaluation**:
    -   Splits the data into training (80%) and testing (20%) sets using a stratified approach to handle class imbalance.
    -   Trains and evaluates two popular classification models:
        1.  **Logistic Regression**: A linear model used as a baseline.
        2.  **Random Forest**: An ensemble model known for its high accuracy and ability to provide feature importance.
    -   Uses a helper function to systematically evaluate models on Accuracy, Precision, Recall, and F1-Score.
-   **Feature Importance**: Analyzes and visualizes the feature importance scores from the Random Forest model to identify the most influential factors in predicting diabetes.
-   **Model Comparison**: Presents a final summary table comparing the performance metrics of both models.

## Requirements

To run this notebook, you will need Python and the libraries listed in `requirements.txt`.

You can install them using pip:
```bash
pip install -r requirements.txt
```

## How to Run

1.  **Dataset**:
    -   Ensure the dataset file named `sowutuom_clinic_dataset.csv` is in the same directory as the notebook.

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch Jupyter**: Open your terminal or command prompt, navigate to the project directory, and run:
    ```bash
    jupyter notebook
    ```

4.  **Open and Run**: Open the `Sowutwom_Clinic.ipynb` file and execute the cells sequentially to see the full analysis and model results.

## Models and Evaluation

The notebook implements and compares the following models:

### 1. Logistic Regression
A straightforward and interpretable linear model. It serves as a strong baseline to measure the performance of more complex models. The data is scaled before training this model.

### 2. Random Forest
An ensemble of decision trees that generally provides higher accuracy and is robust to overfitting. This model also allows us to extract feature importances to understand the key drivers of the prediction.

The final output includes a markdown table comparing the key performance metrics of both models, helping to determine which is better suited for this prediction task.

## Output Files

Upon running the notebook, the following output files are generated:

-   `diabetes_correlation.png`: A heatmap showing the correlation between features.
-   `glucose_bmi_scatter.png`: A scatter plot visualizing the relationship between glucose, BMI, and diabetes status.
-   `feature_importance.png`: A bar chart showing the importance of each feature in the Random Forest model's prediction.