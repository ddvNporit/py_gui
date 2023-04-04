# Name : groups.py
# Author : "Denisov Dmitry"
# Time : 01.04.2023
import os, random, string
from comtypes.client import CreateObject


class GenerateData():
    global n
    n = 3
    project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file = os.path.join(project_dir, "groups.xlsx")

    def random_string(self, prefix, maxlen):
        # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
        symbols = string.ascii_letters + string.digits + " " * 10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def generator_data(self):
        testdata = [
            self.random_string("name", 10)
            for i in range(n)
        ]
        return testdata

    def greate_file_xlsx(self, file):
        testdata = self.generator_data()
        xl = CreateObject("Excel.Application")
        xl.Visible = 0
        wb = xl.Workbooks.Add()
        i = 0
        self.generator_data()
        while i < len(testdata):
            xl.Range["A%s" % (i + 1)].Value[()] = testdata[i]
            i += 1
        if os.path.isfile(file):
            os.remove(file)
        wb.SaveAs(file)
        xl.Quit()

    def read_data_xlsx(self, file):
        xl = CreateObject("Excel.Application")
        xl.Visible = 0
        # project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # file = os.path.join(project_dir, "groups.xlsx")
        wb = xl.Workbooks.Open(file)
        sheet = wb.ActiveSheet
        i = 1
        list_groups = []
        while sheet.Cells(i, 1).value() is not None:
            val = sheet.Cells(i, 1).value()
            list_groups.append(val)
            i += 1
            if i >= 100:
                break
        xl.Quit()
        return list_groups
