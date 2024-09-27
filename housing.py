import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV Dosyasının Yüklenmesi
df = pd.read_csv('python/housing.csv')

# Area - Histogram
plt.figure(figsize=(10, 6))
plt.hist(df['area'], bins=30, edgecolor='k')
plt.title('Distribution of House Prices by Area')
plt.xlabel('Area')
plt.ylabel('Frequency')
plt.show()

# Bedrooms - Histogram
plt.figure(figsize=(10, 6))
plt.hist(df['bedrooms'], bins=30, edgecolor='k')
plt.title('Distribution of House Prices by Bedrooms')
plt.xlabel('Bedrooms')
plt.ylabel('Frequency')
plt.show()

# Stories - Histogram
plt.figure(figsize=(10, 6))
plt.hist(df['stories'], bins=30, edgecolor='k')
plt.title('Distribution of House Prices by Stories')
plt.xlabel('Stories')
plt.ylabel('Frequency')
plt.show()


# Bathroom sayısına göre ortalama fiyatlar
bathroom_mean = df.groupby('bathrooms')['price'].mean()

plt.figure(figsize=(10, 6))
bathroom_mean.plot(kind='bar')
plt.title('Average Price by Bathroom Count')
plt.xlabel('Bathrooms')
plt.ylabel('Average Price')
plt.show()

# Furnishingstatus'e göre ortalama fiyatlar
furnishing_mean = df.groupby('furnishingstatus')['price'].mean()

plt.figure(figsize=(10, 6))
furnishing_mean.plot(kind='bar')
plt.title('Average Price by Furnishing Status')
plt.xlabel('Furnishing Status')
plt.ylabel('Average Price')
plt.show()

# 4. Korelasyon Matrisi
plt.figure(figsize=(12, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Housing Data')
plt.show()
