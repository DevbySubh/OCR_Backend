from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access backend (restrict later if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "Backend is running on Render"}

@app.post("/ocr")
async def receive_pdf(file: UploadFile = File(...)):
    return {
        "message": "File received successfully",
        "original_name": file.filename or "uploaded.pdf"
    }
