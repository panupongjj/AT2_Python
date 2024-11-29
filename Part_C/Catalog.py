# Catalog.py
import sys
from Book import Book
from tkinter import messagebox 
# Global catalog list
catalog = [
    Book("0553296981", "The Diary of a Young Girl", "Frank, Anne", 16.50),
    Book("1400082773", "Dreams from My Father", "Obama, Barrack", 24.99),
    Book("1500CCS027", "AAAAAAA", "JJJJ, Barrack", 12.58),
    Book("170008275", "Dreams of My", "Oa, rack", 30.22),
]

def display_catalog(sort_price):
    """Display all books sorted by price."""
    root = tkinter.Tk()
    if sort_price == 1 :
        root.title("Display Books Sorted by Price")
    else: root.title("Display All Books ")

    if not catalog:
        label = tkinter.Label(root, text="The catalog is empty.")
    else:
        sorted_catalog = catalog
        if sort_price == 1 :
            sorted_catalog = sorted(catalog, key=lambda book: book.price)
        for book in sorted_catalog:
            print(book.display())
            label = tkinter.Label(root, anchor="w", padx=10,pady=10,text=book.display())
            label.pack() 
     
    root.mainloop()
    
def search_book_by_title():

    def search():
        title = titleEntry.get()

        found_books = [book for book in catalog if title.lower() in book.title.lower()]
        if not found_books:
            print(f"No books found with the title '{title}'.")
        else:
            reult = tkinter.Tk()
            reult.title("Search Book")
            count = 0
            for book in found_books:
                label = tkinter.Label(reult, anchor="w", padx=10,pady=10,text=book.display())
                label.grid(sticky="W",row=count,column=0)
                count+=1 
            root.mainloop()

    root = tkinter.Tk()
    root.title("Search Book")

    title = tkinter.Label(root, text="Enter Title: ")
    title.grid(sticky="W",row=0,column=0)
    titleEntry = tkinter.Entry(root)
    titleEntry.grid(sticky="w",row=0,column=1)
    submit_OK = tkinter.Button(root,text="SEARCH", command= search)
    submit_OK.grid(sticky="new",row=1,column=1,pady=5)
    root.mainloop()

def add_book():
    
    def add():
        isbn = isbnEntry.get()
        title = titleEntry.get()
        author = authorEntry.get()
        price = priceEntry.get()
        
        if not isbn or not title or not author or not price:
            print("All fields must be entered.")
            return
        try:
            price = float(price)
        except ValueError:
            print("Invalid price entered. Please enter a numeric value for price.")
            print("All fields must be entered.")
            return
        
        new_book = Book(isbn, title, author, price)
        catalog.append(new_book)
        print(f"Book '{title}' added to the catalog.")


    root = tkinter.Tk()
    root.title("Add Books")
   
    isbn = tkinter.Label(root, text="Enter ISBN :")
    isbn.grid(sticky="W",row=0,column=0)
    isbnEntry = tkinter.Entry(root)
    isbnEntry.grid(sticky="w",row=0,column=1)

    title = tkinter.Label(root, text="Enter Title: ")
    title.grid(sticky="W",row=1,column=0)
    titleEntry = tkinter.Entry(root)
    titleEntry.grid(sticky="w",row=1,column=1)

    author = tkinter.Label(root, text="Enter Author: ")
    author.grid(sticky="W",row=2,column=0)
    authorEntry = tkinter.Entry(root)
    authorEntry.grid(sticky="w",row=2,column=1)

    price = tkinter.Label(root, text="Enter Price: ")
    price.grid(sticky="W",row=3,column=0)
    priceEntry = tkinter.Entry(root)
    priceEntry.grid(sticky="w",row=3,column=1)
    

# FRAME ROW 2 COL 0
    submit_OK = tkinter.Button(root,text="ADD", command= add)
    submit_OK.grid(sticky="new",row=4,column=0,pady=5)

    # Add the new book to the catalog


