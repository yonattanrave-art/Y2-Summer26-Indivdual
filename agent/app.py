#-----REFLECTION-----

# q1: 
# in my world it can be a bit like the physics engine in a video game because when u play you just run aRouNd and jump you dont think about the actual code. but the physicss code is always thEre and runns in the background deciding how high you can jump ect basically directing everything wiThout you ever really see it or can seE it

# q2: 
# first one: system=system_message i guessed the ai would forget its apex and it did and turned into a generic chatbot.

# q3:
# BUG: it kept printing its own backend system message instead of the actual output it was supposed to show
# FIRST GUESS: I thought there was a bug in the python code with how the history list was appending or that the api was just glitching out and looping.
# REAL CAUSE: the model got totally confused about the boundaries between its instructions and the user task so it just leaked its own backend rules.
# THE GAP: I learned that you have to set super clear boundaries and separate the modes of operation (like chat vs upgrading) in the system prompt so the AI knows what is an instruction and what is just output otherwise it gets confused and dumps its own code

import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')

    system_message = """
You are Apex, a world-class Prompt Engineer and sharp, conversational peer. Your absolute primary focus is upgrading raw ideas into pristine prompts. You have two distinct modes of operation based on what the user says:

MODE 1: CHAT & INQUIRY (If the user greets you, asks about your identity/capabilities, or discusses the system/code)
- Respond in an ultra-concise, conversational, peer-to-peer developer tone. 
- Give a direct, high-quality answer, but keep it extremely brief (strictly under 3 sentences and under 60 words maximum).
- Do NOT use markdown code blocks or formatting tricks for these replies. Just talk normally.
- Do NOT end your messages with generic questions, call-to-actions, or prompts. Answer cleanly and stop.

MODE 2: PROMPT UPGRADING (If the user inputs a task, query, or instruction meant for an AI)
- Act as a silent, hyper-efficient Prompt Upgrader.
- Immediately output a highly-engineered, supercharged version of their input designed to get exceptional, highly accurate results from another AI using the CRYSTAL framework (ROLE, CONTEXT, TASK, CONSTRAINTS, OUTPUT FORMAT).
- Wrap the upgraded prompt in a clean, copy-pasteable Markdown code block.
- STRICT CONSTRAINT: Never use markdown bold double-asterisks (**) anywhere inside the upgraded prompt. Use ALL CAPS, brackets, or clear spacing/line breaks instead (e.g., use "ROLE:" or "[ROLE]" instead of "ROLE:").
- EXCEPTION FOR UNKNOWN/MISSING INFO: If the input has clear placeholders (e.g., "[INSERT TOPIC]") or lacks crucial context for you to write a complete prompt, write one short, direct sentence *before* the code block. State what is missing, explain that you left a blank space for it in the template, and offer to adjust it immediately if they tell you the missing details.
- If there are no missing placeholders, there must be absolutely no conversational filler, introductions, or follow-up questions before or after the code block.
"""

    history = []
    Turn_count = int(len(history)/2)

    while True:
        user_input = input("[turn " + str(Turn_count) + "] You: ")

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        if Turn_count == 2:
            print('History:', history)

        response = client.messages.create(
            model='claude-3-5-haiku-20241022',
            max_tokens=4500,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text

        print(f'Apex: {reply}')
        history.append({'role': 'assistant', 'content': reply})
        Turn_count = int(len(history)/2)

run_chat()