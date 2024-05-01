import tkinter as tk
from tkinter import filedialog
import pandas as pd
from typing import cast

class IOLReader:
    def __init__(self, root, browser_driver):
        self.root = root
        self.df = None
        self.filepath = None
        self.current_row = 0
        self.entries = []
        self.entry_vars = []

        self.open_btn = tk.Button(root, text="Open file", command=self.open_file)
        self.open_btn.pack()

        self.row_label = tk.Label(root, text="")
        self.row_label.pack()

        self.prev_btn = tk.Button(root, text="Previous", command=self.prev_row, state=tk.DISABLED)
        self.prev_btn.pack(side=tk.LEFT)

        self.next_btn = tk.Button(root, text="Next", command=self.next_row, state=tk.DISABLED)
        self.next_btn.pack(side=tk.RIGHT)
        self.final_frame = tk.Frame(root)
        self.final_frame.pack()

        self.input_frame = tk.Frame(root)
        self.input_frame.pack()


        self.autofill_btn = tk.Button(root, text="Autofill", command=self.autofill, state=tk.NORMAL)
        self.autofill_btn.pack()
        self.save_btn = tk.Button(root, text="Save Changes", command=self.save_to_file, state=tk.NORMAL)
        self.save_btn.pack()

        self.browser_driver = browser_driver



    def open_file(self):
        filepath = filedialog.askopenfilename(title="Open file", filetypes=[("xlsx files", "*.xlsx")])
        if not filepath:
            return
        self.df = pd.read_excel(filepath)
        self.filepath = filepath
        self.current_row = 0
        self.create_input_boxes()
        self.prev_btn.config(state=tk.NORMAL)
        self.next_btn.config(state=tk.NORMAL)

    def prev_row(self):
        if self.current_row > 0:
            self.current_row -= 1
            self.update_entries()

    def next_row(self):
        assert isinstance(self.df, pd.DataFrame)
        if self.current_row < len(self.df) - 1:
            self.current_row += 1
            self.update_entries()

    def on_entry_change(self, index):
        assert isinstance(self.df, pd.DataFrame)

        new_value = self.entry_vars[index].get()
        self.df.iloc[self.current_row, index] = new_value


    def create_input_boxes(self):
        assert isinstance(self.df, pd.DataFrame)

        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.entries = []
        self.entry_vars = []  # Reset the list of StringVars

        final_vars = ["Target", "Power", "Hill RBF prediction"]

        j = 0
        for i, column in enumerate(self.df.columns):
            r = i // 3
            c = i % 3 * 2

            var = tk.StringVar()

            parent = self.input_frame if column in final_vars else self.final_frame
            if (column in final_vars):
                r = 0
                c = j * 2
                j+=1

            entry = tk.Entry(parent, textvariable=var)
            label = tk.Label(parent, text=column)

            entry.grid(row=r, column=c+1)
            label.grid(row=r, column=c)

            var.set(self.df.iloc[self.current_row, i])
            var.trace("w", lambda name, index, mode, idx=i: self.on_entry_change(idx))
            
            self.entries.append(entry)
            self.entry_vars.append(var)  # Store StringVar to track changes


    def update_entries(self):
        assert isinstance(self.df, pd.DataFrame)
        for i, var in enumerate(self.entry_vars):
            current_value = str(self.df.iloc[self.current_row, i])
            var.set(current_value)


    def save_to_file(self):
        assert isinstance(self.df, pd.DataFrame)
        self.df.to_excel(self.filepath, index=False)
        self.df = pd.read_excel(self.filepath)

    def autofill(self):
        assert isinstance(self.df, pd.DataFrame)
        self.browser_driver.autofill(self.df.iloc[self.current_row])

