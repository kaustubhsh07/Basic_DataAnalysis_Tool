import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV file
file_path = r"C:\Users\kaust\Downloads\data.csv"  # Use raw string notation to handle backslashes
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Perform basic analysis
print("\nBasic Analysis:")
for column in data.select_dtypes(include=np.number):  # Only consider numeric columns
    mean = data[column].mean()  # Corrected mean calculation using pandas
    median = data[column].median()  # Corrected median calculation using pandas
    mode = data[column].mode()[0]  # Pandas mode() returns a Series; get the first mode
    
    print(f"\nColumn: {column}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")

# Visualization
plt.figure(figsize=(10, 6))
for column in data.select_dtypes(include=np.number):
    plt.hist(data[column], bins=15, alpha=0.5, label=column)

plt.title("Histogram of Numeric Columns")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

