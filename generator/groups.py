# Name : groups.py
# Author : "Denisov Dmitry"
# Time : 01.04.2023
import os
from comtypes.client import CreateObject

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
xl = CreateObject("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
for i in range(10):
    xl.Range["A%s" % (i+1)].Value[()] = "group %s" %i
wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
xl.Quit()
