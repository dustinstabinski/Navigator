from __future__ import absolute_import
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
    name = raw_input(u'''Name the folder.
''')

    response = raw_input(u'''What would you like?
''')

    if response == u"" or name == u"" or response == u" ":
        print u"Invalid"
    else:
        trial = 1
        amount = 0
        try:
            num2 = len_of_dir(unicode(os.path.expanduser(u"~")) + u"/Desktop" + u"/" + name)
            if num2 == 0:
                num2 = 1
        except:
            num2 = 1
        if not os.path.isdir(name):
            os.mkdir(name)
        destination_dir = os.path.join(os.getcwdu(), name)
        for path, dirnames, filenames in os.walk(os.getcwdu()):
            if response.lower() in path.lower():
                for file in filenames:
                    file_name = os.path.join(path,file)
                    extension = u""
                    full_name = u""
                    num = -4
                    while num < 0:
                        extension += unicode(file_name)[num]
                        num += 1
                    # puts file in new directory
                    if not file.startswith(u'.'):
                        shutil.copyfile(file_name, os.path.join(destination_dir, u"File_" + unicode(num2) + extension))
                        amount += 1
                        num2 += 1
                time.sleep(.001)
                print u"Attempt " + unicode(trial) + u": Files found!"
                trial = trial + 1
            else:
                time.sleep(.001)
                print u"Attempt " + unicode(trial) + u": Could not find any \"" + response + u"\" files"
                trial = trial + 1
            for file_title in filenames:
                if response.lower() in file_title.lower():
                    file_title = os.path.join(path, file_title)
                    extension = u""
                    num = -4
                    while num < 0:
                        extension += unicode(file_title)[num]
                        num += 1
                    if not file_title.startswith(u'.'):
                        shutil.copyfile(file_title, os.path.join(destination_dir, u"File_" + unicode(num2) + extension))
                        amount += 1
                        num2 += 1
                        time.sleep(.001)
                        print u"Attempt " + unicode(trial) + u": Files found!"
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
        print u'\033c'
        if trial > 1 and amount > 0:
            time.sleep(1)
            print u"SUCCESS: I was able to find " + unicode(amount) + u" files for you. I placed them in a folder called " + unicode(name) + u"."
            print u"PLEASE NOTE that the original files still exist. These are renamed copies of the originals."
        else:
            print u"FAILED: I could not find any files related to " + response + u"."
#_____________________________________________________________________________________________________________________________________
copy_it()
