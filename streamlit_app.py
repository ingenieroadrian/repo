import pandas as pd
import matplotlib.pyplot as plt

# Import the ATP match data for the 2021-2022 season
df = pd.read_csv("atp_matches_2021_2022.csv")

# Select the players from the top 10 positions on ATP
top_10_players = df["winner_name"].value_counts()[:10].index

# Create a heat map for each player
for player in top_10_players:
    # Get the player's match data
    player_df = df[df["winner_name"] == player]

    # Create a heat map of the player's wins and losses by surface
    plt.imshow(player_df["surface"].value_counts().to_numpy(), cmap="hot")
    plt.title(player)
    plt.show()

