# Scientific PDF Analysis Tool

A Python application that processes scientific papers in PDF format and generates detailed scientific analyses using the GPT-4 API.

## Features

- Text extraction from PDF files
- Scientific analysis using GPT-4 API
- Batch PDF processing
- Automatic result reporting
- Error handling and retry mechanism

## Installation

1. Clone the project:
```bash
git clone [repository-url]
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key in `gpt_paper.py`:
```python
# Add your OpenAI API key here
openai.api_key = "your-api-key-here"  # Replace with your actual API key
```

You can get your API key from: https://platform.openai.com/api-keys

## Usage

1. Place your PDF files in the `Papers_Eng` directory.

2. Run the program:
```bash
python gpt_paper.py
```

3. Processed results will be created in the `Papers_Tr` directory.

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