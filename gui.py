import tkinter as tk
from tkinter import ttk
import webbrowser
from ttkthemes import ThemedTk
from scraper import scrape_g1

class NewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notícias de Política - G1")
        self.root.geometry("900x600")
        self.create_widgets()
        self.load_news()

    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="Manchetes de Política - G1",
            font=("Helvetica", 20, "bold")
        )
        title_label.pack(pady=20)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            "Treeview.Heading",
            font=("Helvetica", 14, "bold"),
            foreground="#333333"
        )
        style.configure(
            "Treeview",
            font=("Helvetica", 12),
            rowheight=30,
            background="#ffffff",
            fieldbackground="#ffffff"
        )
        style.map(
            'Treeview',
            background=[('selected', '#6CC644')],
            foreground=[('selected', '#ffffff')]
        )

        container = ttk.Frame(self.root)
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.tree = ttk.Treeview(
            container,
            columns=("title", "link"),
            show="headings",
            style="Treeview"
        )
        self.tree.heading("title", text="Título")
        self.tree.heading("link", text="Link")
        self.tree.column("title", anchor=tk.W, width=600)
        self.tree.column("link", anchor=tk.W, width=250)

        self.tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        scrollbar = ttk.Scrollbar(
            container, orient=tk.VERTICAL, command=self.tree.yview
        )
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind("<Double-1>", self.open_link)

    def load_news(self):
        news = scrape_g1()
        for article in news:
            self.tree.insert("", tk.END, values=(article["title"], article["link"]))

    def open_link(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            link = item["values"][1]
            webbrowser.open(link)