def delete_book():
    def yes():
        catalog.remove(book_to_delete[0])
        messagebox.showinfo(title="  ", message="Book HAS benn deleted")
        root.destroy()
        
    def no():
        messagebox(title="ss", message="Book has NOT benn deleted")
    
    def CheckDel():
        isbn = isbnEntry.get()
        
        for book in catalog:
            if book.isbn == isbn:
                book_to_delete.append(book)
                break
        
        if len(book_to_delete) !=0:
            result = tkinter.Tk()
            result.title("DELETE BOOK")
            count = 0
            for book in book_to_delete:
                label = tkinter.Label(result, anchor="w", padx=10,pady=10,text=book.display())
                label = tkinter.Label(result, anchor="w", padx=10,pady=10,text=book.display())
                label.grid(sticky="W",row=count,column=0)
                count+=1 
           
            isbn = tkinter.Label(result, text="Are you sure to delete this book?")
            isbn.grid(row=1,column=0)
            submit_yes = tkinter.Button(result,text="YES", command= yes)
            submit_yes.grid(sticky="new",row=3,column=0,pady=5)
            submit_no= tkinter.Button(result,text="NO", command= no)
            submit_no.grid(sticky="new",row=4,column=0,pady=5)
            result.mainloop()

    book_to_delete = []
    root = tkinter.Tk()
    root.title("Delete Book")
    isbn = tkinter.Label(root, text="Enter ISBN :")
    isbn.grid(sticky="W",row=0,column=0)
    isbnEntry = tkinter.Entry(root)
    isbnEntry.grid(sticky="w",row=0,column=1)
    submit_OK = tkinter.Button(root,text="DELETE", command= CheckDel)
    submit_OK.grid(sticky="new",row=1,column=1,pady=5)
    root.mainloop()

def check_user_choice():
    userChoice = int(user_choice_entry.get())
    if userChoice == 1 :
        add_book()
    elif userChoice == 2 :
        display_catalog(1)
    elif userChoice == 3 :
        search_book_by_title()
    elif userChoice == 4 :
        delete_book()
    elif userChoice == 5 :
        display_catalog(0)
    elif userChoice == 6 :
        window.destroy()

def cancel_btn():
    user_choice_entry.delete(0,100)



import tkinter
window = tkinter.Tk()
window.title("BOOK CATALOG")

frame = tkinter.Frame(window)
frame.pack(anchor="w")

# Catalog Menu
user_info_frame = tkinter.LabelFrame(frame, text="Holmesglen Book Store")
user_info_frame.grid(sticky="W",row=0,column=0,padx=20,pady=20)

# FRAME ROW 0  COL 0
add_info_lable = tkinter.Label(user_info_frame, text="1. Add a book")
add_info_lable.grid(sticky="W",row=0,column=0)

sort_info_lable = tkinter.Label(user_info_frame, text="2. Sort and display books by price")
sort_info_lable.grid(sticky="W",row=1,column=0)

search_info_lable = tkinter.Label(user_info_frame, text="3. Search for books by title")
search_info_lable.grid(sticky="W",row=2,column=0)

delete_info_lable = tkinter.Label(user_info_frame, text="4. Delete a book")
delete_info_lable.grid(sticky="W",row=3,column=0)

display_info_lable = tkinter.Label(user_info_frame, text="5. Display all books")
display_info_lable.grid(sticky="W",row=4,column=0)

exit_info_lable = tkinter.Label(user_info_frame, text="6. Exit")
exit_info_lable.grid(sticky="W",row=5,column=0)

# FRAME ROW 1  COL 0
user_input_frame = tkinter.LabelFrame(frame, text="Enter menu choice")
user_input_frame.grid(sticky="new",row=1,column=0,padx=20,pady=20)

user_choice_entry = tkinter.Entry(user_input_frame)
user_choice_entry.grid(sticky="w",row=0,column=0,padx=20,pady=5)

# FRAME ROW 2 COL 0
submit_OK = tkinter.Button(frame,text="OK", command= check_user_choice)
submit_OK.grid(sticky="new",row=2,column=0, padx=20)

submit_Cancel = tkinter.Button(frame,text="Cancel", command=cancel_btn)
submit_Cancel.grid(sticky="new",row=3,column=0, padx=20,pady=5)

window.mainloop()
