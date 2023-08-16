#ifneededdo
simple shell filter to see if a file exists if not run a command useful for doing batch scripting on a directory full of items example there is a directory of .jp2 files that I want to convert to .jpg

script tests that no / is included and that the generated command is longer than 20 characters, for safety


#Examples


find tests | python3 ./ifneededdo.py -o ".jpg" -c "cat %1 %2"

# generate and run example
find tests | python3 ./ifneededdo.py -o ".jpg" -c "cat %1 %2" | xjobs -j4
