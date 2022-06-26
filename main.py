import os, shutil, errno
from aifc import Error

#os will create the folders in C:
#shutil will move the folder to the folder the place the user want
folderpath = input("Type where you want your folders to be created: ")

#os will rename the folder
input_filename = input("Type the filename you desired: ")

#separte the filename with space
filename = input_filename.split()

#check the number of object in the list, and decide which function should be used
list_length = len(filename)

#it will printed out when the folder are able to be created
def suscess_msg():
    print(str(list_length) + " " + "folders created successfully")

#if the folder existed already, it will stop it from being over written
def fail_msg():
    print("Folders cannot be created, try again")
    if Error.errno != errno.EEXIST:
        raise

def main(list_length):
    try:
        #times it will be executed is what user typed
        for list_next in range(list_length):
            os.makedirs(r'C:\\' + filename[list_next])
            shutil.move("C:\\"+ filename[list_next], folderpath)
            #move on and do the same thing for the next folder
            list_next += 1
        suscess_msg()
    except OSError as e:
        fail_msg()

main(list_length)