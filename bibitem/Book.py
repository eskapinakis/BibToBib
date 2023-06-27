class Book:

    key = ""
    title = ""
    authors = []
    year = ""
    publisher = ""

    def __init__(self, key, title, authors, year, publisher):
        self.key = key
        self.title = title
        self.authors = authors
        self.year = year
        self.publisher = publisher

    def printItem(self):
        toprint = "\\bibitem{" + self.key + "}\n" +\
                  self.authors + ".\n" +\
                  "\\newblock " + self.title+".\n" +\
                  "\\newblock " + self.publisher + ", " + self.year + "."
        return self.fixToPrint(toprint)

    @staticmethod
    def fixToPrint(toprint):
        toprint = toprint.replace(", ,", ",")
        toprint = toprint.replace("()", "")
        toprint = toprint.replace(" : ,", "")
        toprint = toprint.replace(", :", ":")
        return toprint
