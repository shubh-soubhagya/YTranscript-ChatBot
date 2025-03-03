from transcript_extractor.extract_transcript import get_transcript, get_transcript_with_timestamps
from transcript_extractor.saving_file import save_transcript_to_file
import os
from groq import Groq
from dotenv import load_dotenv
from transcriptQA.groqllm import ask_groq  # Importing the function to query Groq

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Define transcript file paths
base_path = os.path.join(os.getcwd(), "YTranscript-ChatBot", "temp_files")
transcript_file = os.path.join(base_path, "transcript.txt")
timestamp_file = os.path.join(base_path, "transcripts_with_timestamps.txt")

print("Bot: Hi! I can extract transcripts from YouTube videos and answer questions about them. Send me a YouTube URL to get started!")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! Have a great day!")
        break
    
    print("Bot: Extracting transcript, please wait...")
    result = get_transcript(user_input)
    timestamp_result = get_transcript_with_timestamps(user_input)

    if result['success']:
        save_transcript_to_file(result['transcript'], transcript_file)
        print("Bot: Transcript extracted successfully!")
        
        if timestamp_result['success']:
            save_transcript_to_file(timestamp_result['transcript'], timestamp_file)
            print("Bot: Transcript with timestamps extracted successfully! You can now ask me questions about the video.")
        else:
            print("Bot: Warning! Could not extract transcript with timestamps. Answering based on the plain transcript.")

        while True:
            question = input("You: ")
            if question.lower() in ["exit", "quit", "bye", "new video"]:
                print("Bot: Okay! You can send another YouTube link or type 'bye' to exit.")
                break
            
            # Check if timestamp transcript exists, otherwise use the regular transcript
            if os.path.exists(timestamp_file):
                with open(timestamp_file, "r", encoding="utf-8") as file:
                    transcript_text = file.read()
            else:
                with open(transcript_file, "r", encoding="utf-8") as file:
                    transcript_text = file.read()
            
            answer = ask_groq(question, client=client, transcript_text=transcript_text)
            print("Bot:", answer)
    else:
        print(f"Bot: Failed to extract transcript. {result['error']}")
