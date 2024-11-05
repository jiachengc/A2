import matplotlib.pyplot as plt

# Data from the screenshot for PDFSam-core metrics
metrics_pdfsam = {
    'Metric': [
        'McCabe Cyclomatic Complexity', 'Weighted methods per Class', 'Number of Static methods',
        'Total lines of code', 'Method lines of code', 'Class Interface Size'
    ],
    'Values': [
        1.104, 597, 30, 3719, 1241, 430
    ]
}

# Creating box plot for PDFSam-core metrics
plt.figure(figsize=(10, 6))

plt.boxplot(metrics_pdfsam['Values'], patch_artist=True)
plt.title('Box Plot for PDFSam-core Metrics')
plt.ylabel('Metric Values')
plt.xticks([1], ['PDFSam-core Metrics'])
plt.grid(axis='y')

# Scatter plot to show the mean value
mean_value_pdfsam = sum(metrics_pdfsam['Values']) / len(metrics_pdfsam['Values'])
plt.scatter(1, mean_value_pdfsam, color='red', label=f'Mean Value: {mean_value_pdfsam:.2f}')

plt.legend()
plt.show()
