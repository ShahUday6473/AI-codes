import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Load and scale the Iris dataset
iris = load_iris()
data_scaled = StandardScaler().fit_transform(iris.data)  # Combine scaling into one line

# Apply PCA to reduce dimensions to 2 principal components
principal_components = PCA(n_components=2).fit_transform(data_scaled)

# Create DataFrame directly with target for plotting
pca_data = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
pca_data['Target'] = iris.target

# Plot PCA result
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PC1', y='PC2', hue='Target', palette='viridis', data=pca_data)
plt.title("PCA of Iris Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

# Display explained variance ratio
explained_variance = PCA(n_components=2).fit(data_scaled).explained_variance_ratio_
print("Explained Variance Ratio of each Principal Component:", explained_variance)
print("Total Explained Variance (2 components):", explained_variance.sum())
