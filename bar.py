import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
fig=px.bar(df,x="Avg Rating",y="Mobile Brand")
fig.show()