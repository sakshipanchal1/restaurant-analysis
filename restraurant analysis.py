import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Step 1: Simulate Restaurant & Food Delivery Dataset
np.random.seed(42)
n_restaurants = 250

cuisines = ['North Indian', 'South Indian', 'Chinese', 'Fast Food', 'Italian', 'Bakery']
price_ranges = ['Budget', 'Mid-Range', 'Fine Dining']

data = {
    'Restaurant_ID': range(101, 101 + n_restaurants),
    'Cuisine': np.random.choice(cuisines, n_restaurants),
    'Price_Range': np.random.choice(price_ranges, n_restaurants, p=[0.5, 0.35, 0.15]),
    'Rating': np.random.uniform(2.8, 4.9, n_restaurants).round(1),
    'Votes': np.random.randint(10, 1200, n_restaurants),
    'Online_Delivery': np.random.choice(['Yes', 'No'], n_restaurants, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# Step 2: Data Analysis & Insights
print('--- Restaurant Dataset Preview ---')
print(df.head())

print('\n--- Average Rating by Cuisine Type ---')
cuisine_summary = df.groupby('Cuisine')['Rating'].mean().round(2)
print(cuisine_summary)

print('\n--- Popularity (Avg Votes) by Delivery Availability ---')
delivery_summary = df.groupby('Online_Delivery')['Votes'].mean().round(2)
print(delivery_summary)

# Step 3: Data Visualization
plt.figure(figsize=(10, 4))

# Chart 1: Average Rating by Cuisine
plt.subplot(1, 2, 1)
cuisine_summary.plot(kind='bar', color='coral')
plt.title('Average Rating by Cuisine')
plt.ylabel('Avg Rating')
plt.xticks(rotation=45)

# Chart 2: Count of Restaurants by Price Range
plt.subplot(1, 2, 2)
df['Price_Range'].value_counts().plot(kind='bar', color='mediumseagreen')
plt.title('Restaurant Count by Price Range')
plt.ylabel('Count')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig('restaurant_analysis_chart.png')
print('\n[Success] Analysis complete! Chart saved as "restaurant_analysis_chart.png".')
