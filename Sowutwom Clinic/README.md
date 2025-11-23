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