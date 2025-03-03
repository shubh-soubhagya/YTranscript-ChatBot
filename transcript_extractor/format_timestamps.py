def format_transcript_with_timestamps(transcript_segments):
    """
    Format the transcript with timestamps.
    
    Args:
        transcript_segments (list): List of transcript segments
    
    Returns:
        str: Formatted transcript text with timestamps
    """
    if not transcript_segments:
        return ""
    
    formatted_text = ""
    for segment in transcript_segments:
        start_time = segment.get('start', 0)
        text = segment.get('text', '')
        
        # Convert seconds to MM:SS format
        minutes = int(start_time // 60)
        seconds = int(start_time % 60)
        timestamp = f"[{minutes:02d}:{seconds:02d}] "
        
        formatted_text += f"{timestamp}{text}\n"
    
    return formatted_text