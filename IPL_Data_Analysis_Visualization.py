import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("IPL_dataset.csv")

top_batsman = df.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False).head(5)
print(top_batsman)

top_batsman.plot(kind="bar")
plt.title("Top 5 batsman")
plt.xlabel("match_id")
plt.ylabel("Runs")
plt.show()

match_runs = df.groupby("match_id")["total_runs"].sum()
print(match_runs)

plt.plot(match_runs.head(50))
plt.title("Runs per Match")
plt.xlabel("Match ID")
plt.ylabel("Runs")
plt.show()

top_teams = df.groupby("batting_team")["total_runs"].sum().sort_values(ascending=False).head(5)
print(top_teams)

top_teams.plot(kind='pie', autopct='%1.1f%%')
plt.title("Top Teams Contribution")
plt.ylabel("")
plt.show()


plt.hist(match_runs, bins=20)
plt.title("Distribution of Match Scores")
plt.xlabel("Runs")
plt.ylabel("Frequency")
plt.show()