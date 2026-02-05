from openai import OpenAI
from datetime import datetime
import json
import os

### CONFIGURATION ###
API_URL = "https://api.xxxxx.com/v1" # Insert api url here
API_KEY = "sk-xxxxxxxxxxxxxxxx" # Insert api key here
MODEL_NAME = "mistral-medium-latest"  # Placeholder. Select models here, open "api-url/v1/models" on web
### END ###

client = OpenAI (
    base_url=API_URL,
    api_key=API_KEY,
)

history =[]

def save_chat(history):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"chat_{timestamp}.json"
    with open(filename, "w") as hstry:
        json.dump(history, hstry)
    print("Chat saved! You can safely close this terminal now.")

def list_chat():
    all = os.listdir()
    chatto = [chat for chat in all if chat.startswith("chat_") ]
    chatto.sort()
    print ("This is the chat list!")
    print (chatto)

def load(number):
    all = os.listdir()
    chatto = [chat for chat in all if chat.startswith("chat_") ]
    chatto.sort()
    
    file = chatto[number - 1]

    try:
        with open(file, "r") as hstry: 
            loaded_history = json.load(hstry)
        print("Chat loaded!")
        return loaded_history
    except FileNotFoundError:
        print("There is no history, check the file?")
        return None

def list_history():
    if len(history) == 0:
            print("No conversation yet!")
    else:
        print("Here is the history of the chat:")
        print(json.dumps(history, indent=2))

def send_msg(history, userMsg):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=history + [{"role": "user", "content": userMsg}] # Temp history yada yada, dont touch if u dont know what u do
        )
        return response.choices[0].message.content
    except Exception as error:
        print ("Error: ",error)
        return None



while True:
    userMsg=input("Enter the prompt that will be sent to the API endpoint: ")

    if userMsg == "/quit":
        break

    if userMsg == "/clear":
        history.clear()
        print ("History Cleared!")
        continue

    if userMsg == "/save":
        save_chat(history)
        continue

    if userMsg == "/list":
        list_chat()
        continue
    
    if userMsg.startswith("/load"):
        parts = userMsg.split()

        if len(parts) == 1:
            print ("Choose which chat to load!, use /list to see all saves")
            continue
        else:
             number = int(parts[1])
             loaded = load(number)

        if loaded is not None:
             history = loaded
             continue
    
    if userMsg == "/history":
        list_history()
        continue

    ai_response = send_msg(history, userMsg)
    if ai_response:
        history.append({"role": "user", "content": userMsg})
        history.append({"role": "assistant", "content": ai_response})
        print(f"\nAI: {ai_response}\n")