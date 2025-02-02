# Scientific PDF Analysis Tool

A Python application that processes scientific papers in PDF format and generates detailed scientific analyses using AI models (OpenAI GPT or DeepSeek).

## Features

- Text extraction from PDF files
- Scientific analysis using AI models (OpenAI GPT-4/3.5 or DeepSeek)
- Multiple AI provider support
- Batch PDF processing
- Automatic result reporting
- Error handling and retry mechanism
- Configurable model selection

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
   - Add your API keys (OpenAI and/or DeepSeek)
   - Select your preferred API provider and model

Example `.env` file:
```bash
# API Configuration
OPENAI_API_KEY=your-openai-api-key-here
DEEPSEEK_API_KEY=your-deepseek-api-key-here

# Model Selection
API_PROVIDER=openai     # Options: openai, deepseek
MODEL_NAME=gpt-4       # OpenAI options: gpt-4, gpt-3.5-turbo
                      # DeepSeek options: deepseek-chat, deepseek-coder
```

You can get your API keys from:
- OpenAI API key: https://platform.openai.com/api-keys
- DeepSeek API key: https://platform.deepseek.ai/api-keys

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
- Each PDF analysis consumes API tokens
- Token consumption depends on:
  - Length of the PDF document
  - Selected model (GPT-4 costs more than GPT-3.5-turbo)
  - Selected API provider (pricing varies between OpenAI and DeepSeek)
  - Number of API calls made
- Monitor your API usage at:
  - OpenAI: https://platform.openai.com/usage
  - DeepSeek: https://platform.deepseek.ai/usage

### Processing Time
- Processing time varies based on:
  - PDF size and complexity
  - Number of files being processed
  - API response time
  - Rate limiting and retry mechanisms
  - Selected API provider and model

### Best Practices
- Start with a small number of PDFs to test the system
- Monitor the console output for processing status
- Keep PDFs in English for best results
- Ensure PDFs are text-searchable (not scanned images)
- Check your API keys have sufficient credits before processing large batches
- Compare results between different models and providers

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