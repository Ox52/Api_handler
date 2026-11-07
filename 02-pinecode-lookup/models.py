from pydantic import BaseModel, field_validator


class PincodeRequest(BaseModel):
    pincode: str

    # pincode must be exactly 6 digits
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if len(value) != 6 or not value.isdigit():
            raise ValueError("pincode must be exactly 6 digits")
        return value


class LocationResponse(BaseModel):
    pincode: str
    city: str
    state: str
    district: str


class BulkRequest(BaseModel):
    pincode: list[str]

    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, values):
        if len(values) == 0:
            raise ValueError("At least one pincode is required")
        if len(values) > 20:
            raise ValueError("maximum 20 pincodes are allowed per request")
        for code in values:
            if len(code) != 6 or not code.isdigit():
                raise ValueError("each pincode must be exactly 6 digits")
        return values


class BulkResponse(BaseModel):
    found: int
    not_found: int
    results: list[LocationResponse]
    missing: list[str]
