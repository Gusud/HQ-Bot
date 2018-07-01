# HQ-Bot
A python bot which gathers and (sometimes) solves questions from the HQ trivia app.
This works for iPhones only and should work for both Windows and MacOS (Although only tested on windows)

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

  4) Ensure you have an internet connection and an iPhone that can support AirPlay.

# Usage

(NOTE: This script only works for one monitor - please disable any secondary monitors you have. Also please ensure that GUI scaling is set to 100%, as this can mess up where the screenshot is taken)

1) Open LonelyScreen and make it FULL SCREEN.

2) Connect your iPhone to LonelyScreen by swiping up from the bottom of your IOS device and clicking the TV looking icon, then click the option presented.

3) Open the HQBot.py file, ensure that this is in the foreground but not obstructing your view of your device on the screen.

4) When a question comes up on HQ Trivia press enter in the bot window and the hint will be given to you.

  [PythonLink]: https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe
  [LonelyScreenLink]: https://www.lonelyscreen.com/download.html
