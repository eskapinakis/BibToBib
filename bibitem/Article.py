class Article:

    key = ""
    title = ""
    authors = ""
    journal = ""
    publisher = ""
    year = ""
    volume = ""
    number = ""
    pages = ""

    def __init__(self, key, title, authors, year, volume, number, journal, publisher, pages):
        self.key = key
        self.title = title
        self.authors = authors
        self.year = year
        self.volume = volume
        self.number = number
        self.journal = journal
        self.publisher = publisher
        self.pages = pages

    def printItem(self):
        toprint = "\\bibitem{" + self.key + "}\n" +\
                  self.authors + ".\n" + \
                  "\\newblock " + self.title + ".\n" +\
                  "\\newblock " + self.journal + ", " +\
                  self.volume + "(" + self.number + "): " + self.pages + ", " + self.year + "."
        return self.fixToPrint(toprint)

    @staticmethod
    def fixToPrint(toprint):
        toprint = toprint.replace(", ,", ",")
        toprint = toprint.replace("()", "")
        toprint = toprint.replace(" : ,", "")
        toprint = toprint.replace(", :", ":")
        return toprint
