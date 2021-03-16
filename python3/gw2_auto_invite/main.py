from invitefriend import InviteFriend
import time
import os
import sys


if __name__ == "__main__":
    # Change to directory where this Python script is located
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    os.chdir(dir_name)

    invite_people = InviteFriend("names.txt", 3)
    invite_people.focus_game_window()
    invite_people.invite_friends()

    # Print and update message dynamically
    for i in range(5, 0, -1):
        sys.stdout.write("\rScript will automatically exit in %i second(s)." % i)
        sys.stdout.flush()
        time.sleep(1)
