import os 
import dealing_with_doc
from config import Config


config = Config()
directory = os.getcwd()

dest_dir = config.saving_path

extensions = ['.docx', '.pptx', '.pdf', '.html', '.txt']
file_extension = []

print(directory)

list_of_files = [file for file in os.listdir(directory) if os.path.splitext(file)[1].lower() in extensions]

print(list_of_files)

for f in list_of_files:
    file_extension.append(os.path.splitext(f)[1])

print(file_extension)

doc_translator = dealing_with_doc.DocTranslator(list_of_files, file_extension)
doc_translator.translation()

