#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bellie
#
# Created:     08/08/2014
# Copyright:   (c) Bellie 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv, os
from collections import defaultdict
import batchFiles
import config as cfg
import pandas as pd


csvFile = 'J:\\Projects\\SMB_Model\\ClimateData\\ClimateData.csv'
def csv2dict(csvFile):
    # Code from http://stackoverflow.com/questions/16503560/read-specific-columns-from-csv-file-with-python-csv
    columns = defaultdict(list) # each value in each column is appended to a list
    with open(csvFile) as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value
                try:
                    columns[k].append(float(v)) # append the value into the appropriate list
                except:
                    columns[k].append(v)
    return columns



def writeCSV(csvFile,data):
    b = open(csvFile, 'w')
    a = csv.writer(b)
    a.writerows(data)
    b.close()



def csvTable(X,Y,Z):
    data = [['X','Y','Z']]
    for ii in range(len(X)):
        data.append([X[ii],Y[ii],Z[ii]])
    return data


input_df = pd.DataFrame.from_csv(csvFile,0,',')
input_df['SMB'] = 90
days = input_df['XCord'].values.tolist().count(input_df['XCord'].values[0])
stations = input_df['Date(Local_Day)'].values.tolist().count(input_df['Date(Local_Day)'].values[0])

XCord_ls = input_df['XCord'].values[0:stations]
YCord_ls = input_df['YCord'].values[0:stations]
Rainfall_all = input_df['Rain(mm)'].values
PET_all = input_df['PET(mm)'].values
SMB_ls = input_df['XCord'].values[0:stations]

for ii in range(days):
    Rainfall_ls = Rainfall_all[ii*stations:(ii+1)*stations]
    PET_ls = PET_all[ii*stations:(ii+1)*stations]
    for count in range(len(Rainfall_ls)):
        SMB_ls[count] -= PET_ls[count] + Rainfall_ls[count]
    todaysDate = pd.to_datetime(input_df.index.values[ii*stations+1],'%d/%m/%Y')
    #todaysDate = input_df.index.values[ii*stations+1]
    print todaysDate
    data = csvTable(XCord_ls,YCord_ls,SMB_ls)
    writeCSV(cfg.scriptFP+'\\results\\csv\\'+str(todaysDate)[:10]+'.csv',data)
    #batchFiles.csv2grd(cfg.grid_SMB+str(todaysDate)[:10])



