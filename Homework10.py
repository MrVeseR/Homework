import pandas as pd
import matplotlib.pyplot as plt

# 1 (3)
# ser = pd.Series([1, 2, 3, 4, 3, 4, 4, 5, 5, 5, 5])
# uniValues = ser.value_counts()
# print(type(uniValues))
# plt.bar(uniValues.index, uniValues.values)
# plt.show()

# 2 (4)
# df1 = pd.DataFrame({"one" : [1, 2, 43, 21, 21], "two" : [23, 324, 546, 11, 90]})
# df2 = pd.DataFrame({"three" : [1, 2, 43, 21, 4], "one" : [23, 324, 4, 11, 90]})

# dfOb1 = pd.concat([df1, df2])
# print(dfOb1)
# dfOb2 = pd.concat([df1, df2], axis=1)
# print(dfOb2)

# 3 (5)
# df = pd.DataFrame({"one" : [1, 2, 43, 21, 21], "two" : [23, 324, 546, 11, 90]})
# plt.plot(df["one"], df["two"])
# plt.show()