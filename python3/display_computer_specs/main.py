import platform
import psutil


def display_computer_info():

    print(f"Computer's network name: {platform.node()}")
    print(f"OS name: {platform.system()}")
    print(f"OS version: {platform.platform()}")
    print(f"Installed Python version: {platform.python_version()}")
    print(f"Full CPU name: {platform.processor()}")
    print(f"Machine type: {platform.machine()}")
    print(f"Total CPU count: {psutil.cpu_count()}") 
    print(f"Physical CPU count: {psutil.cpu_count(logical=False)}")


def main():
    display_computer_info()


if __name__ == "__main__":
    main()
