"""Your one-stop for all file management options, like deleting unwanted files, moving files/folders to
   a different directory path, creating folders/files"""
import os, shutil, sys
from time import sleep


def create_folder(folder_name: str = None):

    try:
        # Check if the folder already exists
        if not os.path.exists(folder_name):
            # Create the folder if it doesn't exist
            os.mkdir(folder_name)
        else:
            pass
        return os.path.abspath(folder_name)
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


class Folder:

    def __init__(self, path_to_folder: str = None):

        self.one = 1
        self.path_to_folder = path_to_folder

    def create_folder(self, folder_name, folder_storage_path: str = None):

        sleep(self.one)
        try:
            # Check if the folder already exists
            if not os.path.exists(folder_name):
                # Create the folder if it doesn't exist
                os.mkdir(folder_name)
                print(f"Folder '{folder_name}' created successfully.")
            else:
                print(f"Folder '{folder_name}' already exists.")

            return os.path.abspath(folder_name)
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

    def delete_all_photos(self):

        folder_path = ""
        if not OSError:
            folder_path = os.getcwd() + f'\\{self.path_to_folder}'
        elif OSError:
            folder_path = self.path_to_folder

        # List all the files in the folder
        files = os.listdir(folder_path)

        # Loop through the files and delete any non-picture files
        for file in files:
            if file.lower().endswith(".jpg") or file.lower().endswith(".png") or file.lower().endswith(".jpeg") \
                    or file.lower().endswith(".heic"):
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)
                print(f"Deleted {file_path}")

    def delete_all_videos(self):

        folder_path = ""
        if not OSError:
            folder_path = os.getcwd() + f'\\{self.path_to_folder}'
        elif OSError:
            folder_path = self.path_to_folder

        # List all the files in the folder
        files = os.listdir(folder_path)

        # Loop through the files and delete any non-picture files
        for file in files:
            if file.lower().endswith(".mp4") or file.lower().endswith(".mkv") or file.lower().endswith(".mov"):
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)
                print(f"Deleted {file_path}")

    def delete_all_documents(self):

        folder_path = ""
        if not OSError:
            folder_path = os.getcwd() + f'\\{self.path_to_folder}'
        elif OSError:
            folder_path = self.path_to_folder

        # List all the files in the folder
        files = os.listdir(folder_path)

        # Loop through the files and delete any non-picture files
        for file in files:
            if file.lower().endswith(".docx") or file.lower().endswith(".xlsx") or file.lower().endswith(
                    ".txt") or file.lower().endswith(".pptx"):
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)
                print(f"Deleted {file_path}")

    def delete_all_gifs(self):

        folder_path = ""
        if not OSError:
            folder_path = os.getcwd() + f'\\{self.path_to_folder}'
        elif OSError:
            folder_path = self.path_to_folder

        # List all the files in the folder
        files = os.listdir(folder_path)

        # Loop through the files and delete any non-picture files
        for file in files:
            if file.lower().endswith(".gif"):
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)
                print(f"Deleted {file_path}")

    def delete_all_audios(self):

        folder_path = ""
        if not OSError:
            folder_path = os.getcwd() + f'\\{self.path_to_folder}'
        elif OSError:
            folder_path = self.path_to_folder

        # List all the files in the folder
        files = os.listdir(folder_path)

        # Loop through the files and delete any non-picture files
        for file in files:
            if file.lower().endswith(".mp3"):
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)
                print(f"Deleted {file_path}")

    def delete_all_chrome_html_documents(self):

        folder_path = ""
        if not OSError:
            folder_path = os.getcwd() + f'\\{self.path_to_folder}'
        elif OSError:
            folder_path = self.path_to_folder

        # List all the files in the folder
        files = os.listdir(folder_path)

        # Loop through the files and delete any non-picture files
        for file in files:
            if file.lower().endswith(".webp"):
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)
                print(f"Deleted {file_path}")

    def delete_duplicate_files(self):

        print(self.path_to_folder)


class Move:

    def __init__(self, path_to_file, path_to_folder=None):

        self.path_to_file = path_to_file
        self.path_to_folder = path_to_folder

    def to(self, path):
        if self.path_to_file:
            shutil.move(self.path_to_file, path)
        elif self.path_to_folder:
            shutil.move(self.path_to_folder, path)


class CategoriseFilesIntoFolders:

    def __init__(self, directory_containing_the_files: str):

        self.one = 1
        self.directory_path = directory_containing_the_files

    def by_similar_filenames(self, similarity_threshold: int):

        folder_path = os.getcwd() + f'\\{self.directory_path}' if not OSError else self.directory_path
        files = os.listdir(folder_path)
        for index, any1 in enumerate(files):
            if index < len(files) - 1:
                if any1[:similarity_threshold] == files[index + 1][:similarity_threshold]:
                    new_folder = create_folder(f"{any1[:similarity_threshold]}")
                    new_files = os.path.join(folder_path, files[index + 1])
                    Move(new_files).to(new_folder)
                elif len(files[index + 1]) < similarity_threshold or len(any1) < similarity_threshold:
                    print("Your similarity threshold is too high")
                    sys.exit(3)

    def by_similar_filetypes(self):
        sleep(self.one)

    def by_similar_file_extensions(self):
        sleep(self.one)


if __name__ == "__main__":
    # Folder(r"Paste Here").delete_all_chrome_html_documents()
    # Move("Paste Here", path_to_folder=None).to("Paste Here")
    # CategoriseFilesIntoFolders("Paste Here").by_similar_filenames(12)
    print("Hello World")
