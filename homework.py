#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thur Aug 22 16:34:56 2019

@author: MD. Hasnain
"""

# JLeague Player Search - Jリーグ

# Importing the libraries
import numpy as np
import pandas as pd
import datetime as dt

# Data set of japanese calender
era_list = [["令和","2019-05-01",2018],
            ["平成","1989-01-08",1988],
            ["昭和","1926-12-25",1925]]

# Importing the dataset
dataset = pd.read_csv('player_info.csv', encoding='SHIFT-JIS', header=None)
player_numbers = dataset.iloc[:, [0]].values
player_names = dataset.iloc[:, [1]].values
player_birthdays = dataset.iloc[:, [4]].values
    
def searchPlayer():
    input_number = input ("背番号を入力してください: ")
    
    try:
        player_to_search = int(input_number)
    except ValueError:
        print("無効入力")
        searchPlayer()
        

    # Search the player
    player_index = np.where(player_numbers == player_to_search)[0]
    
    if(len(player_index) == 0):
        # Player not found
        print("添付のファイルをご覧ください")
    else:
        # Player found.
        player_name = player_names[player_index[0]]
        
        # Removing space from the name
        name_arr = player_name[0].split()
        name = ""
        for part in name_arr:
            name = name + part
            
        # Converting Birthday from English to Japanese Calender
        birthday_en_str = player_birthdays[player_index[0]]
        month, day, year = birthday_en_str[0].split('/')
        birthday_en = dt.datetime(int(year), int(month), int(day))
        
        for era in era_list:
            era_year, era_month, era_day = era[1].split('-')
            date_era = dt.datetime(int(era_year), int(era_month), int(era_day))
            
            if(birthday_en >= date_era):
                player_era = era[0]
                player_year = int(year) - int(era[2])
                break
        
        # Formatting as requirement
        birthday_jp = player_era + str(player_year) + '年' + str(month) + '月' + str(day) + '日'
        output = player_to_search + '-' + name + '-' + birthday_jp
            
        # Print the output
        print(output)
        
        # Ask user for search again('はい' for search again)
        search_again = input ("もう一度検索(はい/いいえ): ")
        if(search_again == 'はい'):
            searchPlayer()
        
searchPlayer()
    
        
        