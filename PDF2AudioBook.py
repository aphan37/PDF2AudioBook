import PyPDF2
import pyttsx3

file = askopenfilename()
pdf_reader = PyPDF2.PdfReader(file, 'rb'))
speaker = pyttsx3.init()

for page_num in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_num].extract_text()
    if text:
        speaker.say(text)
    speaker.runAndWait()
