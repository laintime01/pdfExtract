# This is a pdf extract program by hao
# pip install pdfminer.six works

import re
from pdfminer.high_level import extract_pages, extract_text
import fitz  # PyMyPDF
import PIL.Image  # pillow
import io
from tabula.io import read_pdf


# extract text
def extract_pdf_text(pdf_name):
    text = extract_text(pdf_name)
    # print(text)
    # find text followed by ,
    pattern = re.compile(r"[a-zA-Z]+,")
    matches_result = pattern.findall(text)
    print(matches_result)
    # make comma disappear
    no_comma = [n[0:-2] for n in matches_result]
    print(no_comma)


# extract image from pdf
# pip install pillow
# pip install pyMuPDF


def extract_image_from_pdf(pdf_name):
    pdf = fitz.open(pdf_name)
    counter = 1
    for i in range(len(pdf)):
        page = pdf[i]
        images = page.get_images()
        for image in images:
            base_image = pdf.extract_image(image[0])
            image_data = base_image["image"]
            # PIL.Image.open used to open specific image path
            # io.BytesIO read bytes from memory
            img_extract = PIL.Image.open(io.BytesIO(image_data))
            img_extension = base_image['ext']
            img_extract.save(open(f"image{counter}.{img_extension}", "wb"))
            counter += 1


# pip install tabula
def extract_table_from_pdf(pdf_name):
    tables = read_pdf(pdf_name, pages="all")
    df = tables[0]
    print(df)


if __name__ == '__main__':
    print("------start extract------")
    extract_pdf_text("textsample.pdf")
    extract_image_from_pdf("sample.pdf")
    extract_table_from_pdf("sample.pdf")
