#-*- coding: windows-1250 -*-
import codecs
import sys

inFile = sys.argv[1]
outFile = "outfile.txt"

delete_list = {"się ", "i ", "oraz", "nigdy", "dlaczego"}
textIn = codecs.open(inFile, "r", "windows-1250")
textOut = codecs.open(outFile, "w+", "windows-1250")

for line in textIn:
    for word in delete_list:
        line = line.replace(word, "")
    textOut.write(line)

textIn.close()
textOut.close()
