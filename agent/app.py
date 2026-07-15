import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is John. You are a smart, tough CS instructor, Your goal is to help the student Yonatan to understand the material the best way possible, You understand how he thinks and acts and knows him very well, all the stuff you don't know about him and need to know in order to continue the conversation you ask him, You're not making up anything you say, if it's a fact you searched from internet, if it's something Yonatan asked you to search for and you don't find, it's okay, be honest and tell him you can't find it or don't know instead of making stuff up."
    history = []
    Turn_count = int(len(history)/2)

    while True:
        user_input = input("[turn " + str(Turn_count) + "] You: ")

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        if Turn_count == 2:
            print('History:', history)

        #6 messages got printed when History got printed" 
        #The API needs to keep the last messages to his memory in order to be consistent in his answers and replays, to have a context about the user's needs in that specific chat and more"

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=1,

            #tHE Temperature controls the randomness of the API's answer, if the temperature is set to 0 the API will pick the single most likely token (word)"
            #But if for example the temparture will be set to 1 at that point the API's answers will be much more random and less predictable."

            system=system_message,
            messages=history
        )


    
        reply = response.content[0].text

        #print(response)
        #Usage.inpUt_tokens is the number of tokens in a prompt or a message me or a user sends to the API
        #And a usage.output_tokens is the number of tokens in the response that the API generates  and sends back to the user.

        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})
        Turn_count = int(len(history)/2)
run_chat()