# YTranscript-ChatBot

The **YTranscript-ChatBot** is an AI-powered tool designed to enhance video content interaction. It enables users to extract transcripts, ask questions, and receive context-aware answers directly from the terminal. By leveraging advanced AI models, it eliminates the need for manual video reviews, making it an invaluable resource for researchers, professionals, and students. Users can efficiently analyze lectures, tutorials, and discussions without watching entire videos.  

This chatbot boosts productivity with features like transcript downloads and intelligent response generation. Its ability to process YouTube transcripts and provide precise insights makes it a powerful research companion.

---

## 🚀 Features

- **AI-Powered Question Answering**: Get precise answers based on YouTube video transcripts.
- **Terminal-Based Interface**: Simple CLI interface for efficient interactions.
- **Transcript Download**: Extract and save video transcripts in the `temp_files` directory for offline reference.
- **Ideal for Researchers & Professionals**: Quickly analyze lectures, tutorials, and discussions.

## 🖥️ Usage

1. Enter the YouTube video URL.
2. Ask a specific question related to the video content.
3. Get AI-driven responses based on the transcript.
4. Downloaded transcripts are saved in the `temp_files` directory for further analysis if needed.

---

## 🛠 Technologies Used

The chatbot is built using the following libraries:

| Library                        | Version  | Purpose  |
|--------------------------------|----------|-------------------------------------------------------------------------------------------------|
| groq                        | 0.16.0   | Integrates advanced AI language processing capabilities.                                      |
| youtube-transcript-api       | 0.6.3    | Fetches and processes video transcripts directly from YouTube for accurate responses.        |

## 📦 Custom Packages
- **transcript_extractor**: Extracts and preprocesses YouTube video transcripts efficiently.
- **transcriptQA**: Enables AI-driven question-answering functionality using the llama3-70b-8192 model via the Groq inference API.

## 🛠 Installation & Setup

Follow these steps to set up and run the YouTube Support ChatBot on your local machine:

#### 1️⃣ Install Dependencies
Run the following command to install the required libraries:
```bash
pip install -r requirements.txt
```

#### 2️⃣ Configure the .env File
Create a .env file inside the project directory (YouTube-support-chatbot/.env) and add your Groq API key:
```ini
GROQ_API_KEY=<your-api-key>
```

#### 3️⃣ Generate API Key
Obtain your Groq API key by visiting [Groq Console](https://console.groq.com/keys) and copying your key.

#### 4️⃣ Run the Application
Start the chatbot by executing the following command:
```bash
python app.py
```

---

## 💡 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## 📩 Contact
For any queries, reach out via [soubhagyasrivastava240@gmail.com](mailto:soubhagyasrivastava240@gmail.com).

---
*Developed with ❤️ for seamless YouTube content analysis.*

