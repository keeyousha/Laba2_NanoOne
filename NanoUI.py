import tkinter as tk

from NanoOneTk import NanoLabeledEntry, NanoMoodIndicator, NanoJoke


root = tk.Tk()

root.title("Example")
root.geometry("500x500")

nano_labeled_entry = NanoLabeledEntry(root)
nano_labeled_entry.pack()

nano_joke = NanoJoke(root)
nano_joke.pack()

nano_mood_indicator = NanoMoodIndicator(root)
nano_mood_indicator.pack()


root.mainloop()

