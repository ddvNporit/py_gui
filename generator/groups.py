# Name : groups.py
# Author : "Denisov Dmitry"
# Time : 01.04.2023
import os, random, string
from comtypes.client import CreateObject

n = 3
project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file = os.path.join(project_dir, "groups.xlsx")


def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def generator_data():
    global testdata
    testdata = [
        random_string("name", 10)
        for i in range(n)
    ]


def greate_file_xlsx():
    xl = CreateObject("Excel.Application")
    xl.Visible = 0
    wb = xl.Workbooks.Add()
    i = 0
    generator_data()
    while i < len(testdata):
        xl.Range["A%s" % (i + 1)].Value[()] = testdata[i]
        i += 1
    if os.path.isfile(file):
        os.remove(file)
    wb.SaveAs(file)
    xl.Quit()


greate_file_xlsx()

def read_data_xlsx():
    xl = CreateObject("Excel.Application")
    xl.Visible = 0
    wb = xl.Workbooks.Open(file)
    sheet = wb.ActiveSheet
    val = sheet.Cells(1, 1).value
    print(val)
    print(repr(val))
    xl.Quit()
read_data_xlsx()
