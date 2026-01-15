import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from datetime import datetime

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
    while True:
        print(" VPD Summary Menu")
        print("1. Daily Average")
        print("2. Daily Minimum")
        print("3. Daily Maximum")
        print("4. Daily Median")
        print("5. Return to Main Menu")
        choice = input("Enter Choice:")
        if choice == "1":
            averageVpd(dfData)
        elif choice == "2":
            minVpd(dfData)
        elif choice == "3":
            maxVpd(dfData)
        elif choice == "4":
            medianVpd(dfData)
        elif choice == "5":
            break
        else:
            print ("\n\tInvlaid Choice\n")


def getData():
    """Reads in the data from the file"""
    df = pd.read_csv("Data\Meter1_data.csv")
#rename columns Need to be aware of units
    df = df.rename(columns={'Temperature_Celsius(°C)': 'Temp', 'Relative_Humidity(%)': 'RH','Absolute_Humidity(g/m³)':'AH', 'DPT_Celsius(°C)':'Dewpoint','VPD(kPa)':'VPD'})
#convert the Timestamp to seperate date time columns
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    print(f'Dataframe for Meter 1 in use')
    print(df.info())
    return df

def averageTemp(dfData):   
    lastDay = (dfData.Timestamp.max())
    lastDay = lastDay.date()
    firstDay = (dfData.Timestamp.min())   
    firstDay = firstDay.date()
    print (f"Showing Data in the following Range:{firstDay} - {lastDay}")
    lastDay = lastDay + dt.timedelta(days=1)  #need to go one day further for the mask
    mask = (dfData.Timestamp >= pd.Timestamp(firstDay)) & (dfData.Timestamp < pd.Timestamp(lastDay))
    dfday = dfData.loc[mask, ['Timestamp','Temp','VPD']]
    dfdaydata = dfday.groupby([dfday['Timestamp'].dt.day])["Temp"].mean()
    print("Mean value of Temperature for each Day")
    print(dfdaydata)
    dfdaydata.plot(kind = 'bar')
    plt.suptitle(f"Mean Temperature Day ")
    plt.xlabel("Day ")
    plt.ylabel("Degree C")
    plt.show()

def maxTemp(dfData):
    lastDay = (dfData.Timestamp.max())
    lastDay = lastDay.date()
    firstDay = (dfData.Timestamp.min())   
    firstDay = firstDay.date()
    print (f"Showing Data in the following Range:{firstDay} - {lastDay}")
    lastDay = lastDay + dt.timedelta(days=1)  #need to go one day further for the mask
    mask = (dfData.Timestamp >= pd.Timestamp(firstDay)) & (dfData.Timestamp < pd.Timestamp(lastDay))
    dfday = dfData.loc[mask, ['Timestamp','Temp','VPD']]
    dfdaydatamax = dfday.groupby([dfday['Timestamp'].dt.day])["Temp"].max()
    print("Maximum value of Temperature for each Day")
    print(dfdaydatamax)
    dfdaydatamax.plot(kind = 'bar')
    plt.suptitle(f"Maximum Temperature each  Day ")
    plt.xlabel("Day ")
    plt.ylabel("Degree C")
    plt.show()    

def minTemp(dfData):
    lastDay = (dfData.Timestamp.max())
    lastDay = lastDay.date()
    firstDay = (dfData.Timestamp.min())   
    firstDay = firstDay.date()
    print (f"Showing Data in the following Range:{firstDay} - {lastDay}")
    lastDay = lastDay + dt.timedelta(days=1)  #need to go one day further for the mask
    mask = (dfData.Timestamp >= pd.Timestamp(firstDay)) & (dfData.Timestamp < pd.Timestamp(lastDay))
    dfday = dfData.loc[mask, ['Timestamp','Temp','VPD']]
    dfdaydata = dfday.groupby([dfday['Timestamp'].dt.day])["Temp"].min()
    print("Minimum value of Temperature for each Day")
    print(dfdaydata)
    dfdaydata.plot(kind = 'bar')
    plt.suptitle(f"Minimum Temperature each  Day ")
    plt.xlabel("Day ")
    plt.ylabel("Degree C")
    plt.show()

