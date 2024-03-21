
import os
import shutil


def checkDir(root, dir):
    if root in os.path.abspath(dir):
        return "ok"
    else:
        return f'\033[31mНет доступа в данную директроию! \033[39m'

class FileManager:
    def __init__(self, root):
        self.root = root
        os.chdir(self.root)
        print(root, "in manager")

    def create_file(self, fileName):
        filepath = os.path.join(os.getcwd(), fileName)
        if checkDir(self.root, filepath) == "ok":
            file = open(filepath, "a")
            file.close()
            return f"\033[32mФайл создан\033[39m"
        else:
            return "Нет доступа в эту директорию"
    def su_command(self):
        return "Вы перешли в режим супер-пользователя"
        

    def PWD(self):
        return os.getcwd()
    def AllDirs(self):
        return '; '.join(os.listdir())
    def create_dir(self, dir_path):
        dirpath = os.path.join(os.getcwd(), dir_path)
        if checkDir(self.root, dirpath) == "ok":
            os.makedirs(dirpath) 
            return f"\033[32mДиректория создана\033[39m"
        else:
            return f'\033[31mНет доступа в данную директроию! \033[39m'

    def delete_dir(self, dir_path):
        # dirpath = os.path.join(os.getcwd(), dir_path)
        dirpath=dir_path
        if checkDir(self.root, dirpath)== "ok":
            os.removedirs(dirpath)
            return f"\033[32mДиректория удалена\033[39m"
        else:
            return f'\033[31mНет доступа в данную директроию! \033[39m'

    def change_dir(self, dir_path):
        if checkDir(self.root,  os.path.join(os.getcwd(), dir_path))== "ok":
            os.chdir(dir_path)
            return "Текущая директория: "+os.getcwd()
        else:
            return f'\033[31mНет доступа в данную директроию! \033[39m'

    def file_input(self, fileName, text):
        filepath = os.path.join(os.getcwd(), fileName)
        if checkDir(self.root, filepath)== "ok":
            file = open(filepath, "a")
            file.write(text)
            file.close()
            return f"\033[32mТекст добавлен в файл\033[39m"
        else:
            return f'\033[31mНет доступа в данную директроию! \033[39m'

    def file_output(self, fileName):
        filepath = os.path.join(os.getcwd(), fileName)
        if checkDir(self.root, filepath)== "ok":
            file = open(filepath, "r")
            file_data = file.readlines()
            file.close()
            return ''.join(file_data)
        else:
            return f'\033[31mНет доступа в данную директроию! \033[39m'

            

    def file_remove(self, fileName):
        filepath = os.path.join(os.getcwd(), fileName)
        if checkDir(self.root, filepath)== "ok":
            os.remove(filepath)
            return f"\033[32mФайл удалён\033[39m"
        else:
            return f'\033[31mНет доступа в данную директроию! \033[39m'


    def file_copy(self, src, dst):
        src_path = os.path.join(os.getcwd(), src)
        dst_path = os.path.join(os.getcwd(), dst)
        if checkDir(self.root, src_path)== "ok" and checkDir(self.root, dst_path)== "ok":
            shutil.copy(src_path, dst_path) 
            return f"\033[32mСделана копия файла\033[39m"
        else:
            return f'\033[31mНет доступа в данную директроию! \033[39m'

    def file_replace(self, src, dst):
        src_path = os.path.join(os.getcwd(), src)
        dst_path = os.path.join(os.getcwd(), dst)
        if checkDir(self.root, src_path)== "ok" and checkDir(self.root, dst_path)== "ok":
            os.replace(src_path, dst_path)
            return f"\033[32mФайл перемещён\033[39m"
        else:
            return f'\033[31mНет доступа в данную директроию! \033[39m'

    def file_rename(self, fileName, fileNameNew):
        filepath = os.path.join(os.getcwd(), fileName)
        filepath2 = os.path.join(os.getcwd(), fileNameNew)
        if checkDir(self.root, filepath)== "ok" and checkDir(self.root, filepath2)== "ok":
            os.rename(filepath, filepath2)
            return "Файл переименован"
        else:
            return f'\033[31mНет доступа в данную директроию! \033[39m'
