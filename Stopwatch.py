#!/usr/bin/env python

"""
 Een python script dat de functie van een stopwatch heeft.
 """

# import
import time

__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

input("Press Enter to start")
start_time = time.time()                                                    #To start counting once start was pressed

input("Press Enter to stop")
end_time = time.time()                                                      #To stop counting once stop was pressed



time_lapsed = end_time - start_time
time_convert(time_lapsed)

if __name__ == '__main__':  # code to execute if called from command-line
    time_convert()
