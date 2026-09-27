import pandas as pd
df = pd.read_csv("data/flight_log.csv")

print("最高高度：", df["altitude"].max())
print("平均高度", df["altitude"].mean())
print("最低电量", df["battery"].min())
print("超限次数",(df["altitude"] > 120).sum())