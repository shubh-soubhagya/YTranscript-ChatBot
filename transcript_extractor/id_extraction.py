from urllib.parse import urlparse, parse_qs
import re

def extract_video_id(url):
    """
    Extract the video ID from a YouTube URL.
    
    Args:
        url (str): The YouTube URL
    
    Returns:
        str: The video ID or None if not found
    """
    # Handle different URL formats
    if 'youtu.be' in url:
        return url.split('/')[-1].split('?')[0]
    
    if 'youtube.com/watch' in url:
        parsed_url = urlparse(url)
        return parse_qs(parsed_url.query).get('v', [None])[0]
    
    # Handle YouTube shorts
    if 'youtube.com/shorts/' in url:
        return url.split('/')[-1].split('?')[0]
    
    # Try to find a video ID pattern directly
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    if match:
        return match.group(1)
    
    return None
