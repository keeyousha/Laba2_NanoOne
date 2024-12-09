import tkinter as tk
import random

class NanoJoke(tk.Frame):
    """
    A custom Tkinter widget combining a Label and a Button with a fun twist.

    This widget displays a label with text and a button. When the button is clicked,
    the label's text is updated to a random joke.
    """
    
    def __init__(self, master=None, **kwargs):
        """
        Initialize the JokeWidget widget.

        Args:
            master (Tk or Widget, optional): The parent widget.
            **kwargs: Additional keyword arguments to configure the Frame widget.
        """
        super().__init__(master, **kwargs)
        
        # List of jokes
        self.jokes = [
            "Программисты на работе общаются двумя фразами: «непонятно» и «вроде работает».",
            "Сколько программистов нужно, чтобы заменить лампочку? Ни одного, это проблема с оборудованием.",
            "От нечего делать бродил по форумам программистов, ответил на свой же собственный вопрос, заданный месяц назад.",
            "За каждым успешным программистом стоит женщина, которой не существует.",
            "Жил—был программист и было у него два сына — Антон и Неантон."
        ]
        
        # Create and pack the label
        self.label = tk.Label(self, text="Нажми на кнопку, чтобы увидеть шутку!")
        self.label.pack(side=tk.TOP, padx=10, pady=10)
        
        # Create and pack the button
        self.button = tk.Button(self, text="Показать шутку", command=self.show_joke)
        self.button.pack(side=tk.BOTTOM, padx=10, pady=10)
    
    def show_joke(self):
        """
        Display a random joke in the label.
        """
        random_joke = random.choice(self.jokes)
        self.label.config(text=random_joke)