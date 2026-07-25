import os
# Specify the directories you want to list
directory_path = '/Kajal/Python'

#List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)