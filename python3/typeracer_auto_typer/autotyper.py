import pyautogui as p
import time
import random
import sys


class AutoTyper:
    """
    Represents a class that automatically types a phrase from a file.txt using the pyautogui library

    :param file_of_phrase: Name of the file where the phrase is located and read from
    :type file_of_phrase: str
    """
    def __init__(self, file_of_phrase):
        """
        Initialization of instance attributes
        """
        self._file_of_phrase = file_of_phrase
        self._phrase_to_type = self.create_phrase_to_type()

    def create_phrase_to_type(self):
        """
        Behaviour: Reads from a file.txt and stores it inside a variable, taking corner cases into account
        """
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
        """
        Behaviour: Automatically types the given phrase
        """
        print("The script will begin typing automatically in 5 seconds.")
        print(f"\n\nPhrase to type: \n{self._phrase_to_type}")
        time.sleep(5)

        p.write(self._phrase_to_type, interval=random.uniform(0.071, 0.081))
        print("\nAutomatic typing finished successfully.\n\n\n")

        # Print and update message dynamically
        for i in range(5, 0, -1):
            sys.stdout.write("\rScript will automatically exit in %i second(s)." % i)
            sys.stdout.flush()
            time.sleep(1)