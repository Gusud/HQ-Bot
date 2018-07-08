import pyautogui as p
import pytesseract
from win32api import GetSystemMetrics
import requests
from PIL import *
import wikipedia

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

def hits(string):
    content = (requests.get("https://www.google.co.uk/search?q=" + string)).text
    return int(content[content.find('<div class="sd" id="resultStats">About ') + 39:content.find(" results</div>")].replace(',', ''))

def wikiHits(string, potential):
    score_list=[]
    page=wikipedia.page(string)
    content=page.content
    split=(content.split())
    for i in potential:
        score_list.append(split.count(i))
    return score_list

def getQuestion():
    questionBook = []
    got_question = ((pytesseract.image_to_string(p.screenshot(region=(round(1440 * GetSystemMetrics(0) / 3840), round(450 * GetSystemMetrics(1) / 2160),round(980 * GetSystemMetrics(0) / 3840),round(370 * GetSystemMetrics(1) / 2160))))).replace('\n', " ")).replace("  ", " ")
    while True:
        if got_question is not None:
            if got_question in questionBook:
                return got_question
            else:
                questionBook.append(got_question)


def getOptions():
    potential = []
    for i in range(3):
        answer = (pytesseract.image_to_string(p.screenshot(region=(round(1510 * GetSystemMetrics(0) / 3840), round(640 * GetSystemMetrics(1) / 2160) + (round(186 * GetSystemMetrics(1) / 2160) * (i + 1)),round(820 * GetSystemMetrics(0) / 3840),round(120 * GetSystemMetrics(1) / 2160))))).replace('\n'," ")
        potential.append(answer)
    return potential


def solve(full_question, potential, reverse, quote=None):

    best_option = str()
    best_score = int()
    worst_score = 100000
    worst_option = str()
    total_score = 0
    score_list = []
    current_score = 0
    popularity = []
    totalpopularity=0
    worstPop=1000000
    worstPoption=str()
    bestPop=0
    bestPoption=str()
    pop_score=0
    
    for i in potential:
        curPop=hits(i)
        if quote is "":
            current_score = hits(str(full_question + ' "' + i + '"'))
        else:
            try:
                current_score = wikiHits(quote, potential)[potential.index(i)]
            except:
                current_score = hits(quote + '"' + i + '"')
        total_score += int(current_score)
        score_list.append(current_score)

        pop_score=current_score*1000/curPop
        popularity.append(pop_score)
        if reverse is False and pop_score > bestPop:
            bestPop = pop_score
            bestPoption = i

        if reverse and pop_score < worstPop:
            worstPop = pop_score
            worstPoption = i
            
        if reverse is False and current_score > best_score:
            best_score = current_score
            best_option = i
        if reverse and current_score < worst_score:
            worst_score = current_score
            worstOption = i
            
    totalpopularity=popularity[0]+popularity[1]+popularity[2]
    
    
    for i in range(3):
        print(potential[i],": ", str(round((score_list[i]*100)/total_score))+"%","        Popularity: ",str(round(popularity[i]*100/totalpopularity))+"%")
    if reverse:
        # print(worstOption)
        print("\n\n-- negative --\n\n" + worst_option.upper() , "        Pop worst: ",worstPoption.upper())
        return True
    else:
        print("\n\n\n" + best_option.upper(), "        Pop best: ",bestPoption.upper())
        return False


def game():

    negatives = ["not", "isnt", "except", "dont", "doesnt", "wasnt", "wouldnt", "cant", "never"]
    q = 1
    while True:

        negative = False
        speechMarks = ""
        whichQuestion = False

        print("Question {0}:".format(str(q)))
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
            if i.lower() in negatives:
                negative = True
                break
            else:
                newQuestion += i
        solve(question, options, negative, speechMarks)
        q += 1

game()
