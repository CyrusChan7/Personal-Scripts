import platform     # Native library
import psutil
import time


def convert_bytes_to_GB(bytes_number):
    """ Convert a number in bytes to a number in GB, then round to 4 digits """
    GB_number = bytes_number / (1024 ** 3)
    GB_number = round(GB_number, 4)
    return GB_number


def display_basic_info():
    """ A cross-platform way to display the basic information on a computer """

    print(f"Computer's network name: {platform.node()}\n")
    print(f"OS name: {platform.system()}\n")
    print(f"OS version: {platform.platform()}\n")
    print(f"Installed Python version: {platform.python_version()}\n")
    print(f"Full CPU name: {platform.processor()}\n")
    print(f"Machine type: {platform.machine()}\n")
    print(f"Total CPU count: {psutil.cpu_count()}\n") 
    print(f"Physical CPU count: {psutil.cpu_count(logical=False)}\n")


def display_RAM_info():
    """ A cross-platform way to display the RAM information on a computer"""

    installed_RAM = psutil.virtual_memory().total
    available_RAM = psutil.virtual_memory().free
    used_RAM = psutil.virtual_memory().used

    installed_RAM_GB = convert_bytes_to_GB(installed_RAM)
    available_RAM_GB = convert_bytes_to_GB(available_RAM)
    used_RAM_GB = convert_bytes_to_GB(used_RAM)

    print(f"Installed RAM: {installed_RAM_GB} GB (Used: {used_RAM_GB} GB. Available: {available_RAM_GB} GB)\n")


def display_disk_info():
    """ A cross-platform way to display the OS disk information on a computer"""

    total_disk_space = psutil.disk_usage("/").total
    available_disk_space = psutil.disk_usage("/").free
    used_disk_space = psutil.disk_usage("/").used

    total_disk_space_GB = convert_bytes_to_GB(total_disk_space)
    available_disk_space_GB = convert_bytes_to_GB(available_disk_space)
    used_disk_space_GB = convert_bytes_to_GB(used_disk_space)

    print(f"Total OS disk space: {total_disk_space_GB} GB (Used: {used_disk_space_GB} GB. Available: {available_disk_space_GB} GB)\n")


def main():
    display_basic_info()
    display_RAM_info()
    display_disk_info()


if __name__ == "__main__":
    start_time = time.time()    # Used to calculate script execution time
    main()
    print(f"Detection of computer information took: {round(time.time() - start_time, 6)} seconds!")
    exit_confirmation = input("Press Enter key to exit...")
