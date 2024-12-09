import tkinter as tk

from NanoOneTk import NanoLabeledEntry

root = tk.Tk()

root.title("Example")
root.geometry("500x500")

nano_labeled_entry = NanoLabeledEntry(root)
nano_labeled_entry.pack()

root.mainloop()
