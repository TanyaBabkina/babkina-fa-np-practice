from FileManagerSetings import *
from FileManager import *

manager = FileManager(root)

while True:
    command = input(f"\033[34m{os.getcwd()} = > \033[39m").split()
    
    try:
        if (command[0] == 'createDir'):
            manager.create_dir(command[1])
        elif (command[0] == 'deleteDir'):
            manager.delete_dir(command[1])
        elif (command[0] == 'changeDir'):
            manager.change_dir(command[1])
        elif (command[0] == 'createFile'):
            manager.create_file(command[1])
        elif (command[0] == 'fileInput'):
            manager.file_input(command[1], ' '.join(command[2:]))
        elif (command[0] == 'fileOutput'):
            manager.file_output(command[1])
        elif (command[0] == 'fileRemove'):
            manager.file_remove(command[1])
            
        elif (command[0] == 'fileCopy'):
            manager.file_copy(command[1], command[2])
            
        elif (command[0] == 'fileReplace' ):
            manager.file_replace(command[1], command[2])
            
        elif (command[0] == 'fileRename'):
            manager.file_rename(command[1], command[2])
            print(f"\033[32mФайл переименован\033[39m")
        elif (command[0] == 'stop'):
            break
        else:
            print(f"\033[31mНеверный ввод!\033[39m")
    except FileNotFoundError:
        print(f"\033[31mФайл или директория не найдены!\033[39m")
    except FileExistsError:
        print(f"\033[31mНевозможно создать файл, так как он уже существует\033[39m")
    except Exception:
        print(f"\033[31mОшибка\033[39m")
    