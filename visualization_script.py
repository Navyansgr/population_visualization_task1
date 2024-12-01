import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('population_data.csv', skiprows=4)

# Filter for selected countries
selected_countries = ['India', 'China', 'United States', 'Brazil', 'Nigeria']
filtered_data = data[data['Country Name'].isin(selected_countries)]

# Select relevant years (1960-2020)
years = [str(year) for year in range(1960, 2021, 10)]
filtered_data = filtered_data[['Country Name'] + years]

# Transpose the data for visualization
filtered_data.set_index('Country Name', inplace=True)
filtered_data = filtered_data.transpose()

# Convert population to billions
filtered_data = filtered_data / 1e9

# Plot the data
plt.figure(figsize=(12, 6))
filtered_data.plot(kind='bar', figsize=(14, 7))
plt.title('Population Trends of Selected Countries (1960-2020)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Population (in Billions)', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Country', fontsize=12)
plt.tight_layout()

# Save the chart as an image
plt.savefig('population_chart.png')
print("Chart saved as 'population_chart.png'.")

# Show the chart
plt.show()