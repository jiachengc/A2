import matplotlib.pyplot as plt

# Data from the screenshot for jEdit metrics
metrics = {
    'Metric': [
        'Weighted methods per Class', 'Number of Children', 'Number of Methods',
        'Number of Normal Methods', 'No of inherited methods', 'Total lines of code',
        'Method lines of code', 'Class interface size', 'Number of Polymorphic Methods'
    ],
    'Values': [
        23858, 459, 5854, 5313, 67814, 121034, 85940, 4875, 257
    ]
}

# Creating box plot for jEdit metrics
plt.figure(figsize=(10, 6))

plt.boxplot(metrics['Values'], patch_artist=True)
plt.title('Box Plot for jEdit Metrics')
plt.ylabel('Metric Values')
plt.xticks([1], ['jEdit Metrics'])
plt.grid(axis='y')

# Scatter plot to show the mean value
mean_value = sum(metrics['Values']) / len(metrics['Values'])
plt.scatter(1, mean_value, color='red', label=f'Mean Value: {mean_value:.2f}')

plt.legend()
plt.show()

