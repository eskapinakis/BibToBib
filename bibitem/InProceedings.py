class InProceedings:

    key = ""
    title = ""
    authors = ""
    booktitle = ""
    year = ""
    pages = ""

    def __init__(self, key, title, authors, year, booktitle, pages):
        self.key = key
        self.title = title
        self.authors = authors
        self.year = year
        self.booktitle = booktitle
        self.pages = pages

    def printItem(self):
        toprint = "\\bibitem{" + self.key + "}\n" + \
                  self.authors + ".\n" + \
                  "\\newblock " + self.title + ".\n" + \
                  "\\newblock " + self.booktitle + ", " +\
                  ": " + self.pages + ", " + self.year + "."
        return self.fixToPrint(toprint)

    @staticmethod
    def fixToPrint(toprint):
        toprint = toprint.replace(", ,", ",")
        toprint = toprint.replace("()", "")
        toprint = toprint.replace(" : ,", "")
        toprint = toprint.replace(", :", ":")
        return toprint
