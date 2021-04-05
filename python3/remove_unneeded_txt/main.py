import os


class TxtFile:
    def __init__(self, file_path):
        # I will use long variable names here as I prefer to be clear
        # on exactly what they mean, as I will be using these variables a lot later
        self._file_path = file_path
        self._txt_file_names_record = []
        self._all_files_counter = 0
        self._txt_file_counter = 0


    def gather_directory_statistics(self):
        for file in os.listdir(self._file_path):
            self._all_files_counter += 1
            if file.endswith(".txt"):
                self._txt_file_counter += 1
                self._txt_file_names_record.append(file)


    @property
    def txt_file_names_record(self):
        return self._txt_file_names_record


    def display_directory_statistics(self):
        txt_file_percentage = round(self._txt_file_counter / self._all_files_counter * 100, 2)

        print(f"\nThere are {self._all_files_counter} files in '{self._file_path}', of which {self._txt_file_counter} "
              f"({txt_file_percentage}%) are .txt files.")

        print(f"\nNames of the .txt files in this directory: {self._txt_file_names_record}")


    def display_file_content(self, txt_file, read_line_count=7):
        # 5 may not be enough lines to understand the context of the file, 10 is too spammy in the console,
        # 7 as a default is good
        with open(txt_file) as f:
            head = f.readlines()[0:read_line_count]
        #print(head)

        print("")
        print("=" * 75)
        print(f"File contents in {txt_file}:\n")
        for line in head:
            print(line.strip())


    def ask_user_for_decision(self, file_name):
        user_response = ""
        valid_response = False
        while valid_response == False:
            user_response = input(f"\nWould you like to skip or delete {file_name}? (s/d): ").lower()
            if user_response == "s" or user_response == "skip":
                valid_response = True
                print("File skipped. No action will be taken.\n")

            elif user_response == "d" or user_response == "delete":
                valid_response = True
                os.remove(file_name)
                print("File deleted successfully.\n")

            else:
                print("ERROR: Invalid input received. Type either 's' or 'd' without the quotations.")



if __name__ == "__main__":
    # Change to directory where this Python script is located
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    os.chdir(dir_name)

    folder_cleanup = TxtFile(dir_name)
    folder_cleanup.gather_directory_statistics()
    folder_cleanup.display_directory_statistics()

    for file in folder_cleanup.txt_file_names_record:
        folder_cleanup.display_file_content(file, 7)
        folder_cleanup.ask_user_for_decision(file)

    print("All .txt files have been processed.")