import numpy as np

# Data values from PDFSam-core metrics
values_pdfsam = [
    1.104, 597, 30, 3719, 1241, 430
]

# Calculating descriptive statistics for PDFSam-core
mean_value_pdfsam = np.mean(values_pdfsam)
q1_pdfsam = np.percentile(values_pdfsam, 25)
median_value_pdfsam = np.median(values_pdfsam)
q3_pdfsam = np.percentile(values_pdfsam, 75)
iqr_pdfsam = q3_pdfsam - q1_pdfsam
lower_bound_pdfsam = q1_pdfsam - 1.5 * iqr_pdfsam
upper_bound_pdfsam = q3_pdfsam + 1.5 * iqr_pdfsam

# Identifying outliers for PDFSam-core
outliers_pdfsam = [value for value in values_pdfsam if value < lower_bound_pdfsam or value > upper_bound_pdfsam]

# Printing the descriptive statistics for PDFSam-core
print(f"Mean: {mean_value_pdfsam:.2f}")
print(f"First Quartile (Q1): {q1_pdfsam:.2f}")
print(f"Median (Q2): {median_value_pdfsam:.2f}")
print(f"Third Quartile (Q3): {q3_pdfsam:.2f}")
print(f"Interquartile Range (IQR): {iqr_pdfsam:.2f}")
print(f"Lower Bound: {lower_bound_pdfsam:.2f}")
print(f"Upper Bound: {upper_bound_pdfsam:.2f}")
print(f"Outliers: {outliers_pdfsam}")
