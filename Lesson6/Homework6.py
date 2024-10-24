#1
# m = [ [1, 2, 3], [1, 4, 3], [10, 2, 3], [11, 2, 3], ]
# mx = 0

# for i in range(len(m)):
#     s = 0
#     for j in range(len(m[0])):
#         s += m[i][j]
#     mx = max(s, mx)
# print(mx)

#2
m = [ [1, 2, 3], [1, 4, 3], [10, 2, 3], [11, 3, 3], ]

for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == min(m[i]) and m[i][j] % 2 == 0: m[i][j] = 0
        elif m[i][j] == min(m[i]) and m[i][j] % 2 == 1: m[i][j] = 1
print(m)