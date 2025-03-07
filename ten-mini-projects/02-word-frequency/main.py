from collections import Counter
import re


def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_count: Counter = Counter(words)


    return word_count.most_common()


def main() -> None:
    text: str = input('Enter your text: ').strip()
    word_frequencies: list[tuple[str, int]] = get_frequency(text)

    for word, count in word_frequencies:
        print(f'{word}: {count}')


if __name__ == "__main__":
    main()


"""
Homework:
1. Create a function that allows the user to read a file directly (such as a txt)
so the user doesn't have to copy and paste text.
"""
