import os
import sys
input_file = os.path.join(sys.path[0],"input_file_names.txt")
output_file = os.path.join(sys.path[0],"output_file_names.txt")
imagespath = os.path.join(sys.path[0],"Images")
file_ext = str(input("File Extension? - *.:"))
fukingdumbandroidreadnumberfilenameodering = str(input('''Support Android Ordering List Images? \n
The Android File Manager ordered the number file name as strings, \n
so if you rename the file in normal order like this: \n
"0.jpg, 1.jpg, 2.jpg,...,99.jpg",\n
it will order the files in the File Explorer like this: \n
"0.jpg, 1.jpg, 10.jpg, 11.jpg,...,2.jpg , 20.jpg, 21.jpg,..." \n
To fix that stupid sorting, we have to add zeros (0) \n
in front of the numbers 1 to 9

'''))
with open(input_file, 'r', encoding="utf-8") as i:
    names = i.readlines()

#function to rename files
def main(imagespath, names, output_file):
    count = 0
    for x in range(len(names)):
        for file in os.listdir(imagespath):
            #check if the file name is present in the name list
            if file in names[count]:
                oldName = os.path.join(imagespath, file)
                if len(names) < 10:
                    new = f'0 + {count} + {file_ext}'
                if 10 < len(names) < 100:
                newName = os.path.join(imagespath, new)

