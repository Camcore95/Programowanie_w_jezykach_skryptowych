import xml.dom.minidom as xml
import sys


output = open("note_modified.xml", "w")
sys.stdout = output

dom = xml.parse(open("note.xml"))
for element in dom.getElementsByTagName("student"):
    element.getElementsByTagName("address")[0].childNodes[0].data = "homeless"

print(dom.toxml(), end='')



