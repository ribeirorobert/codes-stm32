# Flashing STM32 Firmware with Python
# Created by Robert Ribeiro, February 17, 2024.
# All rights reserved.

import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def run_executable_in_directory(directory_path, command):
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print("ERROR: Directory does not exist.")
        return

    # Set the working directory
    os.chdir(directory_path)

    # Execute the command
    subprocess.run(command, shell=True)


def select_directory():
    # Check if the directory path has already been saved
    if os.path.isfile("selected_directory.txt"):
        with open("selected_directory.txt", "r") as file:
            directory_path = file.read().strip()
            # print("Using previously selected directory:", directory_path)
            return directory_path

    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to select a directory
    directory_path = filedialog.askdirectory()

    # Save the selected directory path to a file
    with open("selected_directory.txt", "w") as file:
        file.write(directory_path)

    return directory_path


# DO NOT CHANGE THE FOLLOWING LINES
# call STM32 Programmer executable
programmer = r"STM32_Programmer_CLI -c "    

# port, freq, mode and verbosity level
connection = "port=swd freq=4000 mode=normal -vb 3 -w "

# get file path
file_path = os.getcwd()

# get folder where .bin file is located
file_folder = "build\debug\\build"

# get file name
file_name = os.path.basename(os.getcwd())

# set file format
file_format = ".bin"

# flash start address and run after programming
flash_address = " 0x08000000 -s 0x08000000"

command = programmer + connection + file_path + '\\' + file_folder + '\\' + file_name + file_format + flash_address
# example: <INSTALL_PATH>STM32CubeProgrammer\bin\STM32_Programmer_CLI -c port=swd freq=4000 mode=normal -vb 3 -w <FILE_PATH>\build\debug\build\<FILE_NAME>.bin 0x08000000 -s 0x08000000"



# ONLY CHANGE HERE!!! STM32CubeProgrammer directory
# set manually
# programmer_directory = r"C:\Program Files\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin"
# or
programmer_directory = select_directory()



run_executable_in_directory(programmer_directory, command)