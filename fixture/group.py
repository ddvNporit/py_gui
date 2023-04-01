# Name : group.py
# Author : "Denisov Dmitry"
# Time : 31.03.2023
import random


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def delete_group(self, group_name, move):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        self.select_group_by_name(group_name, tree)
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.delete_group_dialog = self.app.application.window(title="Delete group")
        if not move:
            self.delete_group_dialog.window(auto_id="uxDeleteAllRadioButton").check()
        self.delete_group_dialog.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()

    def select_group_by_name(self, group_name, tree):
        tree.get_item(f'\\Contact groups\\{group_name}').click()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def check_count_group(self, list_group):
        d = len(list_group)
        if d <= 1:
            while d < 2:
                number = str(d)
                self.add_new_group(f"my group  {number}")
                d += 1
            return True
        else:
            return False

    def random_select_group(self, list_group):
        group_name = random.choice([group for group in list_group if group != "Contact groups"])
        return group_name
