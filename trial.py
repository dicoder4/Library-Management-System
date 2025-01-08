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
