class Item:

    @staticmethod
    def fixToPrint(toprint):
        toprint = toprint.replace(", ,", ",")
        toprint = toprint.replace("()", "")
        toprint = toprint.replace(" : ,", "")
        toprint = toprint.replace(", :", ":")
        return toprint
