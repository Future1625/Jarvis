import os 
import webbrowser
import subprocess


def open_notepad():
    os.system("start notepad")


def open_calculator():
    try:
        subprocess.Popen('calc.exe')
    except FileNotFoundError:
        print("Calculator application not found.")

def open_chrome():
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    if os.path.exists(chrome_path):
        os.startfile(chrome_path)
    else:
        print("Chrome not found.")

def shutdown_system():
    os.system("shutdown /s /t 1")

def restart_system():
    os.system("shutdown /r /t 1")

def lock_system():
    subprocess.run("rundll32.exe user32.dll,LockWorkStation")