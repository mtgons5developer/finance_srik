import tkinter as tk

class SearchApp:
    def __init__(self, master):
        self.master = master
        master.title("Search App")

        self.search_label = tk.Label(master, text="Search:")
        self.search_label.pack(side=tk.LEFT)

        self.search_entry = tk.Entry(master)
        self.search_entry.pack(side=tk.LEFT)

        self.search_button = tk.Button(master, text="Search", command=self.search)
        self.search_button.pack(side=tk.LEFT)

    def search(self):
        query = self.search_entry.get()
        # Do something with the search query, such as search a database or file system
        print("Search query:", query)

root = tk.Tk()
app = SearchApp(root)
root.mainloop()
