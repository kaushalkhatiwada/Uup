from fastapi import FastAPI, HTTPException, Query
import requests
from typing import Optional

app = FastAPI(
    title="HTTP/HTTPS Checker API",
    description="API to check HTTP and HTTPS status for websites",
    version="1.0.0"
)

@app.get("/check")
def check(target: str = Query(..., description="Domain to check (e.g., example.com)"), 
          timeout: int = Query(5, description="Timeout in seconds")):
    
    if "." not in target or " " in target:
        raise HTTPException(status_code=400, detail="Bad Request")

    def get_status(scheme: str) -> Optional[int]:
        try:
            response = requests.get(f"{scheme}://{target}", timeout=timeout)
            return response.status_code
        except requests.RequestException:
            return None

    http_status = get_status("http")
    https_status = get_status("https")

    if http_status is None and https_status is None:
        return {
            "target": target,
            "error": "Status Unknown"
        }

    return {
        "target": target,
        "http_status": http_status,
        "https_status": https_status
    }

