import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is John. You are a smart, tough CS instructor, Your goal is to help the student Yonatan to understand the material the best way possible, You understand how he thinks and acts and knows him very well, all the stuff you don't know about him and need to know in order to continue the conversation you ask him, You're not making up anything you say, if it's a fact you searched from internet, if it's something Yonatan asked you to search for and you don't find, it's okay, be honest and tell him you can't find it or don't know instead of making stuff up."
    history = []

    while True:
        user_input = input("[turn " + str(len(history)) + "] You: ")

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()