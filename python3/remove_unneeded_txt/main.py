import os


class TxtFile:
    def __init__(self, file_path):
        self._file_path = file_path
        self._txt_file_names_record = []


    def display_directory_statistics(self):
        txt_file_names = []

        all_files_counter = 0
        txt_file_counter = 0

        for file in os.listdir(self._file_path):
            all_files_counter += 1
            if file.endswith(".txt"):
                txt_file_counter += 1
                txt_file_names.append(file)

        txt_file_percentage = round(txt_file_counter / all_files_counter * 100, 2)

        print(f"There are {all_files_counter} files in '{self._file_path}', of which {txt_file_counter} "
              f"({txt_file_percentage}%) are .txt files.")

        print(f"\nNames of the .txt files in this directory: {txt_file_names}")

        self._txt_file_names_record = txt_file_names


    def display_file_content(self, read_line_count=7):
        # 5 may not be enough lines to understand the context of the file, 10 is too spammy in the console, 7 is good
        for txt_file in self._txt_file_names_record:
            with open(txt_file) as f:
                head = f.readlines()[0:read_line_count]
            #print(head)

            print(f"\nFile contents in {txt_file}:\n")
            for line in head:
                print(line.strip()) 


if __name__ == "__main__":
    # Change to directory where this Python script is located
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    os.chdir(dir_name)

    folder_cleanup = TxtFile(dir_name)
    folder_cleanup.display_directory_statistics()
    folder_cleanup.display_file_content()
