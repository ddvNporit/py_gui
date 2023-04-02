# Name : test_add_group.py
# Author : "Denisov Dmitry"
# Time : 31.03.2023
from comtypes.client import CreateObject
def read_data_xlsx():
    xl = CreateObject("Excel.Application")
    xl.Visible = 1
    wb = xl.Workbooks("groups.xlsx").Activate
read_data_xlsx()
def test_add_group(app):
    old_list = app.groups.get_group_list()
    app.groups.add_new_group("my group")
    new_list = app.groups.get_group_list()
    old_list.append("my group")
    assert sorted(old_list) == sorted(new_list)