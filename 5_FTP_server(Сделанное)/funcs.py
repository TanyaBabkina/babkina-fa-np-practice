
from FuncsForManager.FileManager import *
MAXSIZE = 1024*1 # килобаайт * 3


def folder_size(path, max_size=MAXSIZE):
    size = 0
    for ele in os.scandir(path):
        size += os.stat(ele).st_size
    if max_size-size <= 0:
        return 0
    else:
        return 1

# manager = FileManager(root)
# print(root, "in func")

def process(req, root, manager):
    # global manager
    # global root
    print(root, req, manager)
    command = req.split()
    try:
        if folder_size(root) or root[-17:] == "FileManagerFolder":
            if (command[0] == 'mkdir'):
                return manager.create_dir(command[1])
            if req == 'pwd':
                return manager.PWD()
            elif req == 'ls':
                rez = manager.AllDirs()
                if rez == "":
                    rez = "Пустой репозиторий"
                return rez
            elif req == "su":
                manager.su_command()
                return "Вы перешли в режим супер-пользователя"
            elif (command[0] == 'rmdir'):
                return manager.delete_dir(command[1])
            elif (command[0] == 'cd'):
                return manager.change_dir(command[1])
            elif (command[0] == 'touch'):
                return manager.create_file(command[1])
            elif (command[0] == 'echo'):
                return manager.file_input(command[1], ' '.join(command[2:]))
            elif (command[0] == 'cat'):
                return manager.file_output(command[1])
            elif (command[0] == 'rm'):
                return manager.file_remove(command[1])
                
            elif (command[0] == 'cp'):
                return manager.file_copy(command[1], command[2])
                
            elif (command[0] == 'mv' ):
                return manager.file_replace(command[1], command[2])
                
            elif (command[0] == 'fileRename'):
                return manager.file_rename(command[1], command[2])
        
            # elif (command[0] == 'stop'):
            #     break
            else:
                return f"\033[31mНеверный ввод!\033[39m"
        else:
            return "Место в папке закончилось(((("
    except FileNotFoundError:
        return f"\033[31mФайл или директория не найдены!\033[39m"
    except FileExistsError:
        return f"\033[31mНевозможно создать файл, так как он уже существует\033[39m"
    except Exception:
        return f"\033[31mОшибка\033[39m"