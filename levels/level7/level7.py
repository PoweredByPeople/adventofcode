"""
Day 7! Got stuck on this one, my code is below, got really close, just unable to figure out how to
handle adding the sum of the current directory to all the parent directories. 
"""

from collections import defaultdict

def directory_size(filename):
    """
    Read each line of the file, create a dictionary on the fly where the key is the directory
    absolute path and the value is the sum of the data in the directory. If this is the first
    time visiting the directory, give it a default value of zero and then process and sum the 
    file sizes that come after it.
    How to implement: Start by parsing the file and remove the $s and dir listings. In order
    to return the correct result we need to update the size of every parent directory along 
    with the current dir when addiing files. """



    with open (filename, encoding="utf-8") as data_input:
        file = data_input.read().splitlines()
        directories = defaultdict(int)
        cwd = ""

        for line in file:
            if line.startswith("dir") or line.startswith("$ ls"):
                continue
            elif line.startswith("$ cd .."):
                # if the line is cd .., update cwd and remove a single directory from the path.
                # else: the next argument is a directory to enter, then go into that dir
                # and update cwd and append the child dir to the path.
                # if the next argument is ".." 
                #directories[line] = sum(files)
                child_dir = cwd.rsplit("/", 2)[1]
                cwd = cwd.removesuffix(child_dir + "/")
            elif line.startswith("$ cd /"):
                cwd = "/"
            elif line.startswith("$ cd "):
                cwd = cwd + line.removeprefix("$ cd ") + "/"
            elif line[0].isdigit():
                num = []
                for digit in line:
                    if digit.isdigit():
                        num.append(digit)
                num = ''.join(num)
                num = int(num)

                directories[cwd] += num
                parent_dir = cwd.rsplit("/")
                parent_dirs = []
                for i in parent_dir:
                    for j in parent_dir[1:]:
                        if i and j != '':
                            parent_dirs += ''.join("/" + i + "/" + j + "/")
                if parent_dirs:
                    for each_dir in parent_dirs:
                        directories[each_dir] += num
                # Also update every parent directory using something similar to the rsplit child
                # dir from above line starts with cd ..
            print(line)
    
    #total = 0
    for directory in directories.keys():
        #if directories[directory] < 100000:
            #total += directories[directory]
        print(f"Directory {directory} file size is: {directories[directory]}")

    #print(f"Sum total of all directories under 100000 is: {total}.")

    # Now we just need to aggregate the directorys 
directory_size("levels/level7/level7data.txt")