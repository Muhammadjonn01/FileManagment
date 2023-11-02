import pathlib
import os
from datetime import datetime
import shutil
class Modifications:
    def __init__(self,name_of_file_or_dir):
        self.name_of_file = name_of_file_or_dir
        self.name_of_dir = name_of_file_or_dir

    def info_about_file(self):
            home = pathlib.Path(self.name_of_file)
            size = os.path.getsize(self.name_of_file)
            last_modifications = os.stat(self.name_of_file)
            last_time = last_modifications.st_ctime
            path_of_file = pathlib.Path.cwd() / self.name_of_file
            print ("1. Name of file:", home)
            print ("2. Size of file:", size, 'bytes')
            print ("3. Last modification:", datetime.fromtimestamp(last_time)) 
            print ("4. Path of file:", path_of_file)

    def create_file(self):
            if os.path.exists(self.name_of_file):
                print("This file already exists")
            else:
                open(self.name_of_file, 'x')

    def create_directory(self):
        pathlib.Path(self.name_of_dir).mkdir(parents=True)

    def delete_file(self):
          print(f"Do you want to delete {self.name_of_file}?")
          if input("Enter 1 to confirm: ") == '1':
            os.remove(self.name_of_file)
            print("File deleted.")
          else:
            print("Deletion canceled.")

    def delete_directory(self):
        print(f"Do you want to delete {self.name_of_dir}?")
        if input("Enter 1 to confirm: ") == '1':
            os.rmdir(self.name_of_dir)
            print("Directory deleted.")
        else:
            print("Deletion canceled.")

    def rename_file(self):
        what_rename = input("Name that you want to put:")
        rename1 = pathlib.Path(self.name_of_file).rename(what_rename)
        return rename1

    def change_directory(self):
        old_dir = pathlib.Path.cwd()
        print(f"Your current directory is: {old_dir}")

        print("Are you sure you want to change your current directory?")
        user_agree = input("Y/N\n")

        if user_agree.lower() == 'y':
            user_new_place = input("Enter the new directory path: ")
            new_dir = pathlib.Path(user_new_place)

            if new_dir.is_dir():
                os.chdir(new_dir)
                print(f"Your current directory has been changed to: {new_dir}")
            else:
                print(f"The path '{user_new_place}' is not a valid directory.")
        else:
            pass
    
    def reading_files(self):
        cur_path = pathlib.Path.cwd()
        new_file = pathlib.Path(self.name_of_file)
        cur_p = cur_path / new_file
        print(cur_p)

        input_num = int(input("Enter number of lines: "))
        f = open(cur_p, "r")

        for i in range(1, input_num+1):
            print(f.readline())
    
    def writing_files(self):
        with open(self.name_of_file, "w") as file:
            content = file.write(input("Enter: "))
            print("Content:",content)
            open(self.name_of_file, "a").close()
    
    def append_text(self):
        with open(self.name_of_file, "a") as file:
            content = file.write(input("Enter: "))
            print("Content:")
            print(content)
            open(self.name_of_file, "a").close()

    def search_in_files(self):
        users_info = input("What you want to search:")
        cur_path = pathlib.Path.cwd()
        new_file = pathlib.Path(self.name_of_file)
        cur_ob = cur_path / new_file
        print(cur_ob)
        print(users_info)
        file_in = open(cur_ob, 'r')
        text = file_in.read()
        if users_info in text:
           print(users_info)
        else:
           pass

    def move_dir_file(self):
        place_to_remove = input("Input place to remove your file or directory:")
        name_input_path = pathlib.Path(self.name_of_file)
        place_input_path = pathlib.Path(place_to_remove)
        current_cwd = pathlib.Path.cwd()
        path_object = current_cwd / name_input_path
        path_place = current_cwd / place_input_path
        move_place = shutil.move(path_object, path_place)
        return (move_place)