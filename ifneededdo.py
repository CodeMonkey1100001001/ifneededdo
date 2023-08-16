#!/usr/bin/python3
# ifneededdo
# simple shell filter to see if a file exists if not run a command
# useful for doing batch scripting on a directory full of items
# example there is a directory of .jp2 files that I want to convert
# to .jpg
# find tests | python3 ./ifneededdo.py -o ".jpg" -c "cat %1 %2"
# generate and run example
# find tests | python3 ./ifneededdo.py -o ".jpg" -c "cat %1 %2" | xjobs -j4
import sys
import os.path
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description='Command line basic gcode sender for marlin polargraph')
parser.add_argument('-o', '--output', help='Output file', required=True)
parser.add_argument('-c', '--command', help='Command to run', required=True)
args = parser.parse_args()

outFile = args.output
commandEh = args.command

#print("echo inFile",inFile)
print("echo outFile",outFile)
print("echo commandEh",commandEh)

  
for line in sys.stdin:
    line = line.strip()

    baseNameLine = Path(line).resolve().stem

    print("#" + line , "bnl", baseNameLine )
    newFile = baseNameLine + outFile
    if os.path.isfile(newFile) is False:
        newCommand=commandEh.replace("%1",line)
        newCommand=newCommand.replace("%2",newFile)
        cleanCommandEh = False
        
        if len(newCommand) > 20 :
            cleanCommandEh = True
        
        if newCommand.count("/") > 2:
            cleanCommandEh = False


        if (cleanCommandEh == True):
            print(newCommand)
        else:
            print("echo BADDDDD",newCommand)
