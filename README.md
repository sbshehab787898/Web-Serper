# Custom Search & Scraper API (Serper Clone)

This API provides powerful web search and scraping capabilities for your automation workflows (like n8n). It simulates Google/Yahoo searches and can visit any website to extract clean text.

## 🚀 Deployment Guide (Fix for Render)

If your deployment is stuck on "No open ports detected", you need to update your **Start Command** in Render.

1. Go to your **Render Dashboard**.
2. Select your Web Service.
3. Click on **Settings** in the left sidebar.
4. Scroll down to **Start Command**.
5. **Change it to:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 10000
   ```
6. Click **Save Changes**. Render will automatically redeploy.

---

## 📚 API Usage Guide

Once your API is live (e.g., at `https://your-service-name.onrender.com`), you can use it in **n8n** or any other tool.

### 1. Web Search (Google Simulation)
Search the web for information.
- **Method:** `POST`
- **URL:** `https://your-service-name.onrender.com/api/search`
- **Body (JSON):**
  ```json
  {
    "query": "latest AI news",
    "limit": 5
  }
  ```
- **Response:** Returns a list of titles, links, and snippets.

### 2. Image Search
Find images related to your query.
- **Method:** `POST`
- **URL:** `https://your-service-name.onrender.com/api/images`
- **Body (JSON):**
  ```json
  {
    "query": "cute kittens",
    "limit": 3
  }
  ```

### 3. Visit & Scrape Website
Visit a specific URL and extract all its text content (great for summarizing articles with AI).
- **Method:** `POST`
- **URL:** `https://your-service-name.onrender.com/api/visit`
- **Body (JSON):**
  ```json
  {
    "url": "https://en.wikipedia.org/wiki/Artificial_intelligence"
  }
  ```
- **Response:** Returns the full text content of the page.

---

## 🛠 Local Testing

To run this on your own computer:

1. **Install Python & Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Server:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Open Documentation:**
   Go to `http://localhost:8000/docs` in your browser to test endpoints interactively.
