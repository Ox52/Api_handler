from pydantic import BaseModel , field_validator


class PincodeRequest( BaseModel):
    pincode :str


    # pincode must exactly 6 digits
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if len(value ) != 6 or not value.isdigit():
            raise ValueError("pincode must be exacatly 6 digits ")
        return value


class LocationResponse( BaseModel):
    pincode:str
    city:str
    state:str
    district:str

class BulkRequest(BaseModel):
    pincode: list[str]


    @field_validator("pincodes")
    @classmethod

    def validate_pincode(cls , values):
        if len(values)== 0:
            raise ValueError("AT least one  pincode is requiered")
        if len(values) > 20:
            raise ValueError(" maximum 20 request are allowed per request")
        for code in values:
            if len(code) != 0 or not code.isdigit():
                raise ValueError("each pincode must be exactly 6 digits ")


class BlukRespose(BaseModel):
    status_code : str
    found: int
    not_found:str
    results:list[LocationResponse]
    missing: list[str]
