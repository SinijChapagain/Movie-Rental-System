from read import movie_list
name = input("Enter your name: ")
dict = movie_list()  # return the value of movielist in dict
number_movies = int(input("Enter the number of movies you want to borrow: "))
file4 = open("borrow.txt", "a+")
file4.write("Name: ")
file4.write(name)
file4.write("\n")
file4.write("Movies Name \t\t\t\t\t\t\t\t Price")
file4.write("\n")
dict2 = {}
total = 0

def borr_func(number_movies, dict,total):



    for i in range(number_movies):
        movie_id = input("Enter the movie ID: ")
        for key, value in dict.items():
            if movie_id == key:
                if int(value[2]) >= 1:
                    file4.write("\n")
                    file4.write(value[0])
                    file4.write("\t\t\t\t\t\t\t")
                    file4.write(value[2])
                    value[2] = float(value[2])
                    total = total+value[2]
                    value[2] = str(value[2])
                    value[1] = float(value[1]) - 1
                    dict2[key] = value
                else:
                    print("Sorry " + name + " We don't have " + value[0] + " movie today!!")

    file4.write("\n")
    file4.write("***********************************************************************")
    file4.write("\n")
    file4.write("Total\t\t\t\t\t\t\t\t\t\t")
    file4.write(str(total))
    file4.close()

    return(file4.write,dict2)
borr_func(number_movies, dict,total)
print(dict2)

