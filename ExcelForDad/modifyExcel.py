import openpyxl
import pandas as pd

wbPath= "ExcelForDad/Aderfarben.xlsx"

""" 
wb = openpyxl.load_workbook(wbPath) #workbook
sh = wb["Fertig"] #sheet
r1c1 = sh.cell(1,4).value  """

#firstsheet =pd.read_excel(wbPath,sheet_name=0,engine="openpyxl")
row4=pd.read_excel(wbPath,sheet_name=0,usecols="D")
df=row4["Ader 1"].to_numpy().tolist()

#writer = pd.ExcelWriter(wbPath)


#print(df)

def subst(i):
    if i == "schwarz":
        return i.replace("schwarz","bk")
    if i == "weiß":
        return i.replace("weiß","wh")
    if i == "blau":
        return i.replace("blau","bu")
    if i == "braun":
        return i.replace("braun","bn")
    if i == "rot":
        return i.replace("rot","rd")
    if i == "orange":
        return i.replace("orange","or")
    if i == "violett":
        return i.replace("violett","vio")
    if i == "rosa":
        return i.replace("rosa","rs")
    if i == "grün":
        return i.replace("grün","gn")
    if i == "dunkelblau":
        return i.replace("dunkelblau","dbu")
    if i == "grüngelb":
        return i.replace("grüngelb","gn/ye")
    if i == "braunschwarz":
        return i.replace("braunschwarz","bn/bk")
    else:
        return i
    


testlist = ["schwarz","schwarz","weiß","blau","violett","orange","1","nan"]
#result = [colors.replace('schwarz','bk') for colors in df]

res = map(subst,df)
#newDataFrame = pd.DataFrame.from_records(res)
print(type(newDataFrame))

#print(result)
