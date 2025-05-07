from mistralai import Mistral
from dotenv import load_dotenv
import datauri
import os
import base64
import requests

def encode_pdf(pdf_path):
    """Encode the pdf to base64."""
    try:
        with open(pdf_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {pdf_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None

load_dotenv()
api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

# Local PDF file path
pdf_path = r"E:\Document_Processing_AI\Image_Quality_Module\Test_Files\Bank Statement Example Final.pdf"  # ← Change to your actual file name/path

# Getting the base64 string
base64_pdf = encode_pdf(pdf_path)

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_url",
        "document_url": f"data:application/pdf;base64,{base64_pdf}" 
    }
)

# Print output
for i, page in enumerate(ocr_response.pages):
    print(f"\n--- Page {i + 1} ---\n")
    print(page.markdown)
