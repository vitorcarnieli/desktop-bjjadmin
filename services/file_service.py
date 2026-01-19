import json
import os
import re
import shutil
from pathlib import Path
from uuid import uuid4


class FileService:
    @staticmethod
    def get_file_name(path: str):
        file_name = Path(path).stem
        return file_name

    @staticmethod
    def get_basename(path: str):
        return os.path.basename(path)

    @staticmethod
    def get_folder_path(file_path: str):
        return str(Path(file_path).parent.resolve())

    @staticmethod
    def create_folder(path: str):
        try:
            # Check whether the specified path exists or not
            isExist = os.path.exists(path)

            if not isExist:
                # Create a new directory because it does not exist
                os.makedirs(path)
                return True
            return True
        except Exception as e:
            return False

    @staticmethod
    def copy_file(source_path: str, target_path: str):
        try:
            source_path_full = os.path.realpath(os.path.join(os.getcwd(), source_path))
            if os.path.exists(source_path_full):
                shutil.copy(source_path, target_path)
                return True
            else:
                return False
        except Exception as e:
            return False

    @staticmethod
    def remove_file(path: str):
        try:
            __location__ = os.path.realpath(os.path.join(os.getcwd(), path))
            if os.path.exists(__location__):
                os.remove(__location__)
                return True
        except Exception as e:
            return False

        return False

    @staticmethod
    def remove_folder(path: str):
        try:
            __location__ = os.path.realpath(os.path.join(os.getcwd(), path))
            if os.path.exists(__location__):
                shutil.rmtree(__location__)
                return True
        except Exception as e:
            return False

        return False

    @staticmethod
    def rename_file(old_name, new_name):
        try:
            os.rename(old_name, new_name)
            return True, ""
        except FileExistsError as e:
            return False, "Já existe um arquivo com esse nome"
        except FileNotFoundError as e:
            return False, "Arquivo não encontrado"
        except Exception as e:
            return False, str(e)

    @staticmethod
    def get_file_extension(path: str):
        file_extension = Path(path).suffix
        return file_extension

    @staticmethod
    def get_header_file(file_path):
        header = []
        with open(file_path, 'r', encoding='utf-8') as f:
            contents = f.readlines()
            if len(contents) > 0:
                data_header = contents[0].split(';')

                header = []
                for column in data_header:
                    column_value = column.replace("\n", "")
                    header.append(column_value)

        return header

    @staticmethod
    def get_documents_path():
        try:
            documents_path = os.path.join(os.getenv('USERPROFILE'), 'Documents')
            return documents_path
        except Exception as e:
            return ""

    @staticmethod
    def move_file_to_storage(file_path):
        if not file_path:
            return None
        FileService.create_folder("storage")
        file_name_uuid = str(uuid4())
        extension_file = FileService.get_file_extension(file_path)
        new_path = "storage\\" + file_name_uuid + extension_file
        FileService.copy_file(file_path, new_path)
        return new_path

    @staticmethod
    def get_pictures_path():
        try:
            images_path = os.path.join(os.getenv('USERPROFILE'), 'Pictures')
            return images_path
        except Exception as e:
            return ""

    @staticmethod
    def delete_all_files_in_directory(directory_path: str) -> bool:
        try:
            if not os.path.isdir(directory_path):
                return False
            files = os.listdir(directory_path)
            for file in files:
                file_path = os.path.join(directory_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            return True
        except Exception as e:
            return False

    @staticmethod
    def move_file(source, target):
        try:
            shutil.move(source, target)
            return True
        except Exception as e:
            return False

    @staticmethod
    def list_file_names(directory):
        if not os.path.isdir(directory):
            raise ValueError(f"The directory '{directory}' does not exist.")

        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        return files

    def get_full_path(base_dir, relative_path):
        full_path = os.path.join(base_dir, relative_path)
        return os.path.abspath(full_path)
