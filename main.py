import tkinter as tk
from reader import IOLReader

root = tk.Tk()
root.tk.call('tk', 'scaling', 1.5)

root.title("XLSX Reader")

from browser_ecrs import BrowserECRS
app = IOLReader(root, BrowserECRS())

root.mainloop()
