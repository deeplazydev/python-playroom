from pypdf import PdfReader


def read_file_content(file_path: str) -> list[str]:
    """
    Read text content of file
    :param file_path: full path to file
    """
    if file_path.endswith(".pdf"):
        return read_pdf_file(file_path)
    else:
        return read_text_file(file_path)


def read_text_file(file_path: str) -> list[str]:
    """
    Read text content of file
    :param file_path: full path to file
    """
    with open(file_path, "r") as f:
        return f.readlines()


def read_pdf_file(file_path: str) -> list[str]:
    """
    Read text content of text from the first page of the file
    :param file_path: full path to file
    """
    reader = PdfReader(file_path)
    page = reader.get_page(0)

    return page.extract_text().split('\n')

