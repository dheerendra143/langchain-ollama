import uvicorn

def start():
  uvicorn.run("poetry_fastapi.src.app:app", host="0.0.0.0", port=3000, reload=True)