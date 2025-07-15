from pydantic import BaseModel

class ScanResult(BaseModel):
    card_id: int
    text: str
    confidence: float
