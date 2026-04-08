class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        
    def __str__(self):
        return f'"{self.title}" ({self.pages} pages)'
        
    def __add__(self, other):
        return self.pages + other.pages

b1 = Book('Python 101', 300)
b2 = Book('Advanced Python', 500)
print(b1)
print('Total pages of both books:', b1 + b2)