# HQ-Bot
A python bot which gathers and (sometimes) solves questions from the HQ trivia app.

## Requirements

Python 3.5 used, the significant packages that were used are:

* pyautogui - Taking Screenshots of the game
* pytesseract - The OCR of the question
* requests - Getting how many results google comes up with

LonelyScreen is an IOS screen mirroring application that can be downloaded [here][LonelyScreenLink], the download of this application is required.

# Installation
Windows:

  1) Install [Python 3.5][PythonLink]

  2) Install [LonelyScreen][LonelyScreenLink]

  3) Go to Command Prompt and type the following commands sequentially

  * pip install pyautogui
  * pip install pytesseract

  (If you have an error, try reinstalling python and ensure that the "Add Python to PATH" box is ticked)


  [PythonLink]: https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe
  [LonelyScreenLink]: https://www.lonelyscreen.com/download.html
