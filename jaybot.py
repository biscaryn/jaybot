from PIL import Image, ImageGrab
import pytesseract
import webbrowser
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

# TO-DO:
#   - Train tesseract OCR to HQ's font (Circular)
#   - learn Google Search and Wikipedia API
#   - new method: Using Wikipedia to find answer
#   - new method: Searching "Question + each answer" to find answer
#   - show degree of certainty
#   - More graphic UI with different colors using crayons library
#   - Show one final answer
#   - Deal with special cases like "which of these" and "NOT"




question_bb = (670, 340, 1000, 420) # coordinates of the question live
answers_bb = (670, 420, 1000, 600) # coordinates of the answers live

# question_bb = (670, 390, 1000, 500) # coordinates of the question in training videos
# answers_bb = (670, 500, 1000, 700) # coordinates of the answers in training videos


# Taking screenshots of the question area and the answers area and saving them to the folder
q = ImageGrab.grab(bbox = question_bb)
q.save("question.png", "PNG")

a = ImageGrab.grab(bbox = answers_bb)
a.save("answers.png", "PNG")


# Turning text in screenshots into strings and storing them in variables
question = (pytesseract.image_to_string(Image.open('question.png'))).encode("utf-8")
question = question.replace('\n', ' ')
answers = ((pytesseract.image_to_string(Image.open('answers.png'))).encode("utf-8")).splitlines()


# method 1: directly googling the question
webbrowser.open("http://google.com/search?q=" + question)

