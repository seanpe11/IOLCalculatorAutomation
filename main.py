import tkinter as tk
from reader import IOLReader

root = tk.Tk()
root.tk.call('tk', 'scaling', 1.5)

root.title("XLSX Reader")

## ECRS
from browser_ecrs import BrowserECRS
app = IOLReader(root, BrowserECRS())

## Hill-RBF
# from browser_hill_rbf import BrowserHillRBF 
# app = IOLReader(root, BrowserHillRBF())

root.mainloop()
