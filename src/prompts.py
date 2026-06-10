EXTRACTION_PROMPT = """
Extract the following information from the contract:

- party_a
- party_b
- contract_type
- start_date
- salary
- notice_period
- key_obligations

Return valid JSON only.

Contract:
{contract_text}
"""
