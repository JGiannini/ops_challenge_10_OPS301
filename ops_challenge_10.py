#!/usr/bin/env python3

# Author: Jamie Giannini

# Objectives: Using file handling commands, create a Python script that does the following: 
# [X] Creates a new .txt file
# [X] Appends three lines
# [X] Prints to the screen the first line
# [X] Then deletes the .txt file

import os #for deletion

def create_file():
    #Open function takes two arguments: file to open, string for permissions/operations to do to file
    groovy_file = open("groovy_gorilla.txt", "w+") #w means write to file, + means read and write

    #For loop with range of 3, writes to file then %d displays integer value each on a new line 
    groovy_gorillas = 3
    groovy_file.write("There are " + str(groovy_gorillas) + " Groovy Gorillas in here: \n")
    for i in range(groovy_gorillas):
        groovy_file.write("Groovy Gorilla %d\n" % (i+1))

    #Then we close the instance of the file because changes made to a file may not show until it's closed.
    groovy_file.close() 

    open_print_file()


#Opens file and prints content to screen
def open_print_file():
    groovy_file=open("groovy_gorilla.txt", "r") #Opens file in read mode

    #Prints first line only
    print("Printing the first line in the file...\n")
    number_of_lines_to_print = 1
    for i in range(number_of_lines_to_print):
        line = groovy_file.readline()
        print(line)
    
    delete_file()

#Gets user input and deletes file based on input 
def delete_file():
    t = True
    while t:
        get_name = input("Enter file name to delete or [q] to quit: \n")
        if os.path.exists(get_name):
            os.remove(get_name)
            print(get_name + " has been successfully deleted")
            break
        elif get_name == "q" or get_name == "Q":
            break
        else:
            print("Can't find " + get_name + "...please try again\n") 

# main
create_file()

