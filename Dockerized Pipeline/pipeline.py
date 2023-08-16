import pandas as pd
data = [{"Country": "USA", "Population": 328200000, "GDP": 21439400, "Unemployment": 3.8},{"Country": "China", "Population": 1393000000, "GDP": 14342920, "Unemployment": 3.6},{"Country": "Japan", "Population": 126500000, "GDP": 5082465, "Unemployment": 2.4},{"Country": "Germany", "Population": 82790000, "GDP": 3845481, "Unemployment": 3.4},{"Country": "India", "Population": 1354000000, "GDP": 2956756, "Unemployment": 6.1},{"Country": "France", "Population": 66990000, "GDP": 2930535, "Unemployment": 8.0},{"Country": "United Kingdom", "Population": 66440000, "GDP": 2825208, "Unemployment": 4.1},{"Country": "Italy", "Population": 60480000, "GDP": 2086911, "Unemployment": 9.9},{"Country": "Brazil", "Population": 209300000, "GDP": 1868626, "Unemployment": 11.6},{"Country": "Canada", "Population": 37590000, "GDP": 1673625, "Unemployment": 5.6},{"Country": "South Korea", "Population": 51310000, "GDP": 1660119, "Unemployment": 3.9},{"Country": "Australia", "Population": 25200000, "GDP": 1403313, "Unemployment": 5.2},{"Country": "Russia", "Population": 144500000, "GDP": 1402081, "Unemployment": 4.8},{"Country": "Spain", "Population": 46560000, "GDP": 1394215, "Unemployment": 14.1},{"Country": "Mexico", "Population": 126200000, "GDP": 1212294, "Unemployment": 3.3},{"Country": "Indonesia", "Population": 267700000, "GDP": 1075216, "Unemployment": 5.3},{"Country": "Netherlands", "Population": 17430000, "GDP": 909887, "Unemployment": 3.6},{"Country": "Saudi Arabia", "Population": 33699947, "GDP": 793697, "Unemployment": 12.9},{"Country": "Turkey", "Population": 82003882, "GDP": 754605, "Unemployment": 11.1},{"Country": "Switzerland", "Population": 8541000, "GDP": 703080, "Unemployment": 2.6},{"Country": "Nigeria", "Population": 214000000, "GDP": 448120, "Unemployment": 23.1}]

df = pd.DataFrame(data)
highest_population = df.loc[df['Population'].idxmax(),'Country']
average_GDP = round(df.loc[:, 'GDP'].mean(),2)
lowest_unemployment = df.loc[df['Unemployment'].idxmin(),'Country']
sorted_df = df.sort_values(by='GDP', ascending=False)
top5= sorted_df.head(5)
top5_total_pop = top5['Population'].sum()
cnt_high_gdp = (df.loc[df['GDP']>= 5000000,'Country']).count()
lowest_gdp = df.loc[df['GDP'].idxmin(),'Country']
print(
f""""My name is Abdulmujib, and here are my answers:
1. Country with the highest population: {highest_population} 
2. Average GDP across all countries: {average_GDP} 
3. Country with the lowest unemployment rate: {lowest_unemployment} 
4. Total population of the top 5 countries by GDP: {top5_total_pop} 
5. Number of countries with a GDP higher than 5 trillion: {cnt_high_gdp}
6. Country with the lowest GDP per capita: {lowest_gdp}"""
)