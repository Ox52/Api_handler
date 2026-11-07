from fastapi.responses import JSONResponse
from fastapi import Request


class PinCodeNotFound(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode
        super().__init__(f"pincode not found: {pincode}")


class InvalidPinCode(Exception):
    def __init__(self, pincode: str, reason: str = "Invalid error"):
        self.pincode = pincode
        self.reason = reason
        super().__init__(f"invalid pincode: {pincode} ({reason})")


# custom handler

async def Pinocde_not_found_handler(request: Request, exc: PinCodeNotFound):
    return JSONResponse(
        status_code=404,
        content={
            "error": "pincode_not_found",
            "message": f"no location exists for this pincode {exc.pincode}",
            "pincode": exc.pincode,
        },
    )


async def Invalid_pincode_handler(request: Request, exc: InvalidPinCode):
    return JSONResponse(
        status_code=422,
        content={
            "error": "pincode_invalid",
            "message": f"invalid pincode {exc.pincode}: {exc.reason}",
            "pincode": exc.pincode,
        },
    )
