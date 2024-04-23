import tkinter as tk
from reader import XLSXReader

root = tk.Tk()
root.title("XLSX Reader")
app = XLSXReader(root)
root.mainloop()
