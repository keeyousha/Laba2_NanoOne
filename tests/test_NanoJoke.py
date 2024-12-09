import unittest
import tkinter as tk
from unittest.mock import patch
from io import StringIO
import sys
from NanoOneTk import NanoJoke

class TestNanoJoke(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.widget = NanoJoke(self.root)
        self.widget.pack()

    def tearDown(self):
        self.widget.destroy()
        self.root.destroy()

    def test_label_initial_text(self):
        expected_initial_text = "Нажми на кнопку, чтобы увидеть шутку!"
        self.assertEqual(self.widget.label.cget("text"), expected_initial_text)

    def test_show_joke_changes_label_text(self):
        initial_text = self.widget.label.cget("text")

        self.widget.show_joke()

        updated_text = self.widget.label.cget("text")
        self.assertNotEqual(initial_text, updated_text)
        self.assertIn(updated_text, self.widget.jokes)

    def test_jokes_list_not_empty(self):
        """
        Test that the jokes list is not empty.
        """
        self.assertGreater(len(self.widget.jokes), 0)

if __name__ == "__main__":
    unittest.main()
