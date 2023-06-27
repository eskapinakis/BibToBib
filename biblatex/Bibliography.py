class Bibliography:

    items = []
    size = 0

    def __init__(self):
        self.items = []
        self.size = 0

    def addItem(self, bibItem):
        self.items.append(bibItem)
        self.size += 1

    def getItem(self, key):
        for item in self.items:
            if item.key == key:
                return item

    def sort(self):
        self.items.sort(key=lambda x: x.key)
