import os
import PyPDF2
from gtts import gTTS
from pydub import AudioSegment
import pyttsx3

def pdf_to_text(pdf_file):
    # Extract text from the PDF file
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# Can change text_to_speech() if don't like voice
def text_to_speech(text, output_file):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()


if __name__ == "__main__":
    pdf_file = "affirm.pdf"   # Replace with the path to your PDF file
    output_audio_file = "output_audio.mp3"   # Output audio file name

    text = pdf_to_text(pdf_file)
    text_to_speech(text, output_audio_file)
    
    print(f"Conversion complete. Audio file '{output_audio_file}' created.")
    