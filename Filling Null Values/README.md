# Handling Missing Data in Time-Series Datasets

This Jupyter Notebook provides a practical demonstration of various common techniques for handling missing (NaN) values in a time-series dataset using the `pandas` library. It compares four different imputation methods and analyzes their impact on the dataset's summary statistics.

## Overview

Working with real-world sensor data often involves dealing with missing values. This notebook explores how to load time-series data, identify missing entries, and apply different strategies to fill them. The primary goal is to understand how each method alters the statistical properties of the data.

## Features

-   Loads sensor data from a CSV (`sensor_log.csv`) or creates a mock dataset if the file is not found.
-   Demonstrates four methods for handling null values:
    1.  **Forward Fill (`ffill`)**: Propagates the last valid observation forward.
    2.  **Backward Fill (`bfill`)**: Propagates the next valid observation backward.
    3.  **Linear Interpolation**: Fills NaN values using a linear estimation based on the values before and after.
    4.  **Mean Imputation**: Replaces NaN values with the mean of the entire column.
-   Generates a comprehensive summary table comparing the `min`, `max`, `mean`, and `std` (standard deviation) of the dataset after applying each method.

## Requirements

To run this notebook, you will need Python and the libraries listed in `requirements.txt`.

You can install them using pip:
```bash
pip install -r requirements.txt
```

## How to Run

1.  **Dataset**:
    -   Place your dataset named `sensor_log.csv` in the same directory as the notebook. The CSV should have a `timestamp` column and other numeric data columns.
    -   If `sensor_log.csv` is not found, the notebook will automatically generate a mock dataset with missing values for demonstration purposes.

2.  **Launch Jupyter**: Open your terminal or command prompt, navigate to the project directory, and run:
    ```bash
    jupyter notebook
    ```

3.  **Open and Run**: Open the `Filling_Null_Values.ipynb` file and run the cells sequentially to see the data transformation and the final statistical comparison.

## Imputation Methods Explored

The notebook provides a hands-on look at the following `pandas` methods:

### 1. Forward Fill (`ffill`)

This method fills missing values by carrying forward the last known non-null value. It is useful when data points are missing for short periods and you can assume the value has not changed.

```python
df_ffill = df_original.ffill()
```

### 2. Backward Fill (`bfill`)

This method fills missing values by using the next known non-null value to fill the gap.

```python
df_bfill = df_original.bfill()
```

### 3. Linear Interpolation

This method treats the data as a sequence and fills missing values by estimating them based on the values of their neighbors. It assumes a linear relationship between data points.

```python
df_interp = df_original.interpolate(method='linear')
```

### 4. Mean Imputation

This method calculates the mean of a column and uses it to fill all missing values within that column. It can distort the data's variance but is a simple and common technique.

```python
column_means = df_original.mean()
df_mean = df_original.fillna(column_means)
```

## Summary Statistics and Comparison

The final output of the notebook is a Markdown table that presents the summary statistics (`min`, `max`, `mean`, `std`) for each data column, comparing the original dataset (with NaNs) against the datasets produced by each imputation method. This allows for a clear analysis of how each technique affects the overall data distribution.

This comparison is crucial for deciding which imputation method is most appropriate for your specific use case, as each one introduces its own form of bias.