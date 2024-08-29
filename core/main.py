import sys
import os
import time
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from ds.tree import Trie

class AutocompleteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Autocomplete App")
        self.master.geometry("400x150")

        self.trie = Trie()
        self.load_words()

        self.input_var = tk.StringVar()
        self.input_var.trace_add("write", self.update_suggestions)

        self.input_entry = ctk.CTkEntry(self.master, textvariable=self.input_var)
        self.input_entry.pack(padx=10, pady=10, fill=tk.X)

        self.suggestion_listbox = tk.Listbox(self.master)
        self.suggestion_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.suggestion_listbox.bind("<<ListboxSelect>>", self.use_suggestion)

        self.last_update_time = 0

    def load_words(self):
        with open("core/words.txt", 'r') as words:
            for word in words:
                self.trie.insert(word.rstrip("\n"))
        words.close()

    def update_suggestions(self, *args):
        current_time = time.time()
        if current_time - self.last_update_time < 0.3:  # Debounce
            return
        self.last_update_time = current_time

        prefix = self.input_var.get().lower()
        suggestions = self.trie.collect_words(prefix)[:10]  # Limit to 10 suggestions

        self.suggestion_listbox.delete(0, tk.END)
        for word in suggestions:
            self.suggestion_listbox.insert(tk.END, word)

    def use_suggestion(self, event):
        if self.suggestion_listbox.curselection():
            selected_word = self.suggestion_listbox.get(self.suggestion_listbox.curselection())
            self.input_var.set(selected_word)
            self.input_entry.icursor(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AutocompleteApp(root)
    root.mainloop()
