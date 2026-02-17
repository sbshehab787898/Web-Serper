from ddgs import DDGS
from typing import List, Dict
import traceback

import random
import time

import random
import time
from googlesearch import search as google_search

def search_web(query: str, max_results: int = 10, engine: str = "google") -> List[Dict]:
    """
    Intelligent search that combines results from Google and DuckDuckGo (aggregator).
    
    Args:
        query (str): The search term.
        max_results (int): Number of results to return.
        engine (str): 'google', 'yahoo', 'bing', 'duckduckgo', or 'all'.
    """
    print(f"Searching for '{query}' using engine: {engine}")
    
    combined_results = []
    seen_urls = set()

    # 1. Google Search (Top Priority)
    if engine in ["google", "all"]:
        print("Fetching from Google...")
        try:
            # Fetch slightly more to account for duplicates/promoted content
            g_results = google_search(query, num_results=max_results + 2, advanced=True)
            for r in g_results:
                if r.url not in seen_urls:
                    seen_urls.add(r.url)
                    combined_results.append({
                        "title": r.title,
                        "link": r.url,
                        "snippet": r.description,
                        "source": "Google"
                    })
        except Exception as e:
            print(f"Google search error: {e}")

    # 2. DuckDuckGo Search (Fallback & Diversity)
    # DDG is great for privacy and covers Bing/Yahoo index
    if engine in ["duckduckgo", "bing", "yahoo", "all"] or (engine == "google" and not combined_results):
        print("Fetching from DuckDuckGo...")
        try:
            with DDGS() as ddgs:
                ddg_results = list(ddgs.text(query, max_results=max_results + 5))
                for r in ddg_results:
                    if r['href'] not in seen_urls:
                        seen_urls.add(r['href'])
                        combined_results.append({
                            "title": r['title'],
                            "link": r['href'],
                            "snippet": r['body'],
                            "source": "DuckDuckGo"
                        })
        except Exception as e:
            print(f"DuckDuckGo search error: {e}")

    # 3. Intelligent Ranking & Filtering
    # If we have results from both, Google is already first (prioritized).
    return combined_results[:max_results]

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
