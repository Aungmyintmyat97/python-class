# import time
#
# class ShortInputException(Exception):
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
#
# class BadWordException(Exception):
#     def __init__(self, badword):
#         Exception.__init__(self)
#         self.badword = badword
#
# badwords = ('fuck', 'bitch', 'cyka', 'naxui')
#
# try :
#     text = input("Enter a string : ").strip(' ')
#     if len(text) < 3:
#         raise ShortInputException(len(text), 3)
#     for badword in badwords:
#         if text.lower().find(badword) != -1:
#             raise BadWordException(badword)
# except BadWordException as ex:
#     print("BadWordException: You have used a badword : {} ".format(ex.badword))
# except ShortInputException as ex:
#     print("ShortInputException: Your entered string was too small. Should be atleast {}".format(ex.atleast))
#
#
# time.sleep(2)
# input("Press any key to exit...")

# import time
#
# class ShortInputException(Exception):
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length  = length
#         self.atleast = atleast
#
# class LongInputException(Exception):
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
#
# class BadWordException(Exception):
#     def __init__(self, badword):
#         Exception.__init__(self)
#         self.badword = badword
#
# class SymbolException(Exception):
#     def __init__(self, symbol):
#         Exception.__init__(self)
#         self.symbol = symbol
#
# badwords = ('fuck', 'bitch', 'cyka', 'naxni')
# symbols = ('!', '@', '#', '$', '?')
#
# try:
#     text = input("Enter something--> ").strip(' ')
#     if len(text) < 3:
#         raise ShortInputException(len(text), 3)
#
#     if len(text) > 10:
#         raise LongInputException(len(text), 10)
#
#     for badword in badwords:
#         if text.lower().find(badword) != -1:
#             raise BadWordException(badword)
#
#     for symbol in symbols:
#         if text.lower().find(symbol) != -1:
#             raise SymbolException(symbol)
#
# except BadWordException as ex:
#     print("BadWordException: You have used a badword: {}".format(ex.badword))
#
# except SymbolException as ex:
#     print("SymbolException: You have used a symbol: {}".format(ex.symbol))
#
# except ShortInputException as ex:
#     print("ShortInputException: Your entered string was too small. Should be atleast {}".format(ex.atleast))
#
# except LongInputException as ex:
#     print("LongInputException: Your entered string was too long. Should be atleast {}".format(ex.atleast))
#
# time.sleep(5)
# input('press anykey to exit')

#Try ... Finally

import sys
import time

f = None
try:
    f = open("poem.txt")

    #our usual file-reading idiom

    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+c now")

        #To make sure it runs for a while

        time.sleep(2)

except IOError:
    print("Could not find file poem.txt")

except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")

finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")