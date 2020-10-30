import pyttsx3
import PyPDF2
book = open('The_Art_Of_War.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
speaker.setProperty('rate', 150)
speaker.setProperty('volume', 0.7)
voices = speaker.getProperty('voices')

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

# Use female voice
speaker.setProperty('voice', voice_id)

for num in range(3, pages):
    page = pdfReader.getPage(num)
    page1 = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()