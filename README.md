# Custom Search & Scraper API

This is a Python-based API built with FastAPI that provides search capabilities (Google/Yahoo/Bing via DuckDuckGo) and website scraping functionality. It is designed to be integrated with automation tools like n8n.

## Features
- **Web Search**: Get search results similar to Google.
- **Image Search**: Find images based on queries.
- **Video Search**: Find videos.
- **Website Scraping**: Visit any URL and extract its text content (useful for AI summarization).

## Setup & Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the API:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the API documentation at: `http://localhost:8000/docs`

## Deploy to Render

1. Create a new **Web Service** on Render.
2. Connect your repository.
3. Set the **Build Command** to: `pip install -r requirements.txt`
4. Set the **Start Command** to: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## n8n Integration

To use this API in n8n, use the **HTTP Request** node.

### 1. Search Web
- **Method**: POST
- **URL**: `https://your-render-app-url.onrender.com/api/search`
- **Body**: JSON
  ```json
  {
    "query": "artificial intelligence news",
    "limit": 5
  }
  ```

### 2. Search Images
- **Method**: POST
- **URL**: `https://your-render-app-url.onrender.com/api/images`
- **Body**: JSON
  ```json
  {
    "query": "cute cats",
    "limit": 5
  }
  ```

### 3. Visit & Scrape Website
- **Method**: POST
- **URL**: `https://your-render-app-url.onrender.com/api/visit`
- **Body**: JSON
  ```json
  {
    "url": "https://en.wikipedia.org/wiki/Artificial_intelligence"
  }
  ```
