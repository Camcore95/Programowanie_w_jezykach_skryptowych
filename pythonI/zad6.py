import os

thisFile = "/home/ute/labybash/pythonI/b.jpg"
base = os.path.splitext(thisFile)[0]
os.rename(thisFile, base + ".png")
