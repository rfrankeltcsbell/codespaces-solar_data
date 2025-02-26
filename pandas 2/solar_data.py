import pandas as pd
import sqlite3 

# Connect to DB
conn = sqlite3.connect("./databases/db.sql")
cursor = conn.cursor()

# Load Datasets 
energy_df = pd.read_csv('./data/energy.csv')
weather_df = pd.read_csv('./data/weather.csv')

# See the first 5 rows 
print("Energy_Sample:")
example = energy_df.head()
print(example)

# Statistics for the energy
energy_mean = energy_df.mean()
energy_median = energy_df.median()
energy_std = energy_df.std()

# Statistics for the weather
weather_mean = weather_df.mean()
weather_median = weather_df.median()
weather_std = weather_df.std()

# Store results into a DataFrame 
stats_df = pd.DataFrame({
    'Energy_Mean': energy_mean,
    'Energy_Median': energy_median,
    'Energy_STD': energy_std,
    'Weather_Mean': weather_mean,
    'Weather_Median': weather_median,
    'Weather_STD': weather_std
})
#Save Statistics to database
table_name='energy_weather_stats'
stats_df.to_sql(table_name,conn,if_exists='replaces',)