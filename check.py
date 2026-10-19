import pandas as pd
import matplotlib.pyplot as plt
watchlist_df= pd.read_csv("watchlist.csv")
print(watchlist_df["code"].tolist())
