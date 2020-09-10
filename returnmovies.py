from read import movie_list  # import the function from read.py
dict = movie_list() # return the value of booklist in dict

name = input("Enter name: ")
return_books = int(input("Enter the number of movies you want to return: "))
file5 = open("returnBooks.txt", "a+")
file5.write("Name: ")
file5.write(name)
file5.write("\n")
file5.write("Movie Name \t\t\t\t\t\t\t\t Days Borrowed \t\t\t\t\t\t Price")
file5.write("\n")
total = 0
dict3 = {}
def ret_func(return_movies, dict,total):
    for i in range(return_books):
        choose = input("Enter the movies ID: ")
        for key, value in dict.items():
            if choose == key:
                file5.write("\n")
                file5.write(value[0])
                file5.write("\t\t\t\t\t\t\t\t")
                file5.write(str(return_books))
                file5.write("\t\t\t\t\t\t\t\t")
                file5.write(value[3])
                if return_movies > 10:
                    fine_days = return_mmovies-10
                    fine_amount = 0.1*float(value[3])
                    total_fine = fine_amount*fine_days
                else:
                    total_fine = 0
                file5.write("\n")
                file5.write("Fine")
                file5.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
                file5.write(str(total_fine))
                total = total+(total_fine+float(value[3]))
                value[2] = int(value[1]) + 1
                dict3[key] = value
    file5.write("\n")
    file5.write("________________________________________________________________________")
    file5.write("\n")
    file5.write("Total\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    file5.write(str(total))
    file5.close()

    return(file5.write,dict3)

ret_func(return_movies, dict,total)
'''
for i in range(return_number):
    book_id = input("Enter the book ID: ")
    for key, value in dict.items():  # iterate through each key and value
        if book_id == key:
            value[2] = int(value[2]) + 1
            dict3[key] = value
print(dict3)
'''
