from pydantic import BaseModel

class Card(BaseModel):
    id: int
    name: str
    company: str
    phone: str
    email: str
