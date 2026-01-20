from pydantic import BaseModel

class TextAnalysisRequest(BaseModel):
    subject: str
    body: str
