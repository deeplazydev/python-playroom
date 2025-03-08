import tkinter as tk
from tkinter import filedialog, Tk, Text, Frame, Button


class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Bob's notepad")

        # Text widget
        self.text_area: Text = Text(self.root, wrap="word")
        self.text_area.pack(expand=True, fill="both")

        # Bottom bar
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        self.save_button: Button = Button(self.button_frame, text="Save", command=self.save_file)
        self.save_button.pack(side=tk.LEFT)

        self.load_button: Button = Button(self.button_frame, text="Load", command=self.load_file)
        self.load_button.pack(side=tk.LEFT)

    def run(self) -> None:
        self.root.mainloop()

    def save_file(self):
        file_path: str = filedialog.asksaveasfile(defaultextension=".txt",
                                                  filetypes=[("Text files", "*.txt")])

        if not file_path:
            return

        with open(file_path, "w") as f:
            f.write(self.text_area.get(1.0, tk.END))

        print(f"File saved to: {file_path}")

    def load_file(self):
        file_path: str = filedialog.askopenfilename(defaultextension=".txt",
                                                    filetypes=[("Text files", "*.txt"),
                                                               ("All files", "*.*")])

        if not file_path:
            return

        with open(file_path, "r") as f:
            content: str = f.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.INSERT, content)

        print(f"File loaded from: {file_path}")


def main() -> None:
    window: Tk = Tk()
    app: SimpleNotepad = SimpleNotepad(root=window)
    app.run()


if __name__ == "__main__":
    main()


"""
Homework:
1. Make it so that the save button saves the next to the current file if it already exists, instead
of asking the user to create a new file each time.
"""