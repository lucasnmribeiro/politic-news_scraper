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
        title_label = tk.Label(self.root, text="Manchetes de Política - G1", font=("Helvetica", 20, "bold"), bg='#4B8BBE', fg='#ffffff')
        title_label.pack(pady=20)

        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"), foreground="#333333", background="#ffffff")
        style.configure("Treeview", font=("Helvetica", 12), rowheight=30, background="#ffffff", foreground="#000000", fieldbackground="#e1e1e1")
        style.map('Treeview', background=[('selected', '#6CC644')], foreground=[('selected', '#ffffff')])

        container = ttk.Frame(self.root, style="TFrame")
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.tree = ttk.Treeview(container, columns=("title", "link"), show="headings", style="Treeview")
        self.tree.heading("title", text="Título")
        self.tree.heading("link", text="Link")
        self.tree.column("title", anchor=tk.W, width=700)
        self.tree.column("link", anchor=tk.W, width=200)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree.bind("<Double-1>", self.on_item_double_click)

        scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def load_news(self):
        articles = scrape_g1()
        for article in articles:
            self.tree.insert("", tk.END, values=(article['title'], article['link']))

    def on_item_double_click(self, event):
        item = self.tree.selection()[0]
        link = self.tree.item(item, "values")[1]
        webbrowser.open(link)

if __name__ == "__main__":
    root = ThemedTk(theme="arc")  # Use ThemedTk para aplicar temas
    app = NewsApp(root)
    root.mainloop()