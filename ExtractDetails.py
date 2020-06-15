#In this code, after having extracted all emails as .eml files,I have extrated the necessary data and stored in xls file
import xlwt 
from xlwt import Workbook 
import os
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1') 
sheet1.write(0, 0, 'Customer_name')
sheet1.write(0, 1, 'Customer_Address')
sheet1.write(0, 2, 'Order_date')
sheet1.write(0, 3, 'Order_Id') 
sheet1.write(0, 4, 'Contact_Number')

Customer_name = 519 #In my data,for every mail,  the data I needed was in a particular format,and this I could obtain from these line numbers starting from 0
Customer_Address = 535
Order_Date = 575
Order_Id = 591
Contact_Number = 527
i=0 #This i behaves as a counter to write into the next row of the excel file
#lines[name/address/date/id] can be extracted
files = os.listdir()

for filename in files:
    if filename.endswith('.eml'):
        try:
            with open(filename) as f:
                lines = f.readlines()
                i=i+1
                sheet1.write(i, 0, lines[Customer_name].strip().replace('<td style="text-align: left;font-size: 15px;color: #7d7d76;">','').replace('</td>',''))
                sheet1.write(i, 1, lines[Customer_Address].strip().replace('<td style="text-align: left;font-size: 15px;color: #7d7d76;">','').replace('</td>',''))
                sheet1.write(i, 2, lines[Order_Date].strip())
                sheet1.write(i, 3, lines[Order_Id].strip())
                sheet1.write(i, 4, lines[Contact_Number].strip().replace('<td style="text-align: left;font-size: 15px;color: #7d7d76;">','').replace('</td>',''))
                #print(lines[Customer_name].strip().replace('<td style="text-align: left;font-size: 15px;color: #7d7d76;">','').replace('</td>',''))
                #print(lines[Customer_Address].strip().replace('<td style="text-align: left;font-size: 15px;color: #7d7d76;">','').replace('</td>',''))
                #print(lines[Order_Date].strip())
                #print(lines[Order_Id].strip())
                #print(lines[Contact_Number].strip().replace('<td style="text-align: left;font-size: 15px;color: #7d7d76;">','').replace('</td>',''))
                


        except:
            print(filename)

wb.save('sample.xls')     

