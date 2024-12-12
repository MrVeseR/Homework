import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Mall_Customers.csv", sep=",")

# 1 (4)
# maleDf = df[df["Genre"] == "Male"]
# maleDf = maleDf.sort_values("Age")
# plt.plot(maleDf["Age"], maleDf["Annual Income (k$)"])
# plt.show()


# 2 (5)
# maleDf = df[df["Genre"] == "Male"]
# femaleDf = df[df["Genre"] == "Female"]

# plt.bar(maleDf["Annual Income (k$)"], maleDf["Spending Score (1-100)"], color = "Blue")
# plt.bar(femaleDf["Annual Income (k$)"], femaleDf["Spending Score (1-100)"], color = "Red")
# plt.show()