# file=open('text.txt')

# # for line in file:
# #     print(line )

# # file.seek(0)

# # linelists=file.readline()
# # print(linelists)


# file.seek(50)

# paragraph=file.read(20)
# print(paragraph);

# file.close()

with open('text.txt') as file:
    # for line in file:
    #     print(line);
    file.seek(50)
    paragraph=file.read(15)
    print(paragraph)