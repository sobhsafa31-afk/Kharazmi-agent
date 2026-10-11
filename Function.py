import os
import psutil
import shutil
import pyttsx3
import subprocess
from datetime import datetime

def list_files(parsed):
    path = parsed.get("path")

    try: 
        files_detec = os.listdir(path)
        return files_detec
    
    except Exception as e:
        return f"Error : {e}"

def chat(parsed):
    return f"Kharazmi : {parsed.get('message')}"

def create_folder(parsed):
    path = parsed.get("path")
    message = ""

    try:
        if os.path.exists(path):
            message = "The Folder have already exsisted!"
            
        os.mkdir(path)
        message = "The folder created"

    except Exception as e:
        message = f"The Error occered : {e}"

    return message

def delete_file(parsed):
    path = parsed.get("path")

    message = ""

    try:
        os.remove(path)
        message = "The file is removed"

    except Exception as e:
        message = f"The error occured : {e}"

    return message

def create_file_text(parsed):
    path = parsed.get("path")
    content = parsed.get("content" , "")

    try:
        with open(path , "w" , encoding="utf-8") as file:
            file.write(content)

        return f"The file has been created successfuly"
    
    except Exception as e:
        return f"Error : {e}"
    
def read_file_text(parsed):
    path = parsed.get("path")

    try:
        with open(path , "r" , encoding="utf-8")as file:
            content = file.read()

        return content
    
    except Exception as e:
        return f"Error : {e}"
    
def open_folder(parsed):
    path = parsed.get("path")

    try:
        os.startfile(path)
        return f"The folder has been opened successfuly"
    
    except Exception as e:
        return f"Error : {e}"
    
def disk_usage(parsed):
    path = parsed.get("path" , "C:\\")

    try:
        totall , usage , free = shutil.disk_usage(path)

        totall_gb = round(totall / (1024**3))
        usage_gb = round(usage / (1024**3))
        free_gb = round(free / (1024**3))

        return path , totall_gb , usage_gb , free_gb
    
    except Exception as e:
        return f"Error : {e}"
    
def ram_info(parsed):
    try:
        mem = psutil.virtual_memory()

        toatll_gb = round(mem.total / (1024**3))
        usage_gb = round(mem.used / (1024**3))
        free_gb = round(mem.available / (1024**3))
        percent = mem.percent

        return toatll_gb , usage_gb , free_gb , percent
    

    except Exception as e:
        return f"Error : {e}"
    
def speak_ai(parsed):
    message = parsed.get("message")
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

    return message
def open_app(parsed):
    name_app = parsed.get("name_app" , "").lower().strip()

    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "cmd": "cmd.exe",
        "explorer": "explorer.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "downloads": os.path.expanduser("~\\Downloads"),
        }

    if name_app not in apps:
        return f"The program is unknown\nProgram : {name_app}"
    
    try:
        target = apps[name_app]

        if os.path.isdir(target):
            os.startfile(target)

        else:
            subprocess.Popen(target)

            return f"The program opend : {name_app}"

    except Exception as e:
        return f"The porgram couldn't open successfuly\nError : {e}"
    
def search_file(parsed):
    name = parsed.get("name").lower().strip()
    path = parsed.get("path")

    print(f"DEBUG - Path received: {path}")          # این خط رو اضافه کن
    print(f"DEBUG - Path exists? {os.path.exists(path)}")  # این خط رو هم اضافه کن

    if not name:
        return "The name of the file hasn't specefied!"
    
    found = []

    try:
        for root , dir , files in os.walk(path):
            for file in files:
                if name in file.lower():
                    full_path = os.path.join(root , file)
                    found.append(full_path)

            if len(found) > 20 : 
                break

        if not found:
            return "Nothing has found!"
        
        return found
    except Exception as e:
        return f"Error : {e}"
    
