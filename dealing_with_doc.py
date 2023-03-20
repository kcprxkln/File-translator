import deepl 
from config import Config

config = Config()
translator = deepl.Translator(config.apikey)

class DocTranslator:
    def __init__(self, doc_paths: list, doc_extensions: list): 
        self.doc_paths = doc_paths
        self.doc_extensions = doc_extensions 

    def translation(self):
        print(f'Saving documents to: {config.saving_path}')
        print(self.doc_paths)
        i = 0
        for doc in self.doc_paths:
                doc_extension = self.doc_extensions[i]
                print(doc_extension)
                self.final_name = (f'{config.saving_path}{doc.split("/")[-1].replace(doc_extension, "")}-translated{doc_extension}')
                print(f'doc - {doc}')
                print(f'final name {self.final_name}')

                try:
                    translator.translate_document_from_filepath(
                        doc, 
                        self.final_name,
                        target_lang = config.translate_to_lang
                    )
                    print(f'File {i} successfully translated.')
                    
                except:
                     print('Error, please try again')

                i += 1