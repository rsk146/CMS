import shutil

for i in range(3, 32):
    name = "nano" + str(i)
    filename = "%s.py" % name
    shutil.copyfile("nano0.py", filename)
