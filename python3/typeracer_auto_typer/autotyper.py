import pyautogui as p
import time
import random
import sys


class AutoTyper:
    def __init__(self, file_of_phrase):
        self._file_of_phrase = file_of_phrase
        self._phrase_to_type = self.create_phrase_to_type()

    def create_phrase_to_type(self):
        try:    # Success scenario
            with open(self._file_of_phrase) as f:
                phrase = f.readline().strip()   # Remove unnecessary trailing and leading characters
                phrase = phrase.replace('"', '\"')
                #print(f"DEBUG - phrase is: {phrase}")
            return phrase
        except FileNotFoundError:   # One of the most likely exceptions to occur
            print(f"ERROR: File {self._file_of_phrase} does not exist. Exiting script in 5 seconds.")
            time.sleep(5)
            sys.exit()

    def type_phrase(self):
        print("The script will begin typing automatically in 5 seconds.")
        time.sleep(5)

        print(f"\n\nPhrase to type: \n{self._phrase_to_type}")
        p.write(self._phrase_to_type, interval=random.uniform(0.071, 0.081))
        print("\nAutomatic typing finished successfully.\n\n\n")

        # Print and update message dynamically
        for i in range(5, 0, -1):
            sys.stdout.write("\rScript will automatically exit in %i second(s)." % i)
            sys.stdout.flush()
            time.sleep(1)