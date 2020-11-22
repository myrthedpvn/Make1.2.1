#!/usr/bin/env python

"""
Een script dat als output het aantal tekens geeft van de ingegeven string.
Het script vraagt om een willekeurig woord in te geven en geeft als output het aantal tekens terug.
 """

# imort

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def main():

    words = input("Give me a word\n")                                    #To ask the user for a word
    print(len(words))                                                    #To print out the lenght of the word

if __name__ == '__main__':  # code to execute if called from command-line
    main()
