import os

# specify the directory path
# path = '/Users/datax/Downloads/twitter sub parser/res/VitalikButerin'
path = '/var/www/twitter_sub_parser/twitter_sub_parser/res/VitalikButerin'

# get a list of all files and directories in the specified path
files_and_directories = os.listdir(path)

# iterate through each item in the list and count the number of directories
num_directories = 0
for item in files_and_directories:
    if os.path.isdir(os.path.join(path, item)):
        num_directories += 1

print("Number of directories in", path, "is", num_directories)

# import os

# # specify the directory path
# path = '/Users/datax/Downloads/twitter sub parser/res/VitalikButerin/pokerface123789'

# # get a list of all files and directories in the specified path
# files_and_directories = os.listdir(path)

# # iterate through each item in the list and count the number of files
# num_files = 0
# for item in files_and_directories:
#     if os.path.isfile(os.path.join(path, item)):
#         num_files += 1

# print("Number of files in", path, "is", num_files)
