from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from services import search_engine, web_content_scraper

app = FastAPI(
    title="Custom Search & Scraper API",
    description="API for searching Google/Yahoo/etc (via DuckDuckGo) and scraping website content.",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchRequest(BaseModel):
    query: str
    limit: int = 10
    engine: str = "google"  # Placeholder for future expansion (google, yahoo, bing)

class VisitRequest(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"status": "running", "message": "Welcome to the Custom Search API"}

from fastapi.concurrency import run_in_threadpool

@app.post("/api/search")
async def search(request: SearchRequest):
    """
    Search for web results.
    """
    try:
        results = await run_in_threadpool(search_engine.search_web, request.query, request.limit, request.engine)
        return {"query": request.query, "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/images")
async def search_images(request: SearchRequest):
    """
    Search for images.
    """
    try:
        results = await run_in_threadpool(search_engine.search_images, request.query, request.limit)
        return {"query": request.query, "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/videos")
async def search_videos(request: SearchRequest):
    """
    Search for videos.
    """
    try:
        results = await run_in_threadpool(search_engine.search_videos, request.query, request.limit)
        return {"query": request.query, "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/visit")
async def visit_page(request: VisitRequest):
    """
    Visit a URL and scrape its content.
    """
    try:
        data = await run_in_threadpool(web_content_scraper.scrape_website, request.url)
        if "error" in data:
            raise HTTPException(status_code=400, detail=data["error"])
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
