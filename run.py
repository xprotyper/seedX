import pyautogui
import time
import pyperclip

def read_phrases_from_file(file_path):
    pass

def paste_text(phrase):
    pass

    time.sleep(1)  
    if phrase in pyperclip.paste():
        print(f"{phrase.strip()}\n")

def get_balance():
    pass

    time.sleep(1)
    balance = pyperclip.paste()
    print(f"Balance: {balance}\n")

def tranfert_money():
    pass


phrases_file_path = 'a.txt'

phrases = read_phrases_from_file(phrases_file_path)

# Assuming the website input field is in focus
for phrase in phrases:
    phrase = phrase.strip()  # Remove leading/trailing whitespaces
    paste_text(phrase)
