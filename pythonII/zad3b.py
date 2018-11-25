import xml.sax


class StudentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.name = ""
        self.surname = ""
        self.index = ""
        self.address = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "student":
            print("*****Student*****")

    def endElement(self, tag):
        if self.CurrentData == "name":
            print("Name:", self.name)
        elif self.CurrentData == "surname":
            print("Surname:", self.surname)
        elif self.CurrentData == "index":
            print("Index:", self.index)
        elif self.CurrentData == "address":
            print("Address:", self.address)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "surname":
            self.surname = content
        elif self.CurrentData == "index":
            self.index = content
        elif self.CurrentData == "address":
            self.address = content


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = StudentHandler()
parser.setContentHandler(Handler)
parser.parse("note.xml")



