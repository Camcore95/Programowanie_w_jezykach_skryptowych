import os
import sys

thisFile = sys.argv[1]
base = os.path.splitext(thisFile)[0]
os.rename(thisFile, base + ".png")
