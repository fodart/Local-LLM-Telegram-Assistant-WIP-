import requests
from flask import Flask, request, jsonify

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.1:8b" #You can write here your Ollama model

#You can write here your own SYSTEM_PROMPT
SYSTEM_PROMPT = """ 
  
"""


sessions = {}

app = Flask(__name__)

@app.route("/message", methods=["POST"])
def handle_message():
    data = request.get_json() 

    chat_id = data.get("chat_id")
    text = data.get("text")
    source = data.get("source")

    print("=== NEW MESSAGE ===")
    print("chat_id:", chat_id)
    print("source:", source)
    print("text:", text)
    print("===================")

    if chat_id not in sessions:
      sessions[chat_id] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        ]
      

    sessions[chat_id].append({"role": "user", "content": text})

    reply = call_llm(sessions[chat_id])
    
    sessions[chat_id].append({"role": "assistant", "content": reply})

    return jsonify({
        "type": "text",
        "content": reply,
        "chat_id:": chat_id
    })

def call_llm(messages):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": messages,
            "stream": False
        }
    )
    return response.json()["message"]["content"]

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
