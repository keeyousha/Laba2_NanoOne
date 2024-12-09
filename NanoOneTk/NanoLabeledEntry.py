import tkinter as tk

class NanoLabeledEntry(tk.Frame):
    """
    A custom Tkinter widget combining a Label and an Entry field in a single frame.

    This widget allows for easy association of a label with an entry field and provides
    methods for getting and setting the entry's value.

    Attributes:
        label (tk.Label): The label widget displayed next to the entry field.
        entry (tk.Entry): The entry field widget for user input.
    """

    def __init__(self, master=None, label_text="Label", **kwargs):
        """
        Initialize the NanoLabeledEntry widget.

        Args:
            master (Tk or Widget, optional): The parent widget.
            label_text (str, optional): The text to display in the label. Defaults to "Label".
            **kwargs: Additional keyword arguments to configure the Frame widget.
        """
        super().__init__(master, **kwargs)
        
        # Create and pack the label
        self.label = tk.Label(self, text=label_text)
        self.label.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Create and pack the entry
        self.entry = tk.Entry(self)
        self.entry.pack(side=tk.LEFT, padx=5, pady=5)

    def get(self):
        """
        Retrieve the current value from the entry field.

        Returns:
            str: The current text in the entry field.
        """
        return self.entry.get()

    def set(self, value):
        """
        Set a new value in the entry field.

        Args:
            value (str): The text to insert into the entry field.
        """
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)
