# GPT Conversation Bot

## Overview

This project is a conversational bot designed to interact with users through voice. Using a Large Language Model (LLM) for natural language understanding, Speech-to-Text (STT) for audio transcription, and Text-to-Speech (TTS) for audible responses. The application is designed to be fast, intuitive, and (mostly offline), offering seamless conversational experience to the users.

## Features

- Audio Transcription: Converts customer voice input into text. Using an offline whipsper speech recognition model.
- Natural Language Understanding: Utilizes LLMs to understand and generate appropriate responses.
- Text-to-Speech: Converts generated text responses into audible messages. Using MacOS's built in voice. 
- Smart Silence Detection: Efficiently detects when the customer has stopped speaking to proceed with the conversation. (Not so smart right now)

High level flow:
Loop:
    Audio -> STT -> LLM -> TTS -> Audio 

## Prerequisites

- Mac
- Python 3.8+
- Virtual Environment (`venv`)
- Portaudio, `brew install portaudio` [reference](https://github.com/Uberi/speech_recognition/blob/master/README.rst#pyaudio-for-microphone-users)
- OpenAI API key, [reference](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)
- MacOS system voice

**Quickstart**

```bash
git clone https://github.com/JoeyWangTW/gpt-conversation-bot.git
cd gpt-converersation-bot
sh run.sh
```

## Setup and Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/JoeyWangTW/gpt-conversation-bot.git
    cd gpt-converersation-bot
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv myenv
    ```

    **Activate the Virtual Environment**

    - On macOS and Linux:
        ```bash
        source myenv/bin/activate
        ```
    - On Windows:
        ```bash
        .\myenv\Scripts\activate
        ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Setup OpenAI API Key**

    ``` bash
    export OPENAI_API_KEY=xx-xxxxxxxxxx
    ```


5. **Run the Program**

    ```bash
    python src/main.py
    ```

## Usage

### Conversation Bot
1. Run the program.
2. Speak into the microphone when prompted.
3. The assistant will process your request and respond audibly.
4. `Ctrl + c` to quit

If you want to enter your own system prompt, edit `system_prompt.txt`

### Experiment with LangChain and Prompts

Very useful short coures [DeepLearning.ai + LangChain](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/)

1. Run Jupyter notebook
   ```bash
   jupyter notebook   
   ```
2. Open notebook in `/notebooks`

#### Optional: Making the Virtual Environment Available in Jupyter
If you want to make your virtual environment selectable in Jupyter Notebooks, you can install the ipykernel package and add your virtual environment to Jupyter:

1. Install ipykernel:

    ``` bash
    pip install ipykernel
    ```

2. Add your virtual environment to Jupyter:

    ``` bash
    python -m ipykernel install --user --name=myenv
    ```

Replace myenv with whatever name you want to give this environment in Jupyter.
Now, when you start Jupyter Notebook, you'll have the option to select this environment as a kernel, allowing you to switch between different environments within Jupyter.

## Mac system voice setup
Follow this [guide from apple](https://support.apple.com/guide/mac-help/change-the-voice-your-mac-uses-to-speak-text-mchlp2290/mac)

- Download a voice you like
- Select voice and speed in system settings

## Next Steps
- Better audio recording, smarter silence detection
- Evaluate latency in each steps, allow offline/online tts, stt selection for best latency & performance
- Managible LangChian prompts


The initial idea was to create a personal assistant to call and negotiate with customer services. Since they are using bots, I think it's time to have our own bots too. Maybe will try to develop something that specialized in this task. 
- Call transfer selection
- Waiting music - real agent detection
- Goal setting and context
- More...

## Inspiration
- [talk-to-chatgpt](https://github.com/AllAboutAI-YT/talk-to-chatgpt)
- [PI](https://pi.ai/talk)
