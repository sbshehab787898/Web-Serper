import requests
from bs4 import BeautifulSoup
from typing import Dict, Any
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_website(url: str) -> Dict[str, Any]:
    """Visit a website and return its content."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove scripts and styles
        for script in soup(["script", "style"]):
            script.decompose()
            
        text = soup.get_text()
        
        # Clean text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return {
            "url": url,
            "title": soup.title.string if soup.title else "",
            "content": text[:5000], # Limit content length
            "html": str(soup)[:10000],  # Return truncated HTML if needed
            "status_code": response.status_code
        }
    except Exception as e:
        return {"error": str(e), "url": url}
