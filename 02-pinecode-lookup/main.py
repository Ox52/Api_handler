from fastapi import FastAPI
from exceptions import (
    Invalid_pincode_handler,
    InvalidPinCode,
    PinCodeNotFound,
    Pinocde_not_found_handler,
)
from models import LocationResponse, BulkRequest, BulkResponse
from data import pincode_db

app = FastAPI(
    title="pincode lookup API",
    description="auto fill city and state from indian pincode during checkout",
)


# register your custom exception handlers here
app.add_exception_handler(PinCodeNotFound, Pinocde_not_found_handler)
app.add_exception_handler(InvalidPinCode, Invalid_pincode_handler)


@app.get("/")
def root():
    return {"message": "pincode lookup"}


@app.post("/pincode/bulk", response_model=BulkResponse)
def bulk_lookup(request: BulkRequest):
    results = []
    missing = []

    for code in request.pincode:
        if code in pincode_db:
            results.append(pincode_db[code])
        else:
            missing.append(code)

    return BulkResponse(
        found=len(results),
        not_found=len(missing),
        results=results,
        missing=missing,
    )


@app.get("/pincode/{code}", response_model=LocationResponse)
def lookup_pincode(code: str):
    if len(code) != 6 or not code.isdigit():
        raise InvalidPinCode(code, "must be exactly 6 digits")
    if code not in pincode_db:
        raise PinCodeNotFound(code)
    return pincode_db[code]
