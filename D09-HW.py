# Day 09
import pandas as pd 

#讀取資料夾中boston.csv讀取其欄位CHAS、NOX、RM，輸出成.xlsx檔案

bostonCSV = pd.read_csv("data/boston.csv", usecols=['CHAS', "NOX", "RM"])

bostonCSV.to_excel("data/bostonEXCEL.xlsx", sheet_name="boston")

bostonEXCEL = pd.read_excel("data/bostonEXCEL.xlsx")
print(bostonEXCEL[:5])
