from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
STATIC = BASE / "static"

app = FastAPI(title="Primavera MAF")

app.mount("/assets", StaticFiles(directory=str(STATIC / "assets")), name="assets")

@app.get("/")
async def index():
    return FileResponse(str(STATIC / "index.html"))

@app.get("/{path:path}")
async def fallback():
    return FileResponse(str(STATIC / "index.html"))
