import pytest
import os
from main import parent


@pytest.fixture
def sample_pdf_path():
    """Returns the file path of a sample test PDF."""
    # Get current script's directory
    current_folder = os.path.dirname(__file__)  
    file_path = os.path.join(current_folder, "test_statement/test_statement_1.pdf")
    excel_path = os.path.join(current_folder, "test_excel/test_statement_1.xlsx")

    return file_path, excel_path

@pytest.fixture
def extracted_data(sample_pdf_path):
    """Processes the sample PDF and extracts both summary and transactions."""
    file_path, excel_output = sample_pdf_path  # Automatically provided by pytest fixture
    process_pdf_pages, extract_statement_details, extract_transactions, incoming_transactions, outgoing_transactions = parent(file_path, excel_output)

    nested_list = process_pdf_pages(file_path)
    extracted_summary = extract_statement_details(nested_list)
    extracted_transactions, extracted_incomplete_transactions = extract_transactions(nested_list)

    return extracted_summary, extracted_transactions, incoming_transactions, outgoing_transactions

@pytest.fixture
def expected_summary():
    """Provides the expected summary data for validation."""
    return {
        "Account Holder": "AMARI MICHAEL GORDON",
        "Account Type": "CHQ",
        "Account Number": "XXXX-XXXX-9123",
        "Statement Period Start": "25/12/2022",
        "Statement Period End": "24/03/2023",
        "Opening Balance": 1000.00,
        "Closing Balance": 2750.00,
        "Deposits & Other Credits": 2000.00,
        "Cheques & Other Debits": 250.00
    }

@pytest.fixture
def expected_transactions():
    """Provides the expected transactions data for validation."""
    return [
            {"Date": "25/12", "Description": "Maintenance Fee", "Amount": 2000.00, "Balance": 3000.00, "Type": "Incoming"},
            {"Date": "26/12", "Description": "Interest Credit", "Amount": -150.00, "Balance": 2850.00, "Type": "Outgoing"},
            {"Date": "29/12", "Description": "DIGITAL TICKETS LTD WOODBROOK TT", "Amount": -100.00, "Balance": 2750.00, "Type": "Outgoing"},
        ]

@pytest.fixture
def validate_math(extracted_data):
    extracted_summary, extracted_transactions, incoming_transactions, outgoing_transactions = extracted_data

    incoming = incoming_transactions(extracted_transactions)
    outgoing = outgoing_transactions(extracted_transactions)

    incoming_total = 0  # Initialize outgoing total
    for t in incoming:
        try:
            amount = t['Amount']
            incoming_total += float(amount) if amount else 0
        except ValueError:
            pass  # Handle case where amount isn't a valid number

    outgoing_total = 0  # Initialize outgoing total
    for t in outgoing:
        try:
            amount = t['Amount']
            outgoing_total += float(amount) if amount else 0
        except ValueError:
            pass  # Handle case where amount isn't a valid number

    return incoming_total, outgoing_total

