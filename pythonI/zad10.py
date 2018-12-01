#-*- coding: windows-1250 -*-
import codecs
import sys

inFile = sys.argv[1]
outFile = "outfile.txt"

#I use additional word 'bla' to avoid changing 'i' to 'oraz' and then all 'oraz' to 'i'
replace_list = {" i ": " bla ", " oraz": " i", "nigdy": "prawie nigdy", "dlaczego": "czemu", " bla ": " oraz "}
textIn = codecs.open(inFile, "r", "windows-1250")
textOut = codecs.open(outFile, "w+", "windows-1250")

for line in textIn:
    for word in replace_list:
        line = line.replace(word, replace_list.get(word))
    textOut.write(line)

textIn.close()
textOut.close()
