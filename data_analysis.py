import pandas as pd
import numpy as np

# Step 1: Load the CSV File
file_path = input("Enter the path to your CSV file: ")
try:
    data = pd.read_csv(file_path)
    print("\nCSV Data loaded successfully!")
    print(data.head())  # Display the first few rows to ensure it's read correctly
except Exception as e:
    print(f"Error reading the file: {e}")
    exit()  # Exit if file loading fails

# Step 2: Perform Basic Analysis
print("\nBasic Statistics:")
print(data.describe())

# Handle numeric-only columns for statistical calculations
numeric_data = data.select_dtypes(include=[np.number])

print("\nMean of each numeric column:")
print(numeric_data.mean())

print("\nMedian of each numeric column:")
print(numeric_data.median())

print("\nMode of each column:")
print(data.mode().iloc[0])

# Step 3: Save a Summary to a New File
output_path = "summary.csv"
try:
    numeric_data.describe().to_csv(output_path)
    print(f"\nSummary saved to {output_path}")
except Exception as e:
    print(f"Error saving the summary: {e}")


