# Name : test_add_group.py
# Author : "Denisov Dmitry"
# Time : 31.03.2023
from generator.groups import GenerateData
import os


def test_add_group(app, file_path, generation):
    data = GenerateData()
    project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file = os.path.join(project_dir, file_path)
    if not os.path.isfile(file):
        data.greate_file_xlsx(file, generation)
    elif generation:
        data.greate_file_xlsx(file, generation)

    old_list = app.groups.get_group_list()
    list_groups = data.read_data_xlsx(file)
    i = 0
    while i < len(list_groups):
        app.groups.add_new_group(list_groups[i])
        old_list.append(list_groups[i])
        new_list = app.groups.get_group_list()
        i += 1
        assert sorted(old_list) == sorted(new_list)
