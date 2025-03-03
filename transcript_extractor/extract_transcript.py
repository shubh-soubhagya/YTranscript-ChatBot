from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from transcript_extractor.format import format_transcript
from transcript_extractor.id_extraction import extract_video_id
from transcript_extractor.format_timestamps import format_transcript_with_timestamps

def get_transcript(video_url, language=None):
    """
    Get the transcript for a YouTube video.
    
    Args:
        video_url (str): The YouTube video URL
        language (str, optional): Language code for the transcript (e.g., 'en')
    
    Returns:
        dict: Dictionary with 'success', 'transcript' and 'error' keys
    """
    video_id = extract_video_id(video_url)
    
    if not video_id:
        return {
            'success': False,
            'transcript': None,
            'error': 'Could not extract video ID from URL'
        }
    
    # Try to get transcript with YouTube Transcript API
    try:
        if language:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript = transcript_list.find_transcript([language]).fetch()
        else:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Format the transcript
        formatted_transcript = format_transcript(transcript)
        return {
            'success': True,
            'transcript': formatted_transcript,
            'error': None
        }
    
    except (TranscriptsDisabled, NoTranscriptFound) as e:
        error_msg = f"Transcript not available: {str(e)}"
        print(error_msg)
        return {
            'success': False,
            'transcript': None,
            'error': error_msg
        }
    
    except Exception as e:
        error_msg = f"Error retrieving transcript: {str(e)}"
        print(error_msg)
        return {
            'success': False,
            'transcript': None,
            'error': error_msg
        }

def get_transcript_with_timestamps(video_url, language=None):
    """
    Get the transcript with timestamps.
    
    Args:
        video_url (str): The YouTube video URL
        language (str, optional): Language code for the transcript
    
    Returns:
        dict: Dictionary with 'success', 'transcript' and 'error' keys
    """
    video_id = extract_video_id(video_url)
    
    if not video_id:
        return {
            'success': False,
            'transcript': None,
            'error': 'Could not extract video ID from URL'
        }
    
    try:
        if language:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript = transcript_list.find_transcript([language]).fetch()
        else:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Format the transcript with timestamps
        formatted_transcript = format_transcript_with_timestamps(transcript)
        return {
            'success': True,
            'transcript': formatted_transcript,
            'error': None
        }
    
    except Exception as e:
        error_msg = f"Error retrieving transcript: {str(e)}"
        print(error_msg)
        return {
            'success': False,
            'transcript': None,
            'error': error_msg
        }