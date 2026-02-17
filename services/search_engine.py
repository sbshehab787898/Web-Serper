from ddgs import DDGS
from typing import List, Dict
import traceback

def search_web(query: str, max_results: int = 10) -> List[Dict]:
    """Search for organic web results."""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        return results
    except Exception as e:
        print(f"Error searching web: {e}")
        traceback.print_exc()
        return []

def search_images(query: str, max_results: int = 10) -> List[Dict]:
    """Search for images."""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.images(query, max_results=max_results))
        return results
    except Exception as e:
        print(f"Error searching images: {e}")
        traceback.print_exc()
        return []

def search_videos(query: str, max_results: int = 10) -> List[Dict]:
    """Search for videos."""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.videos(query, max_results=max_results))
        return results
    except Exception as e:
        print(f"Error searching videos: {e}")
        traceback.print_exc()
        return []

if __name__ == "__main__":
    # Test
    print("Web Search:", search_web("python programming")[0])
    print("Image Search:", search_images("python logo")[0])
    print("Video Search:", search_videos("python tutorial")[0])
