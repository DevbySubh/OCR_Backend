from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pdf2image import convert_from_bytes
import pytesseract

app = FastAPI()

# Allow frontend access (can restrict later)
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
async def ocr_pdf(file: UploadFile = File(...)):
    # Read uploaded PDF
    pdf_bytes = await file.read()

    # Convert ONLY the first page to image
    images = convert_from_bytes(
        pdf_bytes,
        first_page=1,
        last_page=1
    )

    # Run OCR on the first page
    extracted_text = pytesseract.image_to_string(images[0])

    return {
        "text": extracted_text.strip()
    }
