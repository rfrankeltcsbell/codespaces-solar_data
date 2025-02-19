import pandas as pd

energy_df=pd.read_csv('./data/energy.csv')
weather_df=pd.read_csv('./data/weather.csv')

energy_df.head()
# print (energy_df.head())

energy_mean=energy_df.mean()
energy_median=energy_df.median()
energy_std=energy_df.std()

# print (energy_mean)
# print(energy_median)
# print(energy_std)
example=energy_df.head()
# print (example.dtypes())
# print (energy_df.dtypes())


weather_mean=weather_df.mean()
weather_median=energy_df.median()
weather_std=weather_df.std()
