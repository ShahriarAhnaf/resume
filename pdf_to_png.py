from pdf2image import convert_from_path

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

images = convert_from_path('Ahnaf_Shahriar_Resume.pdf', output_folder="./", fmt='png', dpi=1000, size=(2160,None),
                           output_file="resume", single_file=True)
