import tkinter as tk
from tkinter import filedialog
import pandas as pd
from browser import run_ecrs

class XLSXReader:
    def __init__(self, root):
        self.root = root
        self.df = None
        self.current_row = 0
        self.entries = []

        self.open_btn = tk.Button(root, text="Open file", command=self.open_file)
        self.open_btn.pack()

        self.row_label = tk.Label(root, text="")
        self.row_label.pack()

        self.prev_btn = tk.Button(root, text="Previous", command=self.prev_row, state=tk.DISABLED)
        self.prev_btn.pack(side=tk.LEFT)

        self.next_btn = tk.Button(root, text="Next", command=self.next_row, state=tk.DISABLED)
        self.next_btn.pack(side=tk.RIGHT)

        self.input_frame = tk.Frame(root)
        self.input_frame.pack()

    def open_file(self):
        filepath = filedialog.askopenfilename(title="Open file", filetypes=[("xlsx files", "*.xlsx")])
        if not filepath:
            return
        self.df = pd.read_excel(filepath)
        self.current_row = 0
        self.update_row_label()
        self.create_input_boxes()
        self.prev_btn.config(state=tk.NORMAL)
        self.next_btn.config(state=tk.NORMAL)

    def prev_row(self):
        if self.current_row > 0:
            self.current_row -= 1
            self.update_row_label()
            self.update_entries()

    def next_row(self):
        assert isinstance(self.df, pd.DataFrame)
        if self.current_row < len(self.df) - 1:
            self.current_row += 1
            self.update_row_label()
            self.update_entries()

    def update_row_label(self):
        assert isinstance(self.df, pd.DataFrame)
        if self.current_row < len(self.df) - 1:
            row_values = self.df.iloc[self.current_row].values
            self.row_label.config(text=f"Row {self.current_row+1}: {row_values}")

   def create_input_boxes(self):
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.entries = []
        assert isinstance(self.df, pd.DataFrame)
        for i, column in enumerate(self.df.columns):
            label = tk.Label(self.input_frame, text=column)
            label.grid(row=i, column=0)
            entry = tk.Entry(self.input_frame)
            entry.grid(row=i, column=1)
            entry.insert(0, self.df.iloc[self.current_row][i])
            self.entries.append(entry)

    def update_entries(self):
        assert isinstance(self.df, pd.DataFrame)
        for i, entry in enumerate(self.entries):
            entry.delete(0, tk.END)
            entry.insert(0, self.df.iloc[self.current_row][i])

