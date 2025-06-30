# Temperature Data Analysis (1 Year)

This Python project simulates and analyzes temperature data for an entire year using NumPy, Matplotlib, and Seaborn. The script performs statistical analysis and generates visualizations based on randomly generated temperature values.

## Description

The project includes:

- Generation of synthetic daily temperature data using NumPy's `random.normal`
- Calculation of monthly average temperatures
- Identification and counting of extreme temperature days (above 37°C)
- Visualization of the overall temperature distribution using a KDE plot

## Features

- Random generation of 365 temperature values (simulating daily data for a year)
- Monthly average temperature analysis based on standard month lengths
- Detection of "Extreme Temperature" days
- Density visualization using Seaborn's `displot` (KDE)

## Technologies Used

- Python
- NumPy
- Matplotlib
- Seaborn

## How to Run

1. Install the required libraries:
pip install numpy matplotlib seaborn

Run the script using Python:
python temperature_analysis.py
Sample Output
Printed minimum, maximum, and average temperatures for each month
KDE plot showing the distribution of temperatures across the year

File Structure
temperature_analysis.py    # Main Python script
README.md                  # Project documentation
License
This project is licensed under the MIT License.

Author
Mian Saib
GitHub: https://github.com/Miansaibx7
