# HQ-Bot
A python bot which gathers and (sometimes) solves questions from the HQ trivia app.
This works for iPhones only and should work for both Windows and MacOS (Although only tested on windows)

The goal of this project was to make a program that could try solve a HQ question fast and accurately

## Requirements

Python 3.5 used, the significant packages that were used are:

  * pyautogui - Taking Screenshots of the game
  * pytesseract - The OCR of the question
  * requests - Getting how many results google comes up with

LonelyScreen is an IOS screen mirroring application that can be downloaded [here][LonelyScreenLink], the download of this application is required.

## Installation
Windows:

  1) Install [Python 3.5][PythonLink]

  2) Install [LonelyScreen][LonelyScreenLink]

  3) Go to Command Prompt and type the following commands sequentially

    * pip install pyautogui
    * pip install pytesseract

    (If you have an error, try reinstalling python and ensure the "Add Python to PATH" box is ticked)

  4) Install the tesseract training files [here][TesseractFile] and follow installation steps.

  5) Ensure you have an Apple device and an IOS version that can support AirPlay.

## Usage

(NOTE: This script only works for one monitor - please disable any secondary monitors you have. Also please ensure that GUI scaling is set to 100%, as this can mess up where the screenshot is taken)

1) Open LonelyScreen and make it FULL SCREEN.

2) Connect your iPhone to LonelyScreen by swiping up from the bottom of your IOS device and clicking the TV looking icon, then click the option presented.

3) Open the HQBot.py file, ensure that this is in the foreground but not obstructing your view of your device on the screen.

4) When a question comes up on HQ Trivia press the enter key in the bot window, the suggested answer will be given to you along with the popularity adjusted result.

## Tips to go far

 If the popularity result and the actual result are the same, then that answer is safe to assume correct.

 The popularity result should probably be used when there is a large gap in popularity score between each result.

 Finally, the actual result should be used when the popularity scores are too close to assume an answer.

  [TesseractFile]: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.02-20180621.exe
  [PythonLink]: https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe
  [LonelyScreenLink]: https://www.lonelyscreen.com/download.html
