from pydantic.main import BaseModel


class SummaryPayloadSchema(BaseModel):
    url: str


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int
