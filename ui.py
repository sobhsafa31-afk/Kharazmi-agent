import customtkinter as ctk
import json
import requests
from Function import *
from data_base import *

#API
ACCOUNT_ID = "PUT YOUR ACCOUNT ID"
API_TOKEN = "PUT YOUR TOKEN"

url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/meta/llama-3.1-8b-instruct"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

with open("system_prompet.txt", "r", encoding="utf-8") as file:
    content = file.read()

messages = [
    {
        "role": "system",
        "content": str(content)
    }
]

actions = {
    "list_files": list_files,
    "chat": chat,
    "create_folder": create_folder,
    "delete_file": delete_file,
    "create_file_text": create_file_text,
    "read_file_text": read_file_text,
    "open_folder": open_folder,
    "disk_usage": disk_usage,
    "ram_info": ram_info,
    "open_app": open_app,
    "search_file": search_file
}

#UI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Kharazmi")
app.geometry("900x600")

chat_frame = ctk.CTkScrollableFrame(app , width=860 , height=480)
chat_frame.pack(padx = 20 , pady =(20 , 10) , fill="x")

bottom_frame = ctk.CTkFrame(app , fg_color="transparent")
bottom_frame.pack(padx = 20 , pady =(0 , 20) , fill = "x")

entry = ctk.CTkEntry(bottom_frame , placeholder_text="write your request" , height=40 , font=("Tahoma", 14))
entry.pack(side = "left" , fill = "x" , expand = True , padx = (0 , 10))

send_button = ctk.CTkButton(bottom_frame , text="send" , width=100 , height=40 , font=("Tomha" , 14))
send_button.pack(side ="right")

def add_message(text , sender = "user"):
    if sender == "user":
        bubble_color = "#1f538d"
        text_color = "white"
        anchor = "e"

    else:
        bubble_color = "#2b2b2b"
        text_color = "white"
        anchor = "w"

    message_frame = ctk.CTkFrame(chat_frame , fg_color=bubble_color , corner_radius=12)
    message_frame.pack(padx = 10 , pady = 6 , anchor = anchor)

    lable = ctk.CTkLabel(
        message_frame ,
        text= text,
        text_color= text_color,
        font = ("Tahoma" , 13),
        wraplength=500,
        justify ="left",
        padx = 12,
        pady = 8
    )

    lable.pack()

def process_agent_response(user_text):
    save_messages("user" , user_text)

    data = {
        "messages" : messages + recent_messages(10)
        }

    try:
        response = requests.post(url , headers=headers , json=data , timeout=30)
        result = response.json()

    except Exception as e :
        add_message(f"Erorr API : {result}" , sender="agent")
        return

    if not result.get("success"):
        add_message(f"Erorr API : {result}" , sender="agent")
        return

    answer = result["result"]["response"]

    try:
        if type(answer) == dict or type(answer) == list:
            parsed = answer

        else:
            cleaned = answer.replace("'" , '"')
            parsed = json.loads(cleaned)

    except Exception as e :
        add_message(f"Erorr in processing the answer\n{answer}" , sender="agent")
        return

    if type(parsed) == list:
        steps = parsed

    else:
        steps = [parsed]

    for step in steps:
        action = step.get("action")

        if action == "chat":
            message = step.get("message" , "")
            add_message(message , sender="agent")
            speak_ai(step)

        elif action in actions:
            tool_result = actions[action](step)

            if action == "list_files":
                if type(tool_result) == list:
                    text = "The Files are found :\n" + "\n".join(f"• {f}" for f in tool_result)

                else:
                    text = str(tool_result)

                add_message(text , sender="agent")

            elif action == "ram_info":
                total , usage , free , percent = tool_result

                text = f"The data of Ram:\nTotal : {total} GB\nUsed space : {usage} GB\nFree : {free}\nPercent : {percent}"
                add_message(text , sender="agent")

            elif action == "disk_usage":
                path , total , usage , free = tool_result

                text = f"The data of Disk ({path}) :\nTotal : {total} GB\nUsed space : {usage} GB\nFree : {free} GB"
                add_message(text , sender="agent")

            elif action == "search_file" :
                if type(tool_result) == list:
                    text = "The result of research:\n" + "\n".join(f"• {f}" for f in tool_result)

                else:
                    text = str(tool_result)
                
                add_message(text , sender="agent")

            else:
                add_message(str(tool_result) , sender="agent")

            clear_old_messages

        else:
            add_message(f"The unknown action : {action}" , sender="agent")

def send_message(event=None):
    user_text = entry.get().strip()
    if user_text == "":
        return

    add_message(user_text, sender="user")
    entry.delete(0, "end")

    # غیرفعال کردن دکمه تا جواب نیومده
    send_button.configure(state="disabled")
    entry.configure(state="disabled")

    # اجرای Agent
    process_agent_response(user_text)

    # فعال کردن دوباره
    send_button.configure(state="normal")
    entry.configure(state="normal")
    entry.focus()


send_button.configure(command =send_message)
entry.bind("<Return>" , send_message)

app.mainloop()