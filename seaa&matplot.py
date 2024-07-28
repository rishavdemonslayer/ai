import seaborn as sns
import pandas as pd
iris=sns.load_dataset("iris")
print(iris)
sns.displot(iris["sepal_length"],kde=True) 
sns.pairplot(iris)
sns.set_style("whitegrid")
sns.barplot(x=["A", "B", "C"], y=[20, 10, 30])
sns.set_style("darkgrid", {"grid.color": ".6", "grid.linestyle": ":"})
sns.boxplot(x="species",y="sepal_length",data=iris)
sns.countplot(x="sepal_length",data=iris )
penguin=sns.load_dataset('penguins')
sns.swarmplot(data=penguin, x="island", y="body_mass_g",color='black')
sns.violinplot(data=penguin, x="island", y="body_mass_g")
numeric_cols = penguin.select_dtypes(include=['number'])
iland_correlation = numeric_cols.corr()
sns.heatmap(iland_correlation,annot=True,cmap='coolwarm')


#matplotlib
# Import Libraries
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Enable inline plotting for Jupyter notebooks


# Read Data
df = pd.read_csv('selling.csv')

# Descriptive Statistics
mean_value = df.mean()
print('Mean Value:', mean_value)

median_value = df.median()
print('Median Value:', median_value)

mode_value = df.mode().iloc[0]
print('Mode Value:', mode_value)

std_deviation = df.std()
print('Standard Deviation:', std_deviation)

variance = df.var()
print('Variance:', variance)

percentile_95 = df.quantile(0.95)
print('95th Percentile:', percentile_95)

# Generate Random Values
bd = np.random.uniform(0, 10, 350)
print('Generated Values:', bd)

# Visualizations
# Bar plot of 'Kms Driven' vs. 'Selling Price' using Seaborn
sns.barplot(x='Kms Driven', y='Selling Price', data=df)
plt.show()

# Bar plot of 'Kms Driven' vs. 'Selling Price' with 'Year' as hue using Seaborn
sns.barplot(x='Kms Driven', y='Selling Price', hue='Year', data=df)
plt.show()

# Histogram of 'Selling Price' using Matplotlib
plt.hist(df['Selling Price'])
plt.show()

# Histogram of 'Selling Price' with 5 bins using Matplotlib
plt.hist(df['Selling Price'], bins=5)
plt.show()

# Box plot of 'Selling Price' using Seaborn
sns.boxplot(y='Selling Price', data=df)
plt.show()

# Scatter plot of 'Selling Price' vs. 'Kms Driven' using Matplotlib
plt.scatter(df['Kms Driven'], df['Selling Price'])
plt.xlabel('Kms Driven')
plt.ylabel('Selling Price')
plt.show()

# Pair plot of the entire DataFrame using Seaborn
sns.pairplot(df)
plt.show()

# Heatmap with annotations using Seaborn
features_of_interest = df[['Selling Price', 'Kms Driven', 'Year']]
correlation_matrix = features_of_interest.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.show()
