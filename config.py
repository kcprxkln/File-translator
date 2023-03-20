import os

class Config:
    def __init__(self):
        self.apikey = os.environ.get('DEEPL_API_KEY') # your DEEPL api key
        self.saving_path = 'path/to/your/directory'  #where the translated files will be stored
        self.translate_to_lang = 'DE' #what is your destination language? List of supported languages with their format in Readme
    
    