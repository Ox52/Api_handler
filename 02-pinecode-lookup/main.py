from fastapi import FastAPI


app = FastAPI(

    title =" pincode lookup API",
    description=" auto fill city and state from indian pincide during checkout"
)


@app.get("/")
def root():
    return{ "message":"pincode lookup"}
