# Name : test_delete_group.py
# Author : "Denisov Dmitry"
# Time : 31.03.2023
import random


def test_delete_group_with_move(app):
    old_list = app.groups.get_group_list()
    group = select_group(old_list)
    app.groups.delete_group(group, move=True)
    new_list = app.groups.get_group_list()
    old_list.remove(group)
    print(new_list)
    assert sorted(old_list) == sorted(new_list)
def test_delete_group_without_move(app):
    old_list = app.groups.get_group_list()
    group = select_group(old_list)
    app.groups.delete_group(group, move=False)
    new_list = app.groups.get_group_list()
    old_list.remove(group)
    assert sorted(old_list) == sorted(new_list)

def select_group(list_group):
    group_name = random.choice([group for group in list_group if group != "Contact groups"])
    return group_name
