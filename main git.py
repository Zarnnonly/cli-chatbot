from openai import OpenAI
import json

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
        with open("chat_history.json", "w") as hstry:
            json.dump(history, hstry)
        print("Chat saved! You can safely close this terminal now.")
        continue
    
    if userMsg == "/load":
        try:
            with open("chat_history.json", "r") as hstry: 
                history = json.load(hstry)
            print("Chat loaded!")

        except FileNotFoundError:
            print("There is no history, check the file?")
        continue

    try:
        response = client.chat.completions.create(
            model="mistral-medium-latest",
            messages=history + [{"role": "user", "content": userMsg}]
        )

        history.append({"role": "user", "content": userMsg})
        history.append({"role": "assistant", "content": response.choices[0].message.content})

        print(response.choices[0].message.content)
    except Exception as e:
        print ("Error: ",e)
