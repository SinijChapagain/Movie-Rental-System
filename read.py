# reading the  information stored in the file


def movie_list():
    # defining a function
    file = open("store.txt", 'r')  # reading the file from the text file store
    contents1 = file.read()
    list1 = contents1.split('\n')  # splitting '\n'
    list2 = []
    for each_item in list1:
        contents2 = each_item.split(',')  # splitting ','
        list2.append(contents2)
    dict1 = {}  # creating a empty dictionary
    for each_value in list2:  # iterating through each elements in the list2
        key = each_value[0]
        values = []
        for i in range(1, len(each_value)):  # iterating through each items from second items to the last item
            contents3 = (each_value[i])
            values.append(contents3)
        dict1[key] = values

    file.close()
    return dict1

