from ddgs import DDGS
from typing import List, Dict
import traceback

import random
import time

def search_web(query: str, max_results: int = 10, engine: str = "google") -> List[Dict]:
    """
    Smart search that simulates Google/Yahoo/Bing results via DuckDuckGo backend.
    
    Args:
        query (str): The search term.
        max_results (int): Number of results to return.
        engine (str): 'google', 'yahoo', 'bing', or 'duckduckgo'. 
                      Note: DDG is the underlying provider but we can tweak headers/regions if needed 
                      or just treat them all as high-quality web searches.
    """
    print(f"Searching for '{query}' using engine: {engine}")
    
    # We can add more engines here later (e.g. scraping other providers), 
    # but for now we stick to DDG as it's the most reliable free 'Google-like' result provider.
    # To make it 'smarter', we can try to fetch more results and filter them.
    
    try:
        with DDGS() as ddgs:
            # Fetch a bit more to filter
            raw_results = list(ddgs.text(query, max_results=max_results + 5))
            
        # Basic finding: DDG results are already quite good. 
        # We can simulate 'Yahoo' or others by just returning the same high-quality links 
        # or potentially re-ordering them if we had specific criteria.
        
        # Deduplicate results based on URL
        seen_urls = set()
        clean_results = []
        for r in raw_results:
            if r['href'] not in seen_urls:
                seen_urls.add(r['href'])
                clean_results.append({
                    "title": r['title'],
                    "link": r['href'],
                    "snippet": r['body'],
                    "source": "Web"
                })
        
        return clean_results[:max_results]

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
