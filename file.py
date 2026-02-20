import os
import shutil

from typing import List

class File:
    """Класс File используется для работы с файлами

    Основное применение - создание и редактирование файлов

    Note:
        Это ещё сырое приложение, будьте осторожны!)
    
    Attributes
    ----------
    file_name : str
        название файла
    create 
        создание файла

    Methods
    -------
    create_file()
        Создаёт файл
    write_to_file(text="Ваш текст")
        Вносит в файл информацию(текст)
    add_to_file(text="Ваш добавленный текст")
        Вносит в текст дополнения, не удаляя прошлые
    read_file
        Прочитывает файл и возвращает содержимое
    delete_file
        Удаляет файл
    rename_file("Новое название")
        Переименовывает файл
    copy_file("Путь копии")
        Копирует файл с содержимым в указанное место
    """

    def __init__(self,file_name: str,create: bool):
        self.file_name = file_name
        self.create = create

        if create == True:
            self.create_file()
        
    def create_file(self):
        '''Метод создания файла'''
        my_text: str= ""
        with open(self.file_name, "w") as my_file:    
            my_file.write(my_text)

    def write_to_file(self,text: str):
        '''Метод внесения информации в файл'''
        try:
            with open(self.file_name, "w") as my_file:    
                my_file.write(text)
        except:
            print("Произошла ошибка. Проверьте файл или его сущестование")
            exit()

    def add_to_file(self,text: str):
        '''Метод добавления информации в файл'''
        try:
            with open(self.file_name, "a") as my_file:    
                my_file.write(text)
        except:
            print("Произошла ошибка. Проверьте файл или его сущестование")
            exit()

    def read_file(self):
        '''Метод прочитывания содержимого файла'''
        try:
            with open(self.file_name, "r") as my_file:
                file_contents = my_file.read()
            return file_contents
        except:
            "Произошла ошибка. Возможно файл пустой. Попробуйте еще раз!"
            exit()

    def delete_file(self):
        '''Метод удаления файла'''
        try:
            os.remove(self.file_name)
        except:
            "Произошла ошибка. Проверьте существование файла."
            exit()

    def rename_file(self,new_name: str):
        '''Метод переименования файла'''
        try:
            os.rename(self.file_name, new_name)
        except:
            "Произошла ошибка. Проверьте существование файла."
            exit()

    def copy_file(self,path_to_copy: str):
        '''Метод копирования файла'''
        try:
            shutil.copy(self.file_name,dst=path_to_copy, follow_symlinks=True)
        except:
            "Произошла ошибка. Проверьте существование файла или путь к копии."
            exit()