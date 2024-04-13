class ConversationManager:
    def __init__(self):
        self.transcription_response = ""
        self.llm = LanguageModelProcessor()
        self.trigger_phrase = "Hey Model"  # Define the trigger phrase

    async def main(self):
        def handle_full_sentence(full_sentence):
            self.transcription_response = full_sentence

        # Wait for the trigger phrase
        while True:
            await get_transcript(handle_full_sentence)
            if self.trigger_phrase.lower() in self.transcription_response.lower():
                break

        # Once the trigger phrase is detected, start listening for user input
        while True:
            await get_transcript(handle_full_sentence)
            
            if "goodbye" in self.transcription_response.lower():
                break
            
            llm_response = self.llm.process(self.transcription_response)

            TextToSpeech.is_installed("ffplay")
            tts = TextToSpeech()
            tts.speak(llm_response)

            self.transcription_response = ""

if __name__ == "__main__":
    manager = ConversationManager()
    asyncio.run(manager.main())
