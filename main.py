from biblatex import Bibliography
from bibitem import Book, Article, InProceedings, PhdThesis

Bib = Bibliography.Bibliography()


def makeBib():
    bibfile = open("bibfile", "r", errors='ignore')
    lines = bibfile.readlines()
    for i in range(0, len(lines)):
        line = lines[i]
        if line[0] == "@":
            content = extract_content(lines, i)
            if "book" in line or "techreport" in line:
                makeBook(content)
            if "phdthesis" in line:
                makePhdThesis(content)
            if "inproceedings" in line:
                makeInproceedings(content)
            if "article" in line:
                makeArticle(content)
    bibfile.close()


# Get what is inside the blocks
def extract_content(lines, start):
    content = ''
    brace_count = 0
    for i in range(start, len(lines)):
        for char in lines[i]:
            if char == '{':
                brace_count += 1
            if char == '}':
                brace_count -= 1
                if brace_count == 0:
                    return content.split('\n')
            content += char
    return 0


def makeBook(Lines):
    key = title = author = year = publisher = ""
    for Line in Lines:
        if "@" in Line:
            key = Line[Line.find("{") + 1: Line.rfind(",")]
        if "title" in Line:
            title = Line[Line.find("{") + 1: Line.rfind("}")]
        if "author" in Line:
            author = Line[Line.find("{") + 1: Line.rfind("}")]
        if "year" in Line:
            year = Line[Line.find("{") + 1: Line.rfind("}")]
        if "publisher" in Line:
            publisher = Line[Line.find("{") + 1: Line.rfind("}")]
    book = Book.Book(key, title, author, year, publisher)
    Bib.addItem(book)


def makePhdThesis(Lines):
    key = title = author = year = school = ""
    for Line in Lines:
        if "@" in Line:
            key = Line[Line.find("{") + 1: Line.rfind(",")]
        if "title" in Line:
            title = Line[Line.find("{") + 1: Line.rfind("}")]
        if "author" in Line:
            author = Line[Line.find("{") + 1: Line.rfind("}")]
        if "year" in Line:
            year = Line[Line.find("{") + 1: Line.rfind("}")]
        if "school" in Line:
            school = Line[Line.find("{") + 1: Line.rfind("}")]
    phdthesis = PhdThesis.PhdThesis(key,title,author,year,school)
    Bib.addItem(phdthesis)


def makeArticle(Lines):
    key = title = author = year = volume = number = journal = publisher = pages = ""
    for Line in Lines:
        if "@" in Line:
            key = Line[Line.find("{") + 1: Line.rfind(",")]
        if "title" in Line:
            title = Line[Line.find("{") + 1: Line.rfind("}")]
        if "author" in Line:
            author = Line[Line.find("{") + 1: Line.rfind("}")]
        if "year" in Line:
            year = Line[Line.find("{") + 1: Line.rfind("}")]
        if "journal" in Line:
            journal = Line[Line.find("{") + 1: Line.rfind("}")]
        if "pages" in Line:
            pages = Line[Line.find("{") + 1: Line.rfind("}")]
        if "volume" in Line:
            volume = Line[Line.find("{") + 1: Line.rfind("}")]
        if "number" in Line:
            number = Line[Line.find("{") + 1: Line.rfind("}")]
        if "publisher" in Line:
            publisher = Line[Line.find("{") + 1: Line.rfind("}")]
    article = Article.Article(key, title, author, year, volume, number, journal, publisher, pages)
    Bib.addItem(article)


def makeInproceedings(Lines):
    key = title = author = year = booktitle = pages = ""
    for Line in Lines:
        if "@" in Line:
            key = Line[Line.find("{") + 1: Line.rfind(",")]
        if "title" in Line and "booktitle" not in Line:
            title = Line[Line.find("{") + 1: Line.rfind("}")]
        if "author" in Line:
            author = Line[Line.find("{") + 1: Line.rfind("}")]
        if "booktitle" in Line:
            booktitle = Line[Line.find("{") + 1: Line.rfind("}")]
        if "year" in Line:
            year = Line[Line.find("{") + 1: Line.rfind("}")]
        if "pages" in Line:
            pages = Line[Line.find("{") + 1: Line.rfind("}")]
    inproceedings = InProceedings.InProceedings(key, title, author, year, booktitle, pages)
    Bib.addItem(inproceedings)


def writeBib():
    file = open('bib_out.txt', 'w')
    size = 0
    latexfile = open("latexfile", "r", errors='ignore')
    contents = latexfile.read()
    Bib.sort()
    for item in Bib.items:
        if item.key in contents:
            file.write(item.printItem())
            file.write("\n\n")
            size += 1
    file.close()
    print("Number of entries: " + str(size))


def printBib():
    Bib.sort()
    for item in Bib.items:
        print(item.printItem())
        print("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    makeBib()
    # printBib()
    writeBib()
