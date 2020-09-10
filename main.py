print("Welcome to Movie Rental")
print('\n')
choose1 = True
while choose1 == True:
    print("\n")
    print("Enter 1 to view movies.")
    print("Enter 2 to Borrow movies.")
    print("Enter 3 to return Borrowed movies.")
    print("Enter 4 to exit.")
    print("\n")
    choose = int(input("Hello! Please enter an option: "))



    if choose == 1:
        import display
    elif choose == 2:
        import display
        from read import movie_list

        name = input("Enter your name: ")
        dict = movie_list()  # return the value of movielist in dict
        number_movies = int(input("Enter the number of mmovies you want to borrow: "))
        name = input("Enter your name: ")
        dict2 = {}
        dict3={}
        total = 0
        from borrowfunc import borr_func
        borr_func(number_movies, dict2, name)
        print(dict2)
        print(dict)
    elif choose == 3:
        import display
        from read import movie_list

        name = input("Enter name: ")
        booksDays = int(input("Enter the days of movies borrowed: "))
        dict = book_list()
        number_books = int(input("Enter the number of movies to return: "))
        dict3 = {}
        dict2={}
        total2 = 0
        from returnfunc import retu_func
        retu_func(dict, number_movies, dict3)
        print(dict3)
        print(dict)
        print("Completed")

    elif choose == 4:
        print(dict)
        file = open("store.txt", "w")
        for key, value in dict.items():
            file.write(key)
            for each_items in value:
                file.write(",")
                file.write(str(each_items))
            file.write("\n")

        for i in range(len(dict2)):
            if i > 0:
                from write import write_borrow
                write_borrow(dict2, name, total)
                #from calculation import calculation
                #dict4 = calculation()
                #print(dict4)
        for i in range(len(dict3)):
            if i > 0:
                from write import write_return
                write_return(dict3, name, moviesDays, total2)

        exit()
    else:
        print("Invalid option and try again!!")




