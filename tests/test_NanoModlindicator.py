import unittest
import tkinter as tk
from NanoOneTk import NanoMoodlindicator 

class TestNanoMoodindicator(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.mood_indicator = NanoMoodlindicator(master=self.root)
        self.mood_indicator.pack()

    def tearDown(self):
        self.root.destroy()

    def test_initial_mood(self):
        self.assertEqual(self.mood_indicator.mood_status.cget("text"), "Настроение: Не определено")
        self.assertEqual(self.mood_indicator.mood_status.cget("fg"), "gray")

    def test_change_mood(self):
        self.mood_indicator.change_mood()
        mood_text = self.mood_indicator.mood_status.cget("text")
        self.assertTrue(mood_text.startswith("Настроение: "))       
        mood_value = mood_text.split(": ")[1]
        self.assertIn(mood_value, self.mood_indicator.moods)  

    def test_mood_color(self):
        for mood in self.mood_indicator.moods:
            self.mood_indicator.mood_status.config(text=f"Настроение: {mood}")          
            self.mood_indicator.change_mood()  
            self.root.update()  
            current_mood = self.mood_indicator.mood_status.cget("text").split(": ")[1]
            if current_mood == "Счастлив!":
                self.assertEqual(self.mood_indicator.mood_status.cget("fg"), "yellow")
            elif current_mood == "Грустный...":
                self.assertEqual(self.mood_indicator.mood_status.cget("fg"), "blue")
            elif current_mood == "Злой!":
                self.assertEqual(self.mood_indicator.mood_status.cget("fg"), "red")
            elif current_mood == "Устал...":
                self.assertEqual(self.mood_indicator.mood_status.cget("fg"), "gray")
            elif current_mood == "Энергичный!":
                self.assertEqual(self.mood_indicator.mood_status.cget("fg"), "green")
            else:
                self.assertEqual(self.mood_indicator.mood_status.cget("fg"), "purple")

if __name__ == "__main__":
    unittest.main()
