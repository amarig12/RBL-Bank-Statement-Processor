# Tests if PDF extraction returns correct details
def test_pdf_extraction(extracted_data, expected_summary, expected_transactions):
    extracted_summary, extracted_transactions, incoming_transactions, outgoing_transactions = extracted_data

    assert extracted_summary == expected_summary, "Extracted summary does not match expected output."
    assert extracted_transactions == expected_transactions, "Extracted transactions do not match expected output."

# Tests incoming and outgoing returns the right amount
def test_math(validate_math, expected_summary):

    incoming_total, outgoing_total = validate_math

    expected_incoming_total = expected_summary["Deposits & Other Credits"]
    expected_outgoing_total = -expected_summary["Cheques & Other Debits"]

    assert incoming_total == expected_incoming_total, "Incoming total do not match expected output."
    assert outgoing_total == expected_outgoing_total, "Outgoing total do not match expected output."

# Tests mathematical consistency (opening balance + sum of transactions = closing balance)
def test_math_closing(validate_math, expected_summary):
    incoming_total, outgoing_total = validate_math

    opening_balance = expected_summary["Opening Balance"]
    closing_balance = expected_summary["Closing Balance"]

    sum_of_transactions = incoming_total + outgoing_total 
    expected_closing = opening_balance + sum_of_transactions

    assert closing_balance == expected_closing, "Closing balance do not match expected output"
