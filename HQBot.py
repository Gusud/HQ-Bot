print("DISCLAIMER: This is not 100% accurate and may give false results due to no fault of the program. \nThis tool "
      "was made by Gusud to be quick (with the program usually solving a question in 4 seconds).\nPlease use this "
      "tool for hints rather than certain answers!\n")
import pyautogui as p
import pytesseract
from win32api import GetSystemMetrics
import requests

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


def hits(string):
    content = (requests.get("https://www.google.co.uk/search?q=" + string)).text
    return int(
        content[content.find('<div class="sd" id="resultStats">About ') + 39:content.find(" results</div>")].replace(
            ',', ''))


def getQuestion():
    questionBook = []
    got_question = ((pytesseract.image_to_string(p.screenshot(region=(
        round(1440 * GetSystemMetrics(0) / 3840), round(450 * GetSystemMetrics(1) / 2160),
        round(980 * GetSystemMetrics(0) / 3840),
        round(370 * GetSystemMetrics(1) / 2160))))).replace('\n', " ")).replace("  ", " ")
    while True:
        if got_question is not None:
            if got_question in questionBook:
                return got_question
            else:
                questionBook.append(got_question)


def getOptions():
    potential = []
    for i in range(3):
        answer = (pytesseract.image_to_string(p.screenshot(region=(round(1510 * GetSystemMetrics(0) / 3840),
                                                                   round(640 * GetSystemMetrics(1) / 2160) + (
                                                                       round(186 * GetSystemMetrics(1) / 2160) * (
                                                                       i + 1)),
                                                                   round(820 * GetSystemMetrics(0) / 3840),
                                                                   round(120 * GetSystemMetrics(1) / 2160))))).replace(
            '\n',
            " ")
        potential.append(answer)
    return potential


def solve(full_question, potential, reverse, quote=None):
    best_option = str()
    best_score = int()
    worst_score = 100000
    worst_option = str()
    # currentScore = 0

    for i in potential:
        if quote is None:
            current_score = hits(str(full_question + ' "' + i + '"'))
        else:
            current_score = hits(quote + '"' + i + '"')
        print(i, ": ", current_score)
        if reverse is False and current_score > best_score:
            best_score = current_score
            best_option = i
        if reverse and current_score < worst_score:
            worst_score = current_score
            worstOption = i

    if reverse:
        # print(worstOption)
        print("\n\n-- negative --\n\n" + worst_option.upper())
        return True
    else:
        print("\n\n\n" + best_option.upper())
        return False


def game():
    negatives = ["not", "isnt", "except", "dont", "doesnt", "wasnt", "wouldnt", "cant", "never"]
    g = 1
    while True:

        negative = False
        speechMarks = ""
        whichQuestion = False

        print("Question " + str(q + 1) + ":\n")
        input()
        question = getQuestion()
        newQuestion = ""
        options = getOptions()
        print(question)

        if '“' in question:
            speechMarks = (question.split('“')[1]).split('”')[0]
            print("Quotes detected", speechMarks, "\n")

        for i in question:
            if i.upper() != i.lower():
                newQuestion += i
            question = newQuestion
            newQuestion = ""

        for i in question.split():
            if i.lower() + "\n" in negatives:
                negative = True
                break
            else:
                newQuestion += i
        solve(question, options, negative, speechMarks)
        g += 1
