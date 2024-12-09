import tkinter as tk

class NanoLabeledEntry(tk.Frame):
    def __init__(self, master=None, label_text="Label", **kwargs):
        super().__init__(master, **kwargs)
        self.label = tk.Label(self, text=label_text)
        self.label.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.entry = tk.Entry(self)
        self.entry.pack(side=tk.LEFT, padx=5, pady=5)

    def get(self):
        return self.entry.get()

    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)