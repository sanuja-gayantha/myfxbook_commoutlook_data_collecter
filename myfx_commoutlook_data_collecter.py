# Name   : myfx_commoutlook_data_collecter.py
# Author : sanuja-gayantha (github.com) 
# Date   : 2020/06/10
# Columns: time, shortPercentage, longPercentage, shortVolume, longVolume, 
#           longPositions, shortPositions, totalPositions, avgShortPrice, avgLongPrice

#important --> time = GMT+3



import requests
from datetime import datetime as dt
import datetime
import time
import os


def save_data():
    try:
        #send requst to server given my account name and password
        Request_key = 'https://www.myfxbook.com/api/login.json?email=username&password=password'
        response = requests.get(Request_key, verify = False)
        row_data = response.json()


        #Get the server time
        ctime = response.headers['Date'].split(',')[1].split(' ')
        ctime_value = str(ctime[1] + ' ' + ctime[2] + ' ' + ctime[3] + ' ' + ctime[4])

        current_time_string = dt.strptime(ctime_value, '%d %b %Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S') 
        #GMT time
        current_time = dt.strptime(current_time_string, '%Y-%m-%d %H:%M:%S')
        #trade server time
        current_server_time = current_time  + datetime.timedelta(hours=3)

        create_date = current_server_time.strftime('%Y-%m-%d')


        #create paths
        currentPath = os.getcwd()
        folder_full_path = os.path.join(currentPath, create_date)

        #create folder accouding to current date
        if not os.path.exists(folder_full_path):
            os.makedirs(folder_full_path)


        #Session id
        session_id = row_data['session'] 

        #send requseting sentement data
        path = ('http://www.myfxbook.com/api/get-community-outlook.json?session=' +  session_id)
        #print(path)
        response = requests.get(path, verify = False)
        data = response.json()['symbols'] #get dictonary list

        #all names of receve currences,comadities, stocks, etc
        receve_name_list = ["EURUSD","GBPUSD","USDJPY","GBPJPY","USDCAD","EURAUD","EURJPY","AUDCAD","AUDJPY","AUDNZD","AUDUSD","CADJPY",
                           "EURCAD","EURCHF","EURCZK","EURDKK","EURGBP","EURHUF","EURNOK","EURNZD","EURPLN","EURSEK","EURTRY","GBPCAD",
                           "GBPCHF","NZDCAD","NZDJPY","NZDUSD","USDCHF","USDCZK","USDDKK","USDHKD","USDHUF","USDMXN","USDNOK","USDPLN",
                           "USDSEK","USDSGD","USDTHB","USDTRY","USDZAR","CHFJPY","AUDCHF","GBPNZD","NZDCHF","XAGUSD","XAUUSD","CADCHF",
                           "GBPAUD","SPA35","SGDJPY","SUGAR","GBPNOK","US30","EURZAR","AUDSGD","GBPZAR","GBPSEK","CHFSGD","EURSGD","GBPSGD",
                           "AUDDKK","EURHKD","GBPDKK","COPPER","COFFEE","EURO50","TRYJPY","US500","GBPPLN","WHEAT","COCOA","UK100","XAUGBP",
                           "COTTON","NOKJPY","SP500","ZARJPY","HKDJPY","CHFNOK","GBPTRY","USDRUB","SEKJPY","MSFT","JNJ","EURMXN","XAUAUD",
                           "XAUEUR","WS30","NAS100","SGDHKD","US2000","FRA40","GER30","AUDSEK","XAUCHF","CHFSEK","AUS200","GBPMXN","JPN225",
                           "XAGAUD","NOKSEK","USDX","XAGEUR","EBAY","VIX","CHFHKD","YHOO","XPTUSD","GBPHKD","XPDUSD","CADHKD","USDCNH",
                           "AUDHKD","NZDHKD","AAPL","PFE","FB","IT40","GS","NKE","BA","CVX","GOOG","XTIUSD","XBRUSD","US30.D","TWTR","HK50",
                           "GOPRO","XNGUSD","APPL","DXU5","DXZ5","OGZD","CN50","DASH","RIPPLE","SCI25","CNI30","LAT30","JPYX"]

        #print(len(receve_name_list))


        for count,row in enumerate(data):

            #save data in seperate files, number of files are 143
            write_data = (str(current_server_time), row['shortPercentage'], row['longPercentage'], row['shortVolume'], row['longVolume'],
                         row['longPositions'], row['shortPositions'], row['totalPositions'], row['avgShortPrice'], row['avgLongPrice'])

            completeName =  os.path.join(folder_full_path, str(receve_name_list [count]) + ".txt")  

            #append new data to file
            with open(completeName, 'a') as myfile:
                myfile.write(str(write_data) + '\n')

        print("running...")

    except Exception as e:
        #Save all execeptions in txt file   
        #with open("Exceptions.txt", 'a') as ex:
            #ex.write(str(e) + '\n')
        pass


    
if __name__ == '__main__':
	
	start_time = time.time()
	while True:
		save_data()
		time.sleep(60.0 - ((time.time() - start_time) % 60.0))
