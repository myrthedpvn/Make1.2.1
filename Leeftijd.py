#!/usr/bin/env python

"""
1. Vraagt achter je leeftijd
2. Berekent in welk jaar je geboren bent en dat ook als output meegeeft
3. Berekent in welk jaar je 50 jaar zal zijn en dat ook als output meegeeft
 """

# import


__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def main():

    age  = int(input("What is your age?\n"))                                    #To know what age the person is
    print(f" You were born in the year {2020 - age}.\n")                        #To find out what year they were born
    print(f" You will be 50 in the year {2020 - age + 50}. ")                   #To know in what year they will be 50



if __name__ == '__main__':  # code to execute if called from command-line
    main()
