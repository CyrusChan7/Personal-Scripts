from invitefriend import InviteFriend
from configparser import ConfigParser  # This is a built-in Python library
import time
import os
import sys


if __name__ == "__main__":
    # Change to directory where this Python script is located
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    os.chdir(dir_name)

    # Instantiation
    config = ConfigParser()
    try:
        config.read("config.ini")
        file_name = config.get("General", "filename")
        inv_count = config.getint("General", "friend_invite_count")
        delay_before_exec = config.getint("General", "start_delay")
        invite_people = InviteFriend(file_name, inv_count, delay_before_exec)
    except:
        print(f"config.ini file does not exist in the script's directory, or the values are incorrect. "
              f"Exiting script in 5 seconds.")
        time.sleep(5)
        sys.exit()

    invite_people.focus_game_window()
    invite_people.invite_friends()

    # Print and update message dynamically
    for i in range(5, 0, -1):
        sys.stdout.write("\rScript will automatically exit in %i second(s)." % i)
        sys.stdout.flush()
        time.sleep(1)
