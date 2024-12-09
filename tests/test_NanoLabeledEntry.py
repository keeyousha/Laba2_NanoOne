import unittest
import tkinter as tk
from NanoOneTk import NanoLabeledEntry

class TestNanoLabeledEntry(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.widget = NanoLabeledEntry(self.root, label_text="Test Label")
        self.widget.pack()

    def tearDown(self):
        self.widget.destroy()
        self.root.destroy()

    def test_initial_label_text(self):
        self.assertEqual(self.widget.label.cget("text"), "Test Label")

    def test_initial_entry_is_empty(self):
        self.assertEqual(self.widget.get(), "")

    def test_set_method(self):
        self.widget.set("New Value")
        self.assertEqual(self.widget.get(), "New Value")

    def test_get_method(self):
        self.widget.entry.insert(0, "Sample Value")
        self.assertEqual(self.widget.get(), "Sample Value")

    def test_set_method_overwrites_existing_value(self):
        self.widget.entry.insert(0, "Old Value")
        self.widget.set("Updated Value")
        self.assertEqual(self.widget.get(), "Updated Value")

if __name__ == "__main__":
    unittest.main()
