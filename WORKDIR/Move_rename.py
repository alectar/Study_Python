#! python3
import os
import shutil

def COPY_DOCS():
    for name in NAMES:
        if name[-4:] == '.jpg' or name[-4:] == '.png' or name[-4:] == 'jpeg':
            SRSNAME = os.path.join(WRKDIR, name)
            DSTNAME = os.path.join(WRKDIR+'Pictures')
            shutil.copy2(SRSNAME, DSTNAME)
            print(name)
        else:
            pass

def RENAME_FILES():
    N_WRKDIR = (WRKDIR + 'Pictures/')
    for position, n_name in enumerate(os.listdir(N_WRKDIR)):
        os.rename(N_WRKDIR + n_name, N_WRKDIR + str('IMG' + '{:04}'.format(position) + '.' + n_name.split('.')[-1]))

os.chdir('/')
WRKDIR = '/home/tarnad/SANDBOX/'
NAMES = os.listdir(WRKDIR)
if not os.path.exists(WRKDIR + 'Pictures'):
    os.makedirs(WRKDIR + 'Pictures', 0o777)
    print('Directory \'Pictures\' just created, ')
    COPY_DOCS()
    RENAME_FILES()
else:
    print('Directory \'Pictures\' exist. Files will not be copied')