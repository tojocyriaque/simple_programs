from math import *
import os

def main():
    while True:
        _inp = input("mash::> ")

        if _inp=="exit":
            break

        elif _inp=="clear":
            os.system("clear")

        else:
            evl = eval(_inp)
            if evl:
                print(evl)

if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("\nGood bye! ;)")
