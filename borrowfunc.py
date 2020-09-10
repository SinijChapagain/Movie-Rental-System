def borr_func(dict,number_movies,dict2,name):
    for i in range(number_movies):
        movie_id = input("Enter the movie ID: ")
        for key, value in dict.items():
            if movie_id == key:
                if int(value[2]) >= 1:
                    value[2] = int(value[2]) - 1
                    dict2[key] = value
                else:
                    print("Sorry " + name + " We don't have " + value[0] + " movie today!!")
    return dict2,dict
