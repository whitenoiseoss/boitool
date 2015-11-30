#!/usr/bin/python3
from archive.archive import Archive
from boitool.boitool import BoITool
from utils.helpers import errprint
import re


def main():
    while True:
        print(COMMAND_PROMPT, end="", flush=True)
        command = re.match(r"^[\w\s]{1,40}$", input().strip())
        if command:
            print("You entered:", command.group())
            command = command.group().split(' ')
            print("Full:", command)
            print("Command:", command[0])
            print("Arguments:", command[1:])
        else:
            errprint("Invalid command")


if __name__ == "__main__":
    print(HEADER)
    boitool = BoITool()
    main()
