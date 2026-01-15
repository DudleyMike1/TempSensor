import pandas as pd

def main():
    while True:
        print("Main Menu")
        print("1. Temperature Data Summary")
        print("2. VPD Data Summary")
        print("3. Quit")
        choice = input("Choose the data to interogate(1 or 2):")
        if choice == "1":
            tempData()
        elif choice == "2":
            vpdData()
        elif choice == "3":
            break
        else:
            print("\n\tInvalid Input\n")


def tempData():
    pass

def vpdData():
    pass


main()