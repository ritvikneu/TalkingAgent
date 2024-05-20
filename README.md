## Conversational AI with Deepgram, Groq, and Langchain

This project implements a simple conversational AI system using Deepgram for speech recognition, Groq for large language model processing, and Langchain for managing conversation history and prompt engineering.

### Features:

* **Real-time Speech Recognition:**  Utilizes Deepgram's API to transcribe spoken input in real-time.
* **Large Language Model Interaction:** Integrates with Groq's mixtral-8x7b-32768 model for powerful natural language understanding and generation.
* **Conversation Memory:** Leverages Langchain's ConversationBufferMemory to maintain conversation context.
* **Text-to-Speech:**  Uses ffplay to convert text responses into spoken output.
* **Simple User Interface:**  Basic command-line interaction, allowing users to speak and receive responses from the AI.

### Dependencies:

* **Python 3.8 or higher:** Required for the project's libraries and functionalities.
* **Deepgram:**  Install the Deepgram library: `pip install deepgram`
* **Groq:** Install the Groq library: `pip install langchain_groq`
* **Langchain:** Install the Langchain library: `pip install langchain`
* **requests:** Install the requests library: `pip install requests`
* **ffmpeg:** Install the ffmpeg library: `sudo apt-get install ffmpeg` (Linux) or `brew install ffmpeg` (macOS)

### Setup:

1. **Environment Variables:**
   * Create a `.env` file in the project root directory.
   * Add your API keys:
     ```
     DEEPGRAM_API_KEY=YOUR_DEEPGRAM_API_KEY
     GROQ_API_KEY=YOUR_GROQ_API_KEY 
     ```
   * Obtain API keys from [Deepgram](https://www.deepgram.com/) and [Groq](https://groq.com/).
   * **Important:** Replace `YOUR_DEEPGRAM_API_KEY` and `YOUR_GROQ_API_KEY` with your actual API keys.

2. **System Prompt:**
   * The `system_prompt.txt` file contains the initial instructions for the LLM. 
   * You can customize it to influence the AI's behavior and response style.

### Running the Project:

1. **Installation:** Install the required dependencies (see "Dependencies" section).
2. **Run:** Execute the Python script: `python conversation.py`

### Usage:

* The script will start a live speech recognition session.
* Speak your questions or commands.
* The AI will transcribe your speech, process it with the LLM, and generate a response.
* The response will be spoken back to you via text-to-speech.
* To end the conversation, say "goodbye."

### Example Interaction:

```
User: Hello, how are you today?
AI: I am doing well, thank you for asking! How can I help you?
User: Can you tell me a joke?
AI: Why don't scientists trust atoms? Because they make up everything! 
User: That's funny! Goodbye.
AI: You have a good one Ritvik! 
```

### Customization:

* **LLM Model:** You can change the LLM model by modifying the `model_name` parameter in `LanguageModelProcessor` class.
* **System Prompt:** Adjust the content of the `system_prompt.txt` file to fine-tune the AI's behavior.
* **Text-to-Speech:**  Experiment with different voices and settings in the `TextToSpeech` class.

### Notes:

* The project uses ffplay for text-to-speech, so make sure you have ffmpeg installed (see "Dependencies").
* For optimal performance, ensure a stable internet connection and a quiet environment for speech recognition.
* The AI's responses are based on the LLM's capabilities and the provided system prompt.

### Further Development:

* **Advanced Conversation Management:**  Implement more sophisticated conversation history and context tracking.
* **Multilingual Support:**  Extend the project to handle multiple languages.
* **User Interface:**  Create a graphical user interface for a more user-friendly experience.
* **Domain-Specific Knowledge:**  Integrate specialized knowledge bases or APIs to enhance the AI's capabilities in specific domains.

This project provides a foundation for building more complex and feature-rich conversational AI systems. You can adapt and extend it to suit your specific needs and creative ideas.

**Learn more by doing more, here's where I started <a href="https://www.buildfastwithai.com/#courses">@BuildFastWithAI</a>**
