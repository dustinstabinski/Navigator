import os
import shutil
import random
import time
#________________________________________________________________________________________________
#________________________________________________________________________________________________
def len_of_dir(path):
    len = 0
    for path, dirnames, filenames in os.walk(path):
        for file in filenames:
            len += 1
    return len

def copy_it():
    name = input('''Name the folder.
''')

    response = input('''What would you like?
''')

    if response == "" or name == "" or response == " ":
        print("Invalid")
    else:
        trial = 1
        amount = 0
        try:
            num2 = len_of_dir(str(os.path.expanduser("~")) + "/Desktop" + "/" + name)
            if num2 == 0:
                num2 = 1
        except:
            num2 = 1
        if not os.path.isdir(name):
            os.mkdir(name)
        destination_dir = os.path.join(os.getcwd(), name)
        for path, dirnames, filenames in os.walk(os.getcwd()):
            if response.lower() in path.lower():
                for file in filenames:
                    file_name = os.path.join(path,file)
                    extension = ""
                    full_name = ""
                    num = -4
                    while num < 0:
                        extension += str(file_name)[num]
                        num += 1
                    # puts file in new directory
                    if not file.startswith('.'):
                        shutil.copyfile(file_name, os.path.join(destination_dir, "File_" + str(num2) + extension))
                        amount += 1
                        num2 += 1
                time.sleep(.001)
                print("Attempt " + str(trial) + ": YUP!")
                trial = trial + 1
            else:
                time.sleep(.001)
                print("Attempt " + str(trial) + ": Could not find any \"" + response + "\" files")
                trial = trial + 1
            for file_title in filenames:
                if response.lower() in file_title.lower():
                    file_title = os.path.join(path, file_title)
                    extension = ""
                    num = -4
                    while num < 0:
                        extension += str(file_title)[num]
                        num += 1
                    if not file_title.startswith('.'):
                        shutil.copyfile(file_title, os.path.join(destination_dir, "File_" + str(num2) + extension))
                        amount += 1
                        num2 += 1
                        time.sleep(.001)
                        print("Attempt " + str(trial) + ": Files found!")
                        trial = trial + 1
        # attempts to move the new directory to the desktop
        # try:
        #     shutil.move(os.getcwd() + "/" + name,str(os.path.expanduser("~")) + "/Desktop")
        # # moves each file to existing directory on desktop
        # except:
        #     for path, dirnames, filenames in os.walk(os.getcwd() + "/" + name):
        #         for file in filenames:
        #             file_name = os.path.join(path,file)
        #             try:
        #                 shutil.move(file_name,str(os.path.expanduser("~")) + "/Desktop" + "/" + name)
        #             except:
        #                 print("file already exists")
        print('\033c', end=None)
        if trial > 1 and amount > 0:
            time.sleep(1)
            print("SUCCESS: I was able to find " + str(amount) + " files for you. I placed them in a folder called " + str(name) + ".")
            print("PLEASE NOTE that the original files still exist. These are renamed copies of the originals.")
        else:
            print("FAILED: I could not find any files related to " + response + ".")
#_____________________________________________________________________________________________________________________________________
copy_it()
