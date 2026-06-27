#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv('Unemployment in India.csv')

# 2. Data Cleaning
# Strip leading/trailing whitespaces from column names
df.columns = df.columns.str.strip()

# Drop rows that contain entirely missing/null values
df = df.dropna()

# Clean and convert 'Date' column to a proper datetime object
df['Date'] = pd.to_datetime(df['Date'].str.strip(), format='%d-%m-%Y')

# Extract Month and Year for easier breakdown
df['Year'] = df['Date'].dt.year
df['Month_Name'] = df['Date'].dt.strftime('%b')

print("--- Cleaned Dataset Sample ---")
print(df.head())

# 3. Exploratory Data Analysis & Covid-19 Impact Analysis
print("\n--- Average Unemployment Rate by Area ---")
print(df.groupby('Area')['Estimated Unemployment Rate (%)'].mean())

print("\n--- Top 5 Regions with Highest Average Unemployment Rates ---")
top_regions = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False).head(5)
print(top_regions)

# 4. Visualizations
sns.set_theme(style="whitegrid")

# Plot 1: Timeline Trend showing Covid-19 Shockwave (April-May 2020 Lockdowns)
plt.figure(figsize=(10, 5))
timeline = df.groupby(['Date', 'Area'])['Estimated Unemployment Rate (%)'].mean().unstack()
timeline.plot(ax=plt.gca(), marker='o', linewidth=2)
plt.title('Monthly Mean Unemployment Rate (%) in India (Rural vs Urban)', fontsize=14, fontweight='bold')
plt.ylabel('Unemployment Rate (%)', fontsize=12)
plt.xlabel('Timeline', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('unemployment_timeline_trend.png')
plt.show()

# Plot 2: Regional Impact Comparison
plt.figure(figsize=(12, 6))
sns.barplot(
    x='Estimated Unemployment Rate (%)', 
    y='Region', 
    data=df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().reset_index().sort_values('Estimated Unemployment Rate (%)', ascending=False),
    hue ='Region',
    legend ='auto',
    palette='viridis'
)
plt.title('Average Unemployment Rate (%) across Indian States/Regions', fontsize=14, fontweight='bold')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Region / State')
plt.tight_layout()
plt.savefig('regional_unemployment.png')
plt.show()


# In[ ]:




