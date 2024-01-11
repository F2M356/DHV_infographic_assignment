#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('nuclear_power_generation.csv')


# # Display basic information about the dataset

print(data.info())

# Summary statistics

print(data.describe())

# Adding Title, Name and ID
name = "Mahdin"
id = " Student ID : 22055871"
headline = "Nuclear Power Generation"


# Adding Explanation

explain_plot1 = "Plot-1 : Operational status is high compare to other which is count 340"
explain_plot2 = "Plot-2 : Under Construction status is 32.2% which is Low"
explain_plot3 = "Plot-3 : It highlight the frequency of verious capacity range"
explain_plot4 = "Plot-4 : Middle of 2005 to 2010 the Capacity had peak"


# DASHBOARD
# Create a figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.patch.set_facecolor('#F0F0F0')  # Set background color to a light gray

# Visualization 1: Bar plot - Power Plant Status
# Using pastel colors
sns.countplot(x='Status', data=data, ax=axs[0, 0], palette='pastel')
# Align title to the left
axs[0, 0].set_title('Power Plant Status', loc='left')

# Visualization 2: Pie plot - Status Distribution
status_counts = data['Status'].value_counts()
axs[0, 1].pie(status_counts, labels=status_counts.index, autopct='%1.1f%%',
              startangle=90, colors=sns.color_palette('Set2'))  # Using Set2 colors
axs[0, 1].legend(bbox_to_anchor=(1, 1), loc='upper left',
                 labels=status_counts.index)
# Align title to the right
axs[0, 1].set_title('Status Distribution', loc='right')

# Visualization 3: Histogram - Distribution of Power Plant Capacity
sns.histplot(data['Capacity_MW'], bins=20, kde=True,
             ax=axs[1, 0], color='skyblue')  # Using a sky blue color
axs[1, 0].set_title('Distribution of Power Plant Capacity',
                    loc='center')  # Align title to the center
axs[1, 0].set_xlabel('Capacity (MW)')
axs[1, 0].set_ylabel('Frequency')

# Visualization 4: Line plot - Commission Year vs. Capacity
data['Commission_Date'] = pd.to_datetime(
    data['Commission_Date'])  # Convert Commission_Date to datetime
# Extract year from Commission_Date
data['Commission_Year'] = data['Commission_Date'].dt.year
sns.lineplot(x='Commission_Year', y='Capacity_MW', data=data,
             ax=axs[1, 1], marker='o', color='orange')  # Using an orange color
axs[1, 1].set_title('Commission Year vs. Capacity',
                    loc='right')  # Align title to the right
axs[1, 1].set_xlabel('Commission Year')
axs[1, 1].set_ylabel('Capacity (MW)')

# text explanations
plt.figtext(0.5, 0.91, f"{name}, {id}",
            ha='center', va='center', fontsize=14)
plt.figtext(0.5, 0.94, headline, ha='center',
            va='center', fontsize=18)
plt.figtext(0.1, 0.06, explain_plot1, ha='left', va='center', fontsize=13)
plt.figtext(0.1, 0.04, explain_plot2, ha='left', va='center', fontsize=13)
plt.figtext(0.1, 0.02, explain_plot3, ha='left', va='center', fontsize=13)
plt.figtext(0.1, 0.0, explain_plot4, ha='left', va='center', fontsize=13)

# Save the dashboard as an image
plt.savefig('22055871.png', dpi=300, bbox_inches='tight')
