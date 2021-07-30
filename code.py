import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

student_df=df.loc[df['student_id']=="TRL_zny"]

print(student_df.groupby("level")["attempt"].mean())

fig = px.scatter(df, x=student_df.groupby("level")["attempt"].mean(), y=['level 1','level 2','level 3','level 4'],
	          orientation='h'
                   )
fig.show()
