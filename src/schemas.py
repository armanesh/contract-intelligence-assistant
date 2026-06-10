from pydantic import BaseModel
from typing import List, Optional


class ContractExtraction(BaseModel):
    party_a: Optional[str]
    party_b: Optional[str]
    contract_type: Optional[str]
    start_date: Optional[str]
    salary: Optional[str]
    notice_period: Optional[str]
    key_obligations: List[str]
