#-*-coding:utf-8-*-
import openpyxl
passa = input("読み込むファイルのパス：")
passb = input("書き出すファイルのパス：")
wb = openpyxl.load_workbook(passa)
sheet = wb["Sheet1"]
colum1 = input("一つ目の列：")
colum2 = input("二つ目の列：")
colum3 = input("結果の列：")
beginrows = int(input("何行目から？："))
endrows = int(input("何行目まで？："))
for i in range(beginrows,endrows+1):
    cell1 = sheet["{0}{1}".format(colum1,i)]
    cell2 = sheet["{0}{1}".format(colum2,i)]
    cell3 = sheet["{0}{1}".format(colum3,i)]
    if cell1.value is None and cell2.value is not None:
        c = set(cell2.value.split())
        cell3.value = ' '.join(c)
    elif cell2.value is None and cell1.value is not None:   
        b = set(cell1.value.split())
        cell3.value = ' '.join(b)
    elif cell1.value is None  and  cell2.value is None:
        cell3.value = ""
    else:    
        b = set(cell1.value.split())
        c = set(cell2.value.split())
        cell3.value = ' '.join(b|c)   
wb.save(passb)
print("完了")    
