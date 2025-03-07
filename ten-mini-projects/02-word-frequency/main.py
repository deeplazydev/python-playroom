from collections import Counter
from tkinter import filedialog as fdialog
from readers import read_file_content
import re


def select_file() -> str | None:
    """
    Open a dialog box to select a file.
    :return: path to file or None if cancelled
    """
    file_types: tuple[tuple[str, str]] = (
        ("Text files", "*.txt"),
        ("PDF files", "*.pdf"),
        ("All files", "*.*")
    )

    return fdialog.askopenfilename(title="Open a file",
                                   initialdir=".",
                                   filetypes=file_types)


def get_frequency(text: list[str]) -> list[tuple[str, int]]:
    """
    Count the number of occurrences that each word appears.
    """
    word_count: Counter = Counter()

    for line in text:
        lowered_line: str = line.lower().strip()
        words: list[str] = re.findall(r'\b\w+\b', lowered_line)
        word_count.update(words)

    return word_count.most_common()


def main() -> None:
    file_path: str = select_file()

    if not file_path:
        return

    text: list[str] = read_file_content(file_path)
    word_frequencies: list[tuple[str, int]] = get_frequency(text)

    for word, count in word_frequencies:
        print(f'{word}: {count}')


if __name__ == "__main__":
    main()
