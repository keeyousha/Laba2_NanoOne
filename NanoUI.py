import tkinter as tk

from NanoOneTk import NanoLabeledEntry, NanoJoke

root = tk.Tk()

root.title("Example")
root.geometry("500x500")

nano_labeled_entry = NanoLabeledEntry(root)
nano_labeled_entry.pack()

nano_joke = NanoJoke(root)
nano_joke.pack()

root.mainloop()