def averageVpd(dfData):
    lastDay = (dfData.Timestamp.max())
    lastDay = lastDay.date()
    firstDay = (dfData.Timestamp.min())   
    firstDay = firstDay.date()
    print (f"Showing Data in the following Range:{firstDay} - {lastDay}")
    lastDay = lastDay + dt.timedelta(days=1)  #need to go one day further for the mask
    mask = (dfData.Timestamp >= pd.Timestamp(firstDay)) & (dfData.Timestamp < pd.Timestamp(lastDay))
    dfday = dfData.loc[mask, ['Timestamp','Temp','VPD']]
    dfdaydata = dfday.groupby([dfday['Timestamp'].dt.day])["VPD"].mean()
    print("Mean value of VPD for each Day")
    print(dfdaydata)
    dfdaydata.plot(kind = 'bar')
    plt.suptitle(f"Mean VPD each  Day ")
    plt.xlabel("Day ")
    plt.ylabel("kPa")
    plt.show()

def minVpd(dfData):
    lastDay = (dfData.Timestamp.max())
    lastDay = lastDay.date()
    firstDay = (dfData.Timestamp.min())   
    firstDay = firstDay.date()
    print (f"Showing Data in the following Range:{firstDay} - {lastDay}")
    lastDay = lastDay + dt.timedelta(days=1)  #need to go one day further for the mask
    mask = (dfData.Timestamp >= pd.Timestamp(firstDay)) & (dfData.Timestamp < pd.Timestamp(lastDay))
    dfday = dfData.loc[mask, ['Timestamp','Temp','VPD']]
    dfdaydata = dfday.groupby([dfday['Timestamp'].dt.day])["VPD"].max()
    print("Max value of VPD for each Day")
    print(dfdaydata)
    dfdaydata.plot(kind = 'bar')
    plt.suptitle(f"Max VPD each  Day ")
    plt.xlabel("Day ")
    plt.ylabel("kPa")
    plt.show()

def maxVpd(dfData):
    lastDay = (dfData.Timestamp.max())
    lastDay = lastDay.date()
    firstDay = (dfData.Timestamp.min())   
    firstDay = firstDay.date()
    print (f"Showing Data in the following Range:{firstDay} - {lastDay}")
    lastDay = lastDay + dt.timedelta(days=1)  #need to go one day further for the mask
    mask = (dfData.Timestamp >= pd.Timestamp(firstDay)) & (dfData.Timestamp < pd.Timestamp(lastDay))
    dfday = dfData.loc[mask, ['Timestamp','Temp','VPD']]
    dfdaydata = dfday.groupby([dfday['Timestamp'].dt.day])["VPD"].min()
    print("Min value of VPD for each Day")
    print(dfdaydata)
    dfdaydata.plot(kind = 'bar')
    plt.suptitle(f"Min VPD each  Day ")
    plt.xlabel("Day ")
    plt.ylabel("kPa")
    plt.show()

def medianVpd(dfData):
    lastDay = (dfData.Timestamp.max())
    lastDay = lastDay.date()
    firstDay = (dfData.Timestamp.min())   
    firstDay = firstDay.date()
    print (f"Showing Data in the following Range:{firstDay} - {lastDay}")
    lastDay = lastDay + dt.timedelta(days=1)  #need to go one day further for the mask
    mask = (dfData.Timestamp >= pd.Timestamp(firstDay)) & (dfData.Timestamp < pd.Timestamp(lastDay))
    dfday = dfData.loc[mask, ['Timestamp','Temp','VPD']]
    dfdaydata = dfday.groupby([dfday['Timestamp'].dt.day])["VPD"].median()
    print("Median value of VPD for each Day")
    print(dfdaydata)
    dfdaydata.plot(kind = 'bar')
    plt.suptitle(f"Median VPD each  Day ")
    plt.xlabel("Day ")
    plt.ylabel("kPa")
    plt.show()




main()