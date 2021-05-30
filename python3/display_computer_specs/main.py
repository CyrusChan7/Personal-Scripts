import platform
import psutil


def convert_bytes_to_GB(bytes_number):
    """ Convert a number in bytes to a number in GB, then round to 4 digits """
    GB_number = bytes_number / (1024 ** 3)
    GB_number = round(GB_number, 4)
    return GB_number


def display_basic_info():
    """ A cross-platform way to display the basic information on a computer """

    print(f"Computer's network name: {platform.node()}")
    print(f"OS name: {platform.system()}")
    print(f"OS version: {platform.platform()}")
    print(f"Installed Python version: {platform.python_version()}")
    print(f"Full CPU name: {platform.processor()}")
    print(f"Machine type: {platform.machine()}")
    print(f"Total CPU count: {psutil.cpu_count()}") 
    print(f"Physical CPU count: {psutil.cpu_count(logical=False)}")


def display_RAM_info():
    """ A cross-platform way to display the RAM information on a computer"""

    installed_RAM = psutil.virtual_memory().total
    available_RAM = psutil.virtual_memory().free
    used_RAM = psutil.virtual_memory().used

    installed_RAM_GB = convert_bytes_to_GB(installed_RAM)
    available_RAM_GB = convert_bytes_to_GB(available_RAM)
    used_RAM_GB = convert_bytes_to_GB(used_RAM)

    print(f"Installed RAM: {installed_RAM_GB} GB (Used: {used_RAM_GB} GB. Available: {available_RAM_GB} GB)")


def main():
    display_basic_info()
    display_RAM_info()


if __name__ == "__main__":
    main()
