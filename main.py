from modules import Modifications
import pathlib 
while True:
    # Here we can choose what we want to do
    print("1. Information about list:")
    print("2. Create a new file:")
    print("3. Create a new directory:")
    print("4. Delete a file:")
    print("5. Delete a directory:")
    print("6. Rename a file or directory:")
    print("7. Change a folder:")
    print("8. Show CWD:")
    print("9. Open a file and lets you edit its content and saves it:")
    print("10. Rewrite all info inside the file:")
    print("11. Append text inside file:")
    print("12. Search function inside a selected folder:")
    print("13. Move directory or file from one place to another")
    inp = input("Choose what you want to do:")

    if inp == '1':
        # This function show info about file for example:it's name,it size,it's last modification,it's path.  
        name_of_files = Modifications(input("Input name of the file that you want to see info about it:"))
        name_of_files.info_about_file() 
    elif inp == '2':
         # With this function we can create file
         name_of_files = Modifications(input("Input name of the file that you want to create:"))
         name_of_files.create_file()
    elif inp == '3':
         # With this function we can create directory
         name_of_files = Modifications(input("Input name of the directory that you want to create:"))
         name_of_files.create_directory()
    elif inp == '4':
        # With this function we can delete file
        name_of_files = Modifications(input("Input name of the file that you want to delete:"))
        name_of_files.delete_file()
    elif inp == '5':
         # With this function we can delete directory
         name_of_files = Modifications(input("Input name of the directory that you want to delete:"))
         name_of_files.delete_directory()
    elif inp == '6':
        # With this function we can rename file or directory
         name_of_files = Modifications(input("Input name of the file or directory that you want to rename:"))
         name_of_files.rename_file()
    elif inp == '7':
        # With this function we can change directory
         name_of_files = Modifications(input("Input name of the directory that you want to change:"))
         name_of_files.change_directory()
    elif inp == '8':
         #This function show current directory
         cur = pathlib.Path.cwd()
         print(f"Your current directory is: {cur}")
    elif inp == '9':
         #this is Function which open a file and lets you edit its content and saves it.
         name_of_files = Modifications(input("Input the new file path:"))
         name_of_files.reading_files()
    elif inp == '10':
         #This function rewrite all info 
         name_of_files = Modifications(input("Input the new file path:"))
         name_of_files.writing_files()
    elif inp == '11':
         #This function can append text inside file
         name_of_files = Modifications(input("Input the new file path:"))
         name_of_files.append_text()
    elif inp =='12':
         #This function can search info that you input
         name_of_files = Modifications(input("Input the new file path:"))
         name_of_files.search_in_files()
    elif inp == '13':
        #This function can remove file or directory to another place
         name_of_files = Modifications(input("Input the name of the file or directory: "))
         name_of_files.move_dir_file()
    else:
        print("Invalid choice")

    ask = input("Do you want to continue? (Y/N): ")
    if ask.lower() != 'y':
        ask_1 = input("Can you rate our program? (Y/N): ")
        if ask_1.lower() == 'y':
            x = int(input("from 1 to 5:"))
            filename = 'rating.txt'
            def save_variable_to_file (x, filename):
               with open(filename, 'w') as file:
                   file.write(str(x))
            print('Thanks!')
            save_variable_to_file(x,filename)
        else:
            break
   