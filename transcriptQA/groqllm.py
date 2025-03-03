import os

# Dynamically get the correct file path
file_path = os.path.join(os.getcwd(), "YouTube-support-chatbot", "temp_files", "transcripts_with_timestamps.txt")

def load_text(file_path):
    """
    Reads the transcript text file and returns its content.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: transcript file not found."

def ask_groq(question, transcript_text, client):

    transcript_text = load_text(file_path=file_path)
    
    if "Error" in transcript_text:
        return transcript_text  # Return error if the file is missing
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI assistant. You will be given a transcript, and "
                        "your task is to answer questions based on its content accurately."
                        "you can answer outside the content also but related to content topic"
                    ),
                },
                {"role": "user", "content": f"Transcript: {transcript_text}\n\nQuestion: {question}"},
            ],
            model="llama3-70b-8192",
            temperature=0.5,
            max_completion_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )
        
        return chat_completion.choices[0].message.content
    
    except Exception as e:
        return f"Error: {str(e)}"


