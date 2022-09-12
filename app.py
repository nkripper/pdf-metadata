import os
from PyPDF2 import PdfReader
import re
import json


def main():
    document_directory = './documents/'
    file_list = os.listdir(document_directory)
    for file in file_list:
        if re.search(f'\.[Pp][Dd][Ff]', str(file)):
            open_file = open(document_directory + file, 'rb')
            reader = PdfReader(open_file)
            pdf_metadata = reader.metadata

            print(file)
            print(json.dumps(pdf_metadata, indent=4))

            open_file.close()


if __name__ == "__main__":
    main()
