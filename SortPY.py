import glob, shutil, os

os.chdir("C:\\Users\\Roby\\Downloads")


#TO DOCUMENTS#

for files in glob.glob("*.pdf"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\documents\\")


for files in glob.glob("*.doc"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\documents\\")


for files in glob.glob("*.docx"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\documents\\")


for files in glob.glob("*.txt"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\documents\\")


for files in glob.glob("*.rtf"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\documents\\")


for files in glob.glob("*.tex"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\documents\\")


for files in glob.glob("*.odt"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\documents\\")

#TO MUSIC#

for files in glob.glob("*.wma"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.wav"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.mp3"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.ra"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.ram"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.rm"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.mid"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.ogg"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

#TO PICTURES#

for files in glob.glob("*.tiff"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.png"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.tif"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.gif"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.jpg"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.jpeg"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.jif"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.jfif"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.jp2"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.jpx"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.j2k"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.j2c"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.pcd"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")

for files in glob.glob("*.fpx"):
    shutil.move(files, "C:\\Users\\Roby\\Downloads\\music\\")
