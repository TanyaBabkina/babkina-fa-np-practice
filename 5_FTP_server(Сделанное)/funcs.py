
from FuncsForManager.FileManager import *
import logging
from datetime import datetime

logging.basicConfig(filename="C:\\Users\\1\\Desktop\\babkina-fa-np-practice\\5_FTP_server(Сделанное)\\logfileForManagerOperations.txt",
                    filemode='a',
                    level=logging.INFO)

MAXSIZE = 1024*1 # килобаайт * 3



def folder_size(path, max_size=MAXSIZE):
    size = 0
    for ele in os.scandir(path):
        size += os.stat(ele).st_size
    if max_size-size <= 0:
        return 0
    else:
        return 1



def process(req, root, manager):
    logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] the command was received [{req}]')
    command = req.split()

    try:
        logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Memmory test')
        if folder_size(root) or root[-17:] == "FileManagerFolder":
            logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Memmory test OK')
            if (command[0] == 'mkdir'):
                rez = manager.create_dir(command[1])
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Dir "{command[2]}" created')
                return rez
            if req == 'pwd':
                rez = manager.PWD()
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Pwd shown')
                return rez
            elif req == 'ls':
                rez = manager.AllDirs()
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] outputting existing repositories')
                if rez == "":
                    rez = "Пустой репозиторий"
                return rez
            elif req == "su":
                manager.su_command()
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Root mode')
                return "Вы перешли в режим супер-пользователя"
            elif (command[0] == 'rmdir'):
                rez = manager.delete_dir(command[1])
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Delete repos "{command[1]}"')
                return rez 
            elif (command[0] == 'cd'):
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Change repos on "{command[1]}"')
                rez = manager.change_dir(command[1])
                return rez 
            elif (command[0] == 'touch'):
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Create file "{command[1]}"')
                rez = manager.create_file(command[1])
                return rez
            elif (command[0] == 'echo'):
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Input in file "{command[1]}"')
                rez = manager.file_input(command[1], ' '.join(command[2:]))
                return rez 
            elif (command[0] == 'cat'):
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Output fron file "{command[1]}"')
                rez = manager.file_output(command[1])
                return rez 
            elif (command[0] == 'rm'):
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Delete file "{command[1]}"')
                rez = manager.file_remove(command[1])
                return rez 
                
            elif (command[0] == 'cp'):
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Copy file "{command[1]}"')
                rez = manager.file_copy(command[1], command[2])
                return rez
                
            elif (command[0] == 'mv' ):
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Move file "{command[1]}"')
                rez = manager.file_replace(command[1], command[2])
                return rez
                
            elif (command[0] == 'fileRename'):
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Rename file "{command[1]}" to "{command[2]}"')
                rez = manager.file_rename(command[1], command[2])
                return rez 
            elif (command[0] == 'copyFileToClient'):
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Copy file "{command[1]}" to client "{command[2]}"')
                rez = manager.copyFileToClient(command[1])
                return rez
            elif (command[0] == 'copyFileToServer'):
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Copy file "{command[1]}" to server "{command[2]}"')
                rez = manager.copyFileToServer(command[2])
                return rez
            else:
                logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Wronge command')
                return f"\033[31mНеверный ввод!\033[39m"
        else:
            logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Not enought space')

            return "Место в папке закончилось(((("
    except FileNotFoundError:
        logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] No such file or derectory')
        return f"\033[31mФайл или директория не найдены!\033[39m"
    except FileExistsError:
        logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] file or derectory already exists')
        return f"\033[31mНевозможно создать файл, так как он уже существует\033[39m"
    except Exception:
        logging.info(f'[{datetime.now().strftime("%H:%M:%S")}] Some error')
        return f"\033[31mОшибка\033[39m"