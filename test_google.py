from googlesearch import search
import traceback

print("Testing simple google search...")
try:
    for url in search("python programming", num_results=5, advanced=True):
        print("Result:", url)
except Exception:
    traceback.print_exc()
