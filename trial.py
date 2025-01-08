import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
class LibrarySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1000x600")
        self.root.configure(bg="#2c3e50")  # Dark blue background
        
        # Store books in memory (for demo)
        self.books = []
        self.borrowed_books = {}
        
        self.setup_styles()
        self.create_widgets()
        
    def setup_styles(self):
        # Configure styles
        style = ttk.Style()
        
        # Configure colors and fonts
        style.configure("MainFrame.TFrame", background="#2c3e50")
        style.configure("Card.TFrame", background="#34495e", padding=20)
        
        # Configure button style
        style.configure("Modern.TButton",
                       padding=10,
                       font=('Helvetica', 10, 'bold'))
        
        # Configure label style
        style.configure("White.TLabel",
                       background="#34495e",
                       foreground="white",
                       font=('Helvetica', 11))
        
        # Configure entry style
        style.configure("Modern.TEntry", padding=5)
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, style="MainFrame.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title = ttk.Label(main_frame, 
                         text="Library Management System",
                         font=('Helvetica', 24, 'bold'),
                         foreground="white",
                         background="#2c3e50")
        title.pack(pady=20)
        
        # Create notebook for tabs
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Add Books Tab
        add_books_frame = ttk.Frame(notebook, style="Card.TFrame")
        notebook.add(add_books_frame, text="Add Books")
        self.create_add_books_tab(add_books_frame)
        
        # Borrow/Return Tab
        borrow_frame = ttk.Frame(notebook, style="Card.TFrame")
        notebook.add(borrow_frame, text="Borrow/Return")
        self.create_borrow_tab(borrow_frame)
        
        # View Books Tab
        view_frame = ttk.Frame(notebook, style="Card.TFrame")
        notebook.add(view_frame, text="View Books")
        self.create_view_tab(view_frame)
   def create_add_books_tab(self, parent):
        # Book Title
        ttk.Label(parent, text="Book Title:", style="White.TLabel").pack(pady=5)
        self.title_entry = ttk.Entry(parent, width=40, style="Modern.TEntry")
        self.title_entry.pack(pady=5)
        
        # Author
        ttk.Label(parent, text="Author:", style="White.TLabel").pack(pady=5)
        self.author_entry = ttk.Entry(parent, width=40, style="Modern.TEntry")
        self.author_entry.pack(pady=5)
        
        # ISBN
        ttk.Label(parent, text="ISBN:", style="White.TLabel").pack(pady=5)
        self.isbn_entry = ttk.Entry(parent, width=40, style="Modern.TEntry")
        self.isbn_entry.pack(pady=5)
        
        # Add Button
        ttk.Button(parent, text="Add Book", 
                  command=self.add_book,
                  style="Modern.TButton").pack(pady=20)
    def create_view_tab(self, parent):
        # Create Treeview
        columns = ('title', 'author', 'isbn', 'status')
        self.tree = ttk.Treeview(parent, columns=columns, show='headings')
        
        # Define headings
        self.tree.heading('title', text='Title')
        self.tree.heading('author', text='Author')
        self.tree.heading('isbn', text='ISBN')
        self.tree.heading('status', text='Status')
        
        # Configure column widths
        for col in columns:
            self.tree.column(col, width=150)
        
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Refresh button
        ttk.Button(parent, text="Refresh List",
                  command=self.refresh_book_list,
                  style="Modern.TButton").pack(pady=10)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        
        if title and author and isbn:
            self.books.append({
                'title': title,
                'author': author,
                'isbn': isbn,
                'available': True
            })
            messagebox.showinfo("Success", "Book added successfully!")
            self.clear_entries()
            self.refresh_book_list()
        else:
            messagebox.showerror("Error", "Please fill all fields!")
def borrow_book(self):
        isbn = self.borrow_isbn_entry.get()
        user_id = self.user_id_entry.get()
        
        if isbn and user_id:
            for book in self.books:
                if book['isbn'] == isbn and book['available']:
                    book['available'] = False
                    self.borrowed_books[isbn] = user_id
                    messagebox.showinfo("Success", "Book borrowed successfully!")
                    self.clear_entries()
                    self.refresh_book_list()
                    return
            messagebox.showerror("Error", "Book not found or not available!")
        else:
            messagebox.showerror("Error", "Please fill all fields!")
  def return_book(self):
        isbn = self.return_isbn_entry.get()
        
        if isbn:
            for book in self.books:
                if book['isbn'] == isbn and not book['available']:
                    book['available'] = True
                    self.borrowed_books.pop(isbn, None)
                    messagebox.showinfo("Success", "Book returned successfully!")
                    self.clear_entries()
                    self.refresh_book_list()
                    return
            messagebox.showerror("Error", "Book not found or already returned!")
        else:
            messagebox.showerror("Error", "Please enter ISBN!")

  def refresh_book_list(self):
        # Clear the tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Repopulate with current data
        for book in self.books:
            status = "Available" if book['available'] else "Borrowed"
            self.tree.insert('', tk.END, values=(
                book['title'],
                book['author'],
                book['isbn'],
                status
            ))
  def clear_entries(self):
        # Clear all entry fields
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)
        self.borrow_isbn_entry.delete(0, tk.END)
        self.user_id_entry.delete(0, tk.END)
        self.return_isbn_entry.delete(0, tk.END)

if _name_ == "_main_":
    root = tk.Tk()
    app = LibrarySystem(root)
    root.mainloop()
