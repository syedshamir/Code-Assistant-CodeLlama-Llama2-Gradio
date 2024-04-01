import requests
import json
import gradio as gr

#backend
url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type':'application/json'
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model":"codeguru",
        "prompt":final_prompt,
        "stream":False    
    }

    response = requests.post(url, headers = headers, data = json.dumps(data))

    if response.status_code == 200: #successful
        response = response.text
        data = json.loads(response)
        actual_reponse = data['response']
        return actual_reponse
    
    else:
        print("error", response.text)

 #Front End

interface = gr.Interface(
    fn = generate_response,
    inputs = gr.Textbox(lines = 4, placeholder= "Enter your Prompt"),
    outputs = "text"
)       
interface.launch()