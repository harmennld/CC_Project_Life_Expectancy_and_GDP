import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('all_data.csv')
print(df.head())

countries = df['Country'].unique()
countries[countries == 'United States of America'] = "USA"

fig, ax = plt.subplots(1, 2, figsize=(12,4))
for country in countries:
    ax[0].plot(df['Year'].where(df['Country'] == country), df['Life expectancy at birth (years)'])

ax[0].set_xlabel('Year')
ax[0].set_ylabel('Age')
ax[0].set_title('Life expectancy at birth (years)')


for country in countries:
    ax[1].plot(df['Year'].where(df['Country'] == country), df['GDP']/1000000000000)

ax[1].set_xlabel('Year')
ax[1].set_ylabel('x $1.000.000.000.000')
ax[1].set_title('Gross domestic product (GDP)')

fig.legend(labels=countries, loc="upper left")
plt.subplots_adjust(left=0.18)
plt.show()