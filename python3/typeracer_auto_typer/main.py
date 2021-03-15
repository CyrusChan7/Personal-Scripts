from autotyper import AutoTyper
import os


if __name__ == "__main__":
    # Change to directory where this Python script is located
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    os.chdir(dir_name)

    auto_typer = AutoTyper("phrase.txt")
    auto_typer.type_phrase()
