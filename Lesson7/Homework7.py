# 1
#  def read_last(lines, file):
#     f = open(file, encoding='utf-8').readlines()
#     for i in range(1, lines + 1):
#         i = -1 * i
#         print(f[i])

# read_last(3, "Lesson7/article.txt")

# 2
# def print_dir(dir):
#     import os
#     #s = list(os.listdir(dir))
#     for i in os.walk(dir):
#         print(i)

# print_dir(r"C:/MyCode")

# 3
# def longest_words(file):
#     f = open(file, encoding="utf-8").readlines()
#     mx = 0
#     slova = []

#     for i in f:
#         i = i.split()
#         for j in i:
#             mx = max(mx, len(j))

#     for i in f:
#         i = i.split()
#         for j in i:
#             if len(j) == mx:
#                 slova.append(j)
#     print(mx, slova)

# longest_words("Lesson7/article.txt")

# 4
# name = input("введите название файла \n")
# f = open(f"Lesson7/{name}.txt", "w+", encoding="utf-8")

# print("введите строку для записи, enter для перехода на следующую строку, 1 для закрытия")
# while True:
#     s = input()
#     if s == "1":
#         f.close()
#         break
#     f.write(s + "\n")