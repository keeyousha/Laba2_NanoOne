import tkinter as tk

class NanoMoodlindicator(tk.Frame):
    """
    A custom Tkinter widget combining a Label, Button, and Mood Indicator.

    This widget displays a label, a button, and a mood indicator that changes when
    the button is clicked, showing a mood from a predefined list in a sequential manner.
    """

    def __init__(self, master=None, **kwargs):
        """
        Initialize the NanoMoodIndicator widget.

        Args:
            master (Tk or Widget, optional): The parent widget.
            **kwargs: Additional keyword arguments to configure the Frame widget.
        """
        super().__init__(master, **kwargs)
        
        self.moods = [
            "Счастлив!",
            "Грустный...",
            "Злой!",
            "Устал...",
            "Энергичный!",
            "Без настроения..."
        ]
        
        self.current_mood_index = 0 
        self.label = tk.Label(self, text="Нажми кнопку, чтобы изменить настроение!")
        self.label.pack(side=tk.TOP, padx=10, pady=10)
        self.mood_status = tk.Label(self, text="Настроение: Не определено", fg="gray")
        self.mood_status.pack(side=tk.TOP, padx=10, pady=10)
        self.button = tk.Button(self, text="Поменять настроение", command=self.change_mood)
        self.button.pack(side=tk.BOTTOM, padx=10, pady=10)

    def change_mood(self):
        """
        Change the mood indicator to the next mood in the list.
        """
        current_mood = self.moods[self.current_mood_index]
        self.mood_status.config(text=f"Настроение: {current_mood}")
        
        if current_mood == "Счастлив!":
            self.mood_status.config(fg="yellow")
        elif current_mood == "Грустный...":
            self.mood_status.config(fg="blue")
        elif current_mood == "Злой!":
            self.mood_status.config(fg="red")
        elif current_mood == "Устал...":
            self.mood_status.config(fg="gray")
        elif current_mood == "Энергичный!":
            self.mood_status.config(fg="green")
        else:
            self.mood_status.config(fg="purple")
        
        self.current_mood_index = (self.current_mood_index + 1) % len(self.moods)
