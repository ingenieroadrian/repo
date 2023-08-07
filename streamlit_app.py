import matplotlib.pyplot as plt
import pandas as pd

# Load the data
df = pd.read_csv("data.csv")

# Create a bar chart of the number of titles won by each player
plt.bar(df["Player"], df["Titles"])
plt.xlabel("Player")
plt.ylabel("Titles")
plt.title("Number of Titles Won by Each Player in 2022")
plt.show()

# Create a line chart of the player rankings over the course of the season
plt.plot(df["Date"], df["Ranking"])
plt.xlabel("Date")
plt.ylabel("Ranking")
plt.title("Player Rankings Over the Course of the 2022 Season")
plt.show()

# Create a scatter plot of the player's service and return percentages
plt.scatter(df["Service Percentage"], df["Return Percentage"])
plt.xlabel("Service Percentage")
plt.ylabel("Return Percentage")
plt.title("Player's Service and Return Percentages in 2022")
plt.show()

