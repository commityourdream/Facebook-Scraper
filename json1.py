import pandas as pd
df = pd.read_json("data.json")
df = df.loc[["created_time", "message","id"]]
df.to_csv("pywu.cache.csv")
