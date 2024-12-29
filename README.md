# Scientific PDF Analysis Tool

A Python application that processes scientific papers in PDF format and generates detailed scientific analyses using the GPT-4 API.

## Features

- Text extraction from PDF files
- Scientific analysis using GPT-4 API
- Batch PDF processing
- Automatic result reporting
- Error handling and retry mechanism
- Configurable OpenAI model selection

## Installation

1. Clone the project:
```bash
git clone [repository-url]
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory:
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key
   - Select your preferred model (gpt-4 or gpt-3.5-turbo)

Example `.env` file:
```bash
# OpenAI Configuration
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=gpt-4  # Options: gpt-4, gpt-3.5-turbo
```

You can get your API key from: https://platform.openai.com/api-keys

## Usage

1. Place your PDF files in the `Papers` directory:
   - The program will process all PDF files in this directory
   - Files are processed sequentially in alphabetical order
   - Each PDF is analyzed independently

2. Run the program:
```bash
python gpt_paper.py
```

3. Check results in the `Result` directory:
   - For each PDF, a corresponding .txt file is created
   - Output files are named as: `[original_pdf_name]_output.txt`
   - Results include detailed scientific analysis in a structured format

## Important Notes

### API Token Usage
- Each PDF analysis consumes OpenAI API tokens
- Token consumption depends on:
  - Length of the PDF document
  - Selected GPT model (GPT-4 costs more than GPT-3.5-turbo)
  - Number of API calls made
- Monitor your OpenAI API usage at: https://platform.openai.com/usage

### Processing Time
- Processing time varies based on:
  - PDF size and complexity
  - Number of files being processed
  - API response time
  - Rate limiting and retry mechanisms

### Best Practices
- Start with a small number of PDFs to test the system
- Monitor the console output for processing status
- Keep PDFs in English for best results
- Ensure PDFs are text-searchable (not scanned images)
- Check your API key has sufficient credits before processing large batches

## Output Format

The analysis report generated for each PDF includes:

1. Article Citation
   - Title
   - Authors
   - Journal
   - Volume and Issue
   - Publication Date
   - DOI
   - Publisher

2. Research Purpose and Hypothesis
   - Research Topic
   - Hypothesis/Problem Statement

3. Participants and Study Area
   - Participant Information
   - Study Area

4. Methodology
   - Data Collection Method
   - Tools/Instruments Used
   - Data Analysis Method

5. Results
   - Key Findings
   - Statistical Results

6. Authors' Recommendations and Discussion
   - Research Success Status
   - Authors' Recommendations and Future Research

7. Scientific Contribution and Strengths/Weaknesses
   - Strengths
   - Weaknesses

8. Summary and Scientific Evaluation

## Author

Burak Can KARA
Email: burakcankara@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE file for details. 