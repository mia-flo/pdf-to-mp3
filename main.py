import pyttsx3, PyPDF2
import zipfile

speaker = pyttsx3.init()

class MP3:
    def __init__(self, file_path: str, name: str, start: int, end: int):
        self.file_path = file_path
        self.start = start
        self.end = end
        self.name = name

        #voice attributes
        voices = speaker.getProperty('voices')
        speaker.setProperty('voice', voices[1].id)
        speaker.setProperty('rate', 150)
        speaker.setProperty('volume', .75)

        #loading the file
        self.pdf = PyPDF2.PdfReader(open(file_path, 'rb'))
        self.page_num = len(self.pdf.pages)

    def extract(self):
        text = ""
        for page in range(self.start, self.end):
            text += self.pdf.pages[page].extract_text()

            self.clean_text = text.strip().replace('\n', ' ')
            print(self.clean_text)

        speaker.save_to_file(self.clean_text, self.name)
        speaker.runAndWait()

        speaker.stop()

class Compress:
    def __init__(self, file_path: str, name: str):
        self.file_path = file_path
        self.name = name

    def zip(self):
        #highest level of compression
        with zipfile.ZipFile(self.name, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as my_zip:
            my_zip.write(self.file_path)


#audio = MP3(r'your_file_path', 'file_name', start_page, end_page)
#audio.extract()

###if you want to compress the audio file
#zipped = Compress(r'your_file_path_here', 'file_name')
