import json

from fastapi import FastAPI, Request
from starlette.responses import StreamingResponse

app = FastAPI()

# Helper function to simulate scan steps
def simulate_scan_steps(url):
    results = {
        "title": f"Title of {url}",
        "description": f"Description of {url}",
        "domain_age": "5 years",
        "emails": ["admin@example.com", "info@example.com"],
        "meta": ["viewport", "description"],
        "tech_stack": ["Bootstrap", "jQuery"],
        "socials": ["https://twitter.com/example"]
    }
    steps = [json.dumps(results) for _ in range(5)]  # simulate 5 steps
    for chunk in steps:
        yield chunk.encode("utf-8")

@app.post("/scan")
async def scan(request: Request):
    data = await request.json()
    url = data.get("url")
    if not url:
        return {"error": "No URL provided"}

    return StreamingResponse(simulate_scan_steps(url), media_type="application/json")

