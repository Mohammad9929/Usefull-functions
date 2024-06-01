from PyPDF2 import PdfReader, PdfWriter

def extract_pages_from_pdf(input_pdf_path, start_page, end_page, output_pdf_path):
    """
    Extracts a range of pages from the input PDF file and saves them to the output PDF file.

    Args:
        input_pdf_path (str): Path to the input PDF file.
        start_page (int): Starting page number (inclusive).
        end_page (int): Ending page number (inclusive).
        output_pdf_path (str): Path to the output PDF file.

    Returns:
        None
    """
    pdf_reader = PdfReader(input_pdf_path)
    pdf_writer = PdfWriter()

    for page_num in range(start_page - 1, end_page):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_pdf_path, 'wb') as output_file:
        pdf_writer.write(output_file)

    print(f"Extracted pages {start_page} to {end_page} and saved to {output_pdf_path}")