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
    dfData = getData()
    print (dfData)
    while True:
        print("Temperatue Menu")
        print("1. Output Daily Average Temperature")
        print("2. Output Daily Maximum Temperature")
        print("3. Output Daily Minimum Temperature")
        print("4. Quit")
        choice = input("What summary do you want?:")
        if choice == "1":
            averageTemp(dfData)
        elif choice == "2":
            maxTemp(dfData)
        elif choice =="3":
            minTemp(dfData)
        elif choice == "4":
            break
        else:
            print ("invalid selection")

def vpdData():
    dfData = getData()
    print (dfData)

def getData():
    """Reads in the data from the file"""
    df = pd.read_csv("Data\Meter1_data.csv")
    return df

def averageTemp(dfData):
    pass

def maxTemp(dfData):
    pass

def minTemp(dfData):
    pass





main()