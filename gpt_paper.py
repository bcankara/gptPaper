"""
Author: Burak Can KARA
Email: burakcankara@gmail.com

This script processes PDF files and analyzes them using GPT-4 API.
It extracts text from PDFs and generates detailed scientific analysis reports.
"""

import os
import requests
import fitz  # PyMuPDF
import time
from dotenv import load_dotenv
import openai
import deepseek

# Load environment variables
load_dotenv()

# Get configuration from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
API_PROVIDER = os.getenv('API_PROVIDER', 'openai')  # Default to OpenAI
MODEL_NAME = os.getenv('MODEL_NAME', 'gpt-4')      # Default model

# Validate environment variables
if API_PROVIDER == 'openai' and not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file. Please add your API key.")
elif API_PROVIDER == 'deepseek' and not DEEPSEEK_API_KEY:
    raise ValueError("DEEPSEEK_API_KEY not found in .env file. Please add your API key.")

def extract_text_from_pdf(pdf_path):
    """Extracts text content from a PDF file."""
    print(f"Extracting text from {pdf_path}...")
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num in range(doc.page_count):
            print(f"Processing page {page_num + 1}...")
            page = doc.load_page(page_num)
            text += page.get_text()
        doc.close()
        print(f"Text extraction completed for {pdf_path}.")
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

def send_text_to_api(text):
    """Sends text to selected API model and returns detailed analysis."""
    if not text:
        print("Input text is empty. Skipping process.")
        return ""

    print(f"Sending text to {API_PROVIDER} ({MODEL_NAME})...")
    
    prompt = (
        f"Analyze the following text and provide a detailed evaluation according to scientific review process. Output format should be:\n"
        "1. Article Citation\n"
        "Title:\n"
        "Authors:\n"
        "Journal:\n"
        "Volume and Issue:\n"
        "Publication Date:\n"
        "DOI:\n"
        "Publisher:\n"
        "2. Research Purpose and Hypothesis\n"
        "Research Topic:\n"
        "Hypothesis/Problem Statement:\n"
        "3. Participants and Study Area\n"
        "Participant Information:\n"
        "Study Area:\n"
        "4. Methodology\n"
        "Data Collection Method:\n"
        "Tools/Instruments Used:\n"
        "Data Analysis Method:\n"
        "5. Results\n"
        "Key Findings:\n"
        "Statistical Results:\n"
        "6. Authors' Recommendations and Discussion\n"
        "Research Success Status:\n"
        "Authors' Recommendations and Future Research:\n"
        "7. Scientific Contribution and Strengths/Weaknesses\n"
        "Strengths:\n"
        "Weaknesses:\n"
        "8. Summary and Scientific Evaluation\n"
        f"Text: {text}\n"
        "Note: Technical terms (e.g., Multiscale Geographically Weighted Regression - MGRW) should be kept as is without translation."
    )

    try:
        if API_PROVIDER == 'openai':
            openai.api_key = OPENAI_API_KEY
            response = openai.ChatCompletion.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=800
            )
            return response.choices[0].message.content

        elif API_PROVIDER == 'deepseek':
            deepseek.api_key = DEEPSEEK_API_KEY
            response = deepseek.ChatCompletion.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=800
            )
            return response.choices[0].message.content

    except Exception as e:
        print(f"API request error: {e}")
        if "rate limit" in str(e).lower():
            print("Rate limit reached. Waiting 15 seconds...")
            time.sleep(15)
            return send_text_to_api(text)  # Retry
        return ""

def process_pdfs_in_directory(directory_path, output_directory):
    """Processes PDF files in the specified directory and saves the results."""
    print(f"Processing PDF files in {directory_path}...")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Created directory: {output_directory}")

    for filename in os.listdir(directory_path):
        if filename.lower().endswith(".pdf"):
            print(f"Processing file: {filename}")
            pdf_path = os.path.join(directory_path, filename)
            text = extract_text_from_pdf(pdf_path)
            api_response = send_text_to_api(text)

            if api_response:
                # Save the result
                output_file_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_output.txt")
                with open(output_file_path, "w", encoding="utf-8") as output_file:
                    output_file.write(api_response)

                print(f"Processed {filename} and saved results to {output_file_path}")
            else:
                print(f"Error processing {filename}, results not saved.")

if __name__ == "__main__":
    pdf_directory = "Papers"     # Directory containing PDF files
    output_directory = "Result"  # Directory for saving results
    print("Starting PDF processing...")
    process_pdfs_in_directory(pdf_directory, output_directory)
    print("PDF processing completed.")
