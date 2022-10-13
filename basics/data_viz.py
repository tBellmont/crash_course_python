import plotly.express as px
import pandas as pd

df = pd.read_csv('/Users/tombellmont/Documents/Python Scripts/movies.csv')

df = df[['Film', 'Genre', 'Lead Studio', 'Rotten Tomatoes %', 'Worldwide Gross','Year']]
df = df.groupby(['Year'],as_index=False)['Worldwide Gross'].sum()

fig = px.bar(df, x='Year', y='Worldwide Gross')
fig.show()