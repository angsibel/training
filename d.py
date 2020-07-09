class Notebook:
    colour = 'Синий'
    property = 'Закрыто'
    data = {}

    def __init__(self, pages):
        self.pages = pages

    def open(self):
        self.property = 'Открыто'

    def close(self):
        self.property = 'Закрыли'

    def write(self, number_pages, text):
        if self.property == 'Открыто' and self.pages >= number_pages:
            self.data[number_pages] = text

    def read(self, tally):
        return self.data[tally]


notebook1 = Notebook()