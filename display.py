from read import movie_list
dict = movie_list()
print("Movie ID \t Movie Name \t\t\t\t\t\t\t\t\t\t\t\t\t\t Price")
for key, value in dict.items():
    print(key, '\t', value[0],'\t\t\t\t\t\t\t\t\t\t\t\t', value[2])

