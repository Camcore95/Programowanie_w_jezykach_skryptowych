import xml.sax
import xml.sax.saxutils


class StudentHandler(xml.sax.saxutils.XMLGenerator):
    def __init__(self, handler):
        xml.sax.saxutils.XMLGenerator.__init__(self, handler)
        self.currentData = ""

    def startElement(self, content, attributes):
        self.currentData = content
        xml.sax.saxutils.XMLGenerator.startElement(self, content, attributes)

    def endElement(self, content):
        self.currentData = ""
        xml.sax.saxutils.XMLGenerator.endElement(self, content)

    def characters(self, content):
        if self.currentData == "address":
            xml.sax.saxutils.XMLGenerator.characters(self, "homeless")
        else:
            xml.sax.saxutils.XMLGenerator.characters(self, content)

filehandler1 = open("note.xml", "r")
filehandler2 = open("note_mod2.xml", "w")
xml.sax.parse(filehandler1, StudentHandler(filehandler2))


