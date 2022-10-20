
import os

# check if file or directory
os.path.isfile("bob.txt")
os.path.isdir("bob")

# check if a file exists
os.path.exists("/home/wolf/package.txt")

# list names of files and folders in a directory without path
name_list = os.listdir('/home/wolf')
print(name_list)

#
dir_list = next(os.walk('/home/wolf'))[1]
print(dir_list)

subdirs = [x[0] for x in os.walk('/home/wolf')]
print(subdirs)


# os.walk
for root, dirs, files in os.walk("/home/wolf/"):
    print(f"{root},---- {dirs},--- {files}")