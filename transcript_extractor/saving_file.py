def save_transcript_to_file(transcript, output_path):
    """
    Save the transcript to a file.
    
    Args:
        transcript (str): The transcript text
        output_path (str): Path to save the file
    
    Returns:
        bool: Success status
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(transcript)
        return True
    except Exception as e:
        print(f"Error saving transcript: {e}")
        return False