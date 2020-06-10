
#'os.listdir' to get all files in a folder

import os
import shutil

currentPath = os.getcwd()
dir_name  = '2020-06-09'
folder_full_path = os.path.join(currentPath, dir_name)

savePath = r'C:\Users\user\Desktop\myfx\history_data'
save_folder_full_path = os.path.join(savePath)

#searching those symbols in folder
check_name_list = ["EURUSD","GBPUSD","USDJPY","GBPJPY","USDCAD","EURAUD","EURJPY","AUDCAD","AUDJPY","AUDNZD","AUDUSD","CADJPY",
                   "EURCAD","EURCHF","EURCZK","EURGBP","EURHUF","EURNOK","EURNZD","EURPLN","EURSEK","EURTRY","GBPCAD","GBPCHF",
                   "NZDCAD","NZDJPY","NZDUSD","USDCHF","USDCZK","USDHUF","USDMXN","USDNOK","USDPLN","USDSEK","USDSGD","USDTHB",
                   "USDTRY","USDZAR","CHFJPY","AUDCHF","GBPNZD","NZDCHF","XAGUSD","XAUUSD","CADCHF","GBPAUD","SPA35","SGDJPY",
                   "GBPNOK","US30","EURZAR","AUDSGD","GBPZAR","GBPSEK","CHFSGD","EURSGD","GBPSGD","EURHKD","COPPER","US500",
                   "GBPPLN","UK100","XAUGBP","NOKJPY","SP500","CHFNOK","GBPTRY","USDRUB","SEKJPY","EURMXN","XAUAUD","XAUEUR",
                   "NAS100","US2000","FRA40","GER30","XAUCHF","AUS200","GBPMXN","JPN225","XAGAUD","NOKSEK","XAGEUR","VIX","XPTUSD",
                   "XPDUSD","USDCNH","XTIUSD","XBRUSD","HK50","XNGUSD","DASH"]


if os.path.exists(folder_full_path):

    #check what are the files inside given folder     
    current_name_list = os.listdir(folder_full_path)

    count = 0

    #searching maching txt files
    for check_name in check_name_list:
        for current_name in current_name_list:

            file_name = check_name + '.txt'
            if file_name == current_name:

                current_path_file_name = os.path.join(folder_full_path, file_name)
                move_path_file_name = os.path.join(save_folder_full_path, file_name)

                with open(current_path_file_name) as cfile:
                  with open(move_path_file_name, 'a') as sfile:
                    for line in cfile:
                      sfile.write(line)


                count +=1
                

    print(dir_name, ', ', count, ' txt files data append to ', save_folder_full_path, ' path txt files')

else:
    print(dir_name , ' folder not exists...')






