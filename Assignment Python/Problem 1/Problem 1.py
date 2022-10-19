# -*- coding: utf-8 -*-
"""
Problem statement 1: Write python code
A restaurant keeps a log of (eater_id, foodmenu_id) for all the diners. The eater_id
is a unique number for every diner and foodmenu_id is unique for every food item
served on the menu. Write a program that reads this log file and returns the top 3
menu items consumed. If you find an eater_id with the same foodmenu_id more
than once then show an error.

Created on Wed Oct 19 22:31:23 2022

@author: mobashshir
"""
import json


class FileRead:
    def __init__(self, file_name):
        __file = open(file_name, "r")
        self._data_lines = __file.read().splitlines()
        __file.close()
        
    def findMenuConsumed(self):
        # print(self.data_lines)
        def _checkDuplicateMenu():
            for data in self._data_lines:
                l = data.split(":")
                
                menu = {}
                
                menu_list = json.loads(l[1])
                # print(l)
                for x in menu_list:
                    
                    if x not in menu:
                        menu[x] = 1
                    else:
                        # return True
                        # print(menu_list)
                        raise Exception(
                            "find an eater_id with the same foodmenu_id more than once ")
                        
            return False

        def _findTopMenu():
            try:
                if _checkDuplicateMenu() == False:
                    d = {}
                    for data in self._data_lines:
                        l = data.split(":")
                        
                        menu_list = json.loads(l[1])
                        # print(menu_list)
                        
                        for x in menu_list:
                            if x not in d:
                                d[x] = 1
                            else:
                                d[x] += 1
                    
                    return sorted(d, key=d.get, reverse=True)[:3]
            except:
                print("DuplicateError: Find an eater_id with the same foodmenu_id more than once!")
        return _findTopMenu()
            
        


data_1 = FileRead("data.LOG")
res = data_1.findMenuConsumed()
if res != None:
    print("Top 3 menu items consumed are:")
    for i in range(1,4):
        print(i, ": ",res[i-1])

