import os
import requests
import getpass
import json
from typing import List
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display
from openai import OpenAI
import gradio as gr

system_prompt = "You are a helpful assistant that responds in markdown"

def stream_gpt(prompt, model, temperatureVal=1.0):
    openai = OpenAI()
    prompt_messages = [
        {"role": "system", "content": "You are a helpful assistant that responds in markdown"},
        {"role": "user", "content": prompt}
    ]
    print(f"Streaming response for model: {model}")
    try:
        temperature = float(temperatureVal)
    except (ValueError, TypeError):
        temperature = 1.0
    print(f"Temperature set to: {temperature}")
    response_stream = openai.chat.completions.create(model=model, temperature=temperature, stream=True, messages=prompt_messages)
    full_response = ""
    for chunk in response_stream:
        if hasattr(chunk.choices[0].delta, 'content') and chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content
            yield full_response

def main():
    print("Welcome to the GenAI Chat!")
    # Here you would implement the chat functionality
    # For example, initializing a chat session, processing user input, etc.
    # This is a placeholder for the actual chat logic.
    
    file = open("OpenAIKey", "r")
    content = file.read()
    file.close()
    os.environ["OPENAI_API_KEY"] = content

    load_dotenv(override=True)
    api_key = os.getenv('OPENAI_API_KEY')

    openai = OpenAI()

    system_message = "You are an assistant that is great at telling jokes"
    user_prompt = "Tell a light-hearted joke for an audience of Data Scientists"

    prompts = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_prompt}
  ]
    completion = openai.chat.completions.create(model='gpt-3.5-turbo', messages=prompts)
    print(completion.choices[0].message.content)

    view = gr.Interface(
        fn=stream_gpt,
        inputs=[
            gr.Textbox(label="Your message:"),
            gr.Dropdown(choices=["gpt-4.1", "gpt-3.5-turbo", "gpt-4o-mini"], label="Model"),
            gr.Textbox(label="Temperature", value="1.0")
        ],
        outputs=[gr.Markdown(label="Response:")],
        flagging_mode="never"
    )
    view.launch(share=True)


if __name__ == "__main__":
    import sys
    # Check if the script is being run directly
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        main()
    else:
        print("Please run this script with 'run' argument to start the chat.")
