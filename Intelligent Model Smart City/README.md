# Smart City Sensor Data Analysis

This Jupyter Notebook, `Intelligent_Model_SmartCity.ipynb`, performs a comprehensive analysis of time-series sensor data collected from a smart city environment. The goal is to load, process, and visualize the data to uncover trends, correlations, and patterns related to environmental conditions.

## Overview

The notebook demonstrates a complete workflow for handling multi-file time-series datasets. It begins by loading and merging several days of sensor readings, performs essential preprocessing, calculates key statistics, and conducts exploratory data analysis (EDA) through various visualizations.

## Features

- **Multi-File Data Loading**: Automatically finds and loads all `sensor_data_*.csv` files in the directory into a single pandas DataFrame.
- **Data Preprocessing**: Converts the `timestamp` column to a proper datetime format and sets it as the DataFrame index for efficient time-series analysis.
- **Statistical Summary**: Computes and displays summary statistics (mean, min, max, and variance) for each sensor and saves the results to `sensor_statistics.csv`.
- **Exploratory Data Analysis (EDA)**:
  - **Trend Analysis**: Visualizes weekly trends for temperature, humidity, and light intensity by resampling the data to an hourly average.
  - **Correlation Analysis**: Generates a heatmap to show the correlation between different sensor readings.
  - **Pattern Analysis**: Creates a boxplot to analyze the distribution of light intensity across different hours of the day, highlighting the day/night cycle.
- **Output Generation**: Saves all generated plots (`trends_plot.png`, `correlation_heatmap.png`, `day_night_cycle.png`) and the statistical summary for easy reference and reporting.

## Requirements

To run this notebook, you will need Python and the libraries listed in `requirements.txt`.

You can install them using pip:
```bash
pip install -r requirements.txt
```

## How to Run

1.  **Dataset**:
    -   Place your sensor data files (e.g., `sensor_data_2025-03-01.csv`, `sensor_data_2025-03-02.csv`, etc.) in the same directory as the notebook.
    -   The notebook is configured to automatically detect any file matching the pattern `sensor_data_*.csv`.

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch Jupyter**: Open your terminal or command prompt, navigate to the project directory, and run:
    ```bash
    jupyter notebook
    ```

4.  **Open and Run**: Open the `Intelligent_Model_SmartCity.ipynb` file and execute the cells sequentially to perform the analysis and generate the outputs.

## Analysis and Visualizations

The notebook produces the following key visualizations:

### 1. Weekly Sensor Trends

This plot shows the hourly average for temperature, humidity, and light intensity over the entire data collection period, making it easy to spot daily cycles and overall trends.

!Weekly Sensor Trends

### 2. Sensor Correlation Matrix

A heatmap that visualizes the correlation coefficients between all sensor metrics. This helps identify which environmental factors are related (e.g., light and temperature).

!Sensor Correlation Matrix

### 3. Hourly Light Distribution (Day/Night Cycle)

A boxplot showing the distribution of light intensity for each hour of the day. This clearly illustrates the natural day/night cycle and identifies the hours with the most variability.

!Hourly Light Distribution

## Output Files

Upon running the notebook, the following files will be generated in the project directory:

- `sensor_statistics.csv`: A CSV file containing the summary statistics for each sensor.
- `trends_plot.png`: The time-series plot of sensor trends.
- `correlation_heatmap.png`: The heatmap of sensor correlations.
- `day_night_cycle.png`: The boxplot showing the hourly light distribution.