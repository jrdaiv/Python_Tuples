library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# print(library)
def book(library, title, author):
    if (title, author) in library:
        print(f"{title} written by: {author} is already added to the library. ")
    else:
        library.append((title, author))
        print(f"{title} written by: {author} was added to the library.")
    

book(library, "Harry Potter", "J.K. Rawlings")
book(library, "Brave New World", "Aldous Huxley") 




