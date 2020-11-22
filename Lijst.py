#!/usr/bin/env python

"""
 Programma dat een voorgeprogrammeerde lijst weergeeft.
 Daarna om een willekeurig aantal woorden vraagt en deze ook in een lijst steekt en weergeeft.
 """

# import


__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def main():
    list1 = ["It's , Christmas , time"]                                             #The list with my chosen words
    print(list1)                                                                    #To print out list1
    words = input("Give me some words\n")                                           #To ask for random words

    list2 = []                                                                      #To create an new list

    list2.append(words)                                                             #To put the words in the list2
    print(list2)                                                                    #To print out list2

if __name__ == '__main__':  # code to execute if called from command-line
    main()
