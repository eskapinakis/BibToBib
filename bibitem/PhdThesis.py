class PhdThesis:

    key = ""
    title = ""
    authors = ""
    year = ""
    school = ""

    def __init__(self, key, title, authors, year, school):
        self.key = key
        self.title = title
        self.authors = authors
        self.year = year
        self.school = school

    def printItem(self):
        toprint = "\\bibitem{" + self.key + "}\n" + \
                  self.authors + ".\n" + \
                  "\\newblock " + self.title + ".\n" + \
                  "\\newblock " + self.school + ", " + self.year + "."
        return self.fixToPrint(toprint)

    @staticmethod
    def fixToPrint(toprint):
        toprint = toprint.replace(", ,", ",")
        toprint = toprint.replace("()", "")
        toprint = toprint.replace(" : ,", "")
        toprint = toprint.replace(", :", ":")
        return toprint
