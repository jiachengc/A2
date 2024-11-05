import numpy as np

# Data values from jEdit metrics
values = [
    23858, 459, 5854, 5313, 67814, 121034, 85940, 4875, 257
]

# Calculating descriptive statistics
mean_value = np.mean(values)
q1 = np.percentile(values, 25)
median_value = np.median(values)
q3 = np.percentile(values, 75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Identifying outliers
outliers = [value for value in values if value < lower_bound or value > upper_bound]

# Printing the descriptive statistics
print(f"Mean: {mean_value:.2f}")
print(f"First Quartile (Q1): {q1:.2f}")
print(f"Median (Q2): {median_value:.2f}")
print(f"Third Quartile (Q3): {q3:.2f}")
print(f"Interquartile Range (IQR): {iqr:.2f}")
print(f"Lower Bound: {lower_bound:.2f}")
print(f"Upper Bound: {upper_bound:.2f}")
print(f"Outliers: {outliers}")

