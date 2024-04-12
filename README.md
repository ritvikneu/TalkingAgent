# TalkingAgent
<h3> This is Terminal based AI Agent where you can have a talk to a LLM model.Deepgram’s Aura Text to Speech and Nova Speech to Text models and Groq API are used, I have chosen these to have minimum latency and for the feel of real time conversation (Currently these APIs are free to use and subject to change)</h3>

Steps to run the code
- pip install -r requirements.txt
- add your DEEPGRAM_API_KEY and GROQ_API_KEY to .env file
- ensure you have installed portaudio(required for pyaudio), ffmpeg(convert and stream audio) and other required libraries
- python3 TalktoLLM.py


Library and Frameworks used
- [Langchain] (https://www.langchain.com/) 
- [Groq] (https://wow.groq.com/)
- [Deepgram] (https://deepgram.com/)
