#!/usr/bin/python

# Install `XlsxWriter` 
#pip install XlsxWriter

import pandas as pd
import sys

sep = ','

if __name__ == "__main__":
    for i in range(len(sys.argv)-1):
        if sys.argv[i]== "--separator" or sys.argv[i] == "-s":
            sep = sys.argv[i+1]
    if len(sys.argv) > 1:
        i = 1
        while  i < len(sys.argv):
            if sys.argv[i]== "--separator" or sys.argv[i] == "-s":
                i += 2
                continue

            param = sys.argv[i]
            df = pd.read_csv(param, sep=sep)
            filexlsx = param.replace(".csv", ".xlsx")
            writer = pd.ExcelWriter(filexlsx, engine='xlsxwriter')
            df.to_excel(writer,"Sheet1")
            writer.save()
            print("{} converted".format(param))
            i += 1
    else:
        print("No cmd arguments")
        
    
