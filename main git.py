from openai import OpenAI
from datetime import datetime
import json
import os

client = OpenAI (
    base_url="https://api.xxxxx.com/v1", # Insert api url here
    api_key="sk-xxxxxxxxxxxxxxxx" # Insert api key here
)

history =[]

while True:
    userMsg=input("Masukkan Prompt Yang Akan Dikirim Ke API Endpoint: ")

    if userMsg == "/quit":
        break

    if userMsg == "/clear":
        history.clear()
        print ("History Cleared!")
        continue

    if userMsg == "/save":
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"chat_{timestamp}.json"
        with open(filename, "w") as hstry:
            json.dump(history, hstry)
        print("Chat saved! You can safely close this terminal now.")
        continue

    if userMsg == "/list":
        all = os.listdir()
        chatto = [chat for chat in all if chat.startswith("chat_") ]
        all.sort()
        print ("This is the chat list!")
        print (chatto)
        continue
    
    if userMsg.startswith("/load"):
        parts = userMsg.split()
        if len(parts) == 1:
            print ("Choose which chat to load!, use /list to see all saves")
            continue
        else:
            number = int(parts[1])
            print (f"Okay! Loading chat {number}...")

            all = os.listdir()
            chatto = [chat for chat in all if chat.startswith("chat_") ]
            all.sort()
            
            file = chatto[number - 1]
            try:
                with open(file, "r") as hstry: 
                    history = json.load(hstry)
                print("Chat loaded!")
            except FileNotFoundError:
                print("There is no history, check the file?")
            continue
    
    if userMsg == "/history":
        print(json.dumps(history, indent=2))
        continue

    try:
        response = client.chat.completions.create(
            model="mistral-medium-latest",
            messages=history + [{"role": "user", "content": userMsg}] # Temp history yada yada
        )

        history.append({"role": "user", "content": userMsg})
        history.append({"role": "assistant", "content": response.choices[0].message.content})

        print(response.choices[0].message.content)
    except Exception as error:
        print ("Error: ",error)
