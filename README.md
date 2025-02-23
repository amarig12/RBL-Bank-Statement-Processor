# RBL Bank Statement Processor

## Project Overview
This Python script extracts financial data from RBL PDF bank statements, validates the data mathematically, classifies transactions (incoming or outgoing), and produces a structured Excel output.

## Key Features:
- Extracts account holder information (name, account type, and account number), statement period, balances, and transactions from PDFs.
- Validates mathematical consistency of transactions.
- Classifies transactions as "incoming" or "outgoing."
- Flags suspicious or inconsistent transactions for manual review.
- Generates an Excel report with a summary, transaction details, and flagged items.


## Setup Instructions

### Requirements
- Python 3.8
- Dependencies listed in `requirements.txt`

### Installation
1. Clone the repository:
   git clone --branch amari https://github.com/amarig12/RBL-Bank-Statement-Processor.git
   cd RBL-Bank-Statement-Processor

2. Create and activate a virtual environment:
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use venv\Scripts\activate

3. Install dependencies:
    pip3 install -r requirements.txt

## Usage Guide

### Command-Line Execution
To run the script, execute the following command in your terminal:
python3 main.py

#### Important:
Before running the script, ensure that your bank statements in PDF format are placed in the bank_statements folder.

Additionally, you can specify the folder for bank statements and where the Excel output files should be saved by editing the config.json configuration file.


### Example Usage:
python3 main.py

## Implementation Details

### Architecture Overview
The script consists of modular components:

- PDF Extraction Module: Extracts data using pdfplumber.
- Validation Module: Ensures transactions sum correctly and flags inconsistencies.
- Classification Module: Categorizes transactions into incoming and outgoing.
- Excel Generation Module: Outputs structured financial data.


#### Key Algorithms & Techniques
- Uses pdfplumber for text extraction and structured parsing.
- Uses openpyxl for Excel report generation.
- Testing
- Running Tests

##### To run the tests, execute:

python3 -m pytest tests/


## Test Coverage
- Mathematical validation tests.
- PDF extraction consistency tests.
- Classification correctness tests.
- Limitations & Future Improvements


## Known Limitations
- Currently specific to RBL PDF formats.


## Potential Enhancements
- Implement OCR support for scanned statements.
- Add multi-language support for multi-language statements.
- Improve machine learning-based classification for transaction categorization.
