import tkinter as tk
from driver import XLSXReader



root = tk.Tk()
root.title("XLSX Reader")
app = XLSXReader(root)
root.mainloop()
