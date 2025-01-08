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

